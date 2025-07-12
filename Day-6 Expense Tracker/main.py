import streamlit as st
import pandas as pd
from datetime import date

st.title("💰 Expense Tracker")


if "expenses" not in st.session_state:
    st.session_state["expenses"]=[]

if "balance" not in st.session_state:
    st.session_state["balance"] = 0.0

if "balance_set" not in st.session_state:
    st.session_state.balance_set = False

if not st.session_state.balance_set:
    with st.expander("💰 Set initial Balance", expanded=True):        
        user_input=st.text_input("Set Starting Balance", key="starting_balance")
        try:
            if st.button("Update Balance"):
                current_balance = float(user_input)
                st.session_state["balance"] = current_balance
                st.session_state.balance_set = True  # Collapse next time
                st.success(f"Balance set to {current_balance}")
        except ValueError:
            st.error("Please enter a valid number.")

amount=st.text_input("Enter amount", placeholder="Enter amount")



category=st.selectbox("Category", ["Food","Transport","Shopping","Bills","Other"])

description=st.text_input("Short description")

expense_date=st.date_input("Date",value=date.today())

mode=st.selectbox("Payment Mode",["Online","Cash"])

trans_type=st.radio("Transaction Type",["Cash in","Cash out"])


if st.button("Add Entry"):
    try:
        if amount.strip()=="":
            st.error("Amount field cannot be empty.")
        else:
            amount=float(amount)
            new_expense={
                
                "Amount":amount,
                "Category":category,
                "Description":description,
                "Date":expense_date,
                "Mode": mode,
                "Type": trans_type
        }
        if trans_type=="Cash in":
            st.session_state.balance+=amount
        else:
            st.session_state.balance-=amount


        st.session_state.expenses.append(new_expense)
        st.success(f"Added:₹{amount} for {category} on {expense_date}")
    except ValueError:
        st.error("Please enter a valid amount.")



if st.session_state.expenses:
    df=pd.DataFrame(st.session_state.expenses)
    st.subheader("🧾 All Transactions")
    st.dataframe(df, use_container_width=True)

    st.subheader("📊 Monthly Summary")

    df["Month"] = pd.to_datetime(df["Date"]).dt.to_period("M")
    monthly_summary = df.groupby(["Month", "Category"])["Amount"].sum().reset_index()

    st.dataframe(monthly_summary)   


    st.metric("Current Balance", f"₹{st.session_state.balance:.2f}")

    csv=df.to_csv(index=False).encode("utf-8")
    st.download_button("📥 Download CSV",csv,"expenses.csv","text/csv")