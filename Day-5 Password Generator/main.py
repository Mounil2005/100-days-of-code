import streamlit as st
import random
import string

st.set_page_config(page_title="Password Generator", page_icon="🔐", layout="centered")
st.title("🔐 Secure Password Generator")

st.markdown("""
Generate strong passwords with customizable options.
""")

# --- User Inputs ---
length = st.slider("Select password length:", min_value=4, max_value=32, value=12)
use_upper = st.checkbox("Include uppercase letters (A-Z)", value=True)
use_lower = st.checkbox("Include lowercase letters (a-z)", value=True)
use_digits = st.checkbox("Include numbers (0-9)", value=True)
use_symbols = st.checkbox("Include symbols (!@#$%)", value=True)

# --- Character Set ---
char_set = ""
if use_upper:
    char_set += string.ascii_uppercase
if use_lower:
    char_set += string.ascii_lowercase
if use_digits:
    char_set += string.digits
if use_symbols:
    char_set += string.punctuation

# --- Generate Password ---
def generate_password(length):
    if not char_set:
        return "Please select at least one character type."
    return ''.join(random.choice(char_set) for _ in range(length))

# if st.button("Generate Password"):
#     password = generate_password(length)
#     st.success(f"Generated Password: **{password}**")
#     st.code(password, language='')
#     st.caption("Click to copy manually.")

if st.button("Generate Password"):
    password = generate_password(length)
    st.session_state["password"] = password  # Save in session state
    st.success(f"Generated Password: **{password}**")
    st.code(password, language='')
    st.caption("Click to copy manually.")


# --- Optional Save (simulated local memory) ---
save = st.checkbox("Save this password (local session only)")
if save:
    site = st.text_input("Website / App")
    email = st.text_input("Email / Username")
    if site and email and st.button("Save Entry"):
        st.session_state.setdefault("saved", []).append({
            "site": site,
            "email": email,
            "password": st.session_state.get("password", "")
})

        st.success("Saved locally!")

# --- Display Saved ---
if "saved" in st.session_state:
    st.subheader("🔒 Saved Credentials (session only)")
    for item in st.session_state["saved"]:
        st.write(f"**{item['site']}** | {item['email']} | `{item['password']}`")

