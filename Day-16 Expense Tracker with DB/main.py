import streamlit as st
import pandas as pd
import sqlite3
from datetime import date


def init_db():
    conn = sqlite3.connect("expenses.db")
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            amount REAL,
            category TEXT,
            description TEXT,
            date TEXT,
            mode TEXT,
            type TEXT
        )
    """)
    c.execute("""
        CREATE TABLE IF NOT EXISTS balance (
            id INTEGER PRIMARY KEY CHECK (id = 0),
            current_balance REAL
        )
    """)
    c.execute("INSERT OR IGNORE INTO balance (id, current_balance) VALUES (0, 0.0)")
    conn.commit()
    conn.close()

def get_balance():
    conn = sqlite3.connect("expenses.db")
    c = conn.cursor()
    c.execute("SELECT current_balance FROM balance WHERE id = 0")
    balance = c.fetchone()[0]
    conn.close()
    return balance

def update_balance(new_balance):
    conn = sqlite3.connect("expenses.db")
    c = conn.cursor()
    c.execute("UPDATE balance SET current_balance = ? WHERE id = 0", (new_balance,))
    conn.commit()
    conn.close()

def add_expense(amount, category, description, date, mode, trans_type):
    conn = sqlite3.connect("expenses.db")
    c = conn.cursor()
    c.execute("""
        INSERT INTO expenses (amount, category, description, date, mode, type)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (amount, category, description, str(date), mode, trans_type))
    conn.commit()
    conn.close()

def get_expenses():
    conn = sqlite3.connect("expenses.db")
    df = pd.read_sql_query("SELECT * FROM expenses ORDER BY date DESC", conn)
    conn.close()
    return df



st.title("💰 Expense Tracker with Backend")
init_db()



balance = get_balance()
if "balance_set" not in st.session_state:
    st.session_state.balance_set = balance > 0

if not st.session_state.balance_set:
    with st.expander("💰 Set Initial Balance", expanded=True):
        user_input = st.text_input("Set Starting Balance", key="starting_balance")
        try:
            if st.button("Update Balance"):
                current_balance = float(user_input)
                update_balance(current_balance)
                st.session_state.balance_set = True
                st.success(f"Balance set to ₹{current_balance}")
        except ValueError:
            st.error("Please enter a valid number.")


amount = st.text_input("Enter amount", placeholder="Enter amount")
category = st.selectbox("Category", ["Food", "Transport", "Shopping", "Bills", "Other"])
description = st.text_input("Short description")
expense_date = st.date_input("Date", value=date.today())
mode = st.selectbox("Payment Mode", ["Online", "Cash"])
trans_type = st.radio("Transaction Type", ["Cash in", "Cash out"])

if st.button("Add Entry"):
    try:
        if amount.strip() == "":
            st.error("Amount field cannot be empty.")
        else:
            amount = float(amount)

            
            current_balance = get_balance()
            if trans_type == "Cash in":
                current_balance += amount
            else:
                current_balance -= amount

            update_balance(current_balance)

            
            add_expense(amount, category, description, expense_date, mode, trans_type)

            st.success(f"Added ₹{amount:.2f} for {category} on {expense_date}")
    except ValueError:
        st.error("Please enter a valid amount.")



df = get_expenses()
if not df.empty:
    st.subheader("🧾 All Transactions")
    st.dataframe(df, use_container_width=True)

    st.subheader("📊 Monthly Summary")
    df["Month"] = pd.to_datetime(df["date"]).dt.to_period("M")
    monthly_summary = df.groupby(["Month", "category"])["amount"].sum().reset_index()
    st.dataframe(monthly_summary)

    balance = get_balance()
    st.metric("Current Balance", f"₹{balance:.2f}")

    csv = df.to_csv(index=False).encode("utf-8")
    st.download_button("📥 Download CSV", csv, "expenses.csv", "text/csv")

else:
    st.info("No transactions yet.")
