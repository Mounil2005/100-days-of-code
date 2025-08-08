import streamlit as st

st.set_page_config(page_title="Secret Auction")

st.title("Secret Auction Program")

if 'bidders' not in st.session_state:
    st.session_state.bidders = {}

with st.form("auction_form"):
    name = st.text_input("Enter your name")
    bid = st.number_input("Enter your bid (₹)", min_value=1, step=1)

    submitted = st.form_submit_button("Submit Bid")

    if submitted:
        if name:
            st.session_state.bidders[name] = bid
            st.success("✅ Bid submitted successfully!")
        else:
            st.error("❌ Name cannot be empty!")

st.write("### Current Bidders:")
st.write(f"{len(st.session_state.bidders)} bids placed so far.")

if st.button("Reveal Winner"):
    if st.session_state.bidders:
        winner = max(st.session_state.bidders, key=st.session_state.bidders.get)
        highest = st.session_state.bidders[winner]
        st.success(f"🏆 The winner is **{winner}** with a bid of ₹{highest}")
    else:
        st.warning("No bids yet!")
