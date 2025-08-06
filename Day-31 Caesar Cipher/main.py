import streamlit as st

alphabet = [chr(i) for i in range(97, 123)]  # 
def encrypt(original_text, shift_amount):
    cipher_text = ""
    for letter in original_text:
        if letter in alphabet:
            shifted_position = (alphabet.index(letter) + shift_amount) % len(alphabet)
            cipher_text += alphabet[shifted_position]
        else:
            cipher_text += letter  
    return cipher_text

def decrypt(original_text, shift_amount):
    msg = ""
    for letter in original_text:
        if letter in alphabet:
            shifted_position = (alphabet.index(letter) - shift_amount) % len(alphabet)
            msg += alphabet[shifted_position]
        else:
            msg += letter  
    return msg


st.set_page_config(page_title="🔐 Caesar Cipher", page_icon="🔏")

st.title("🔏 Caesar Cipher Encoder/Decoder")

direction = st.radio("Choose the operation:", ["Encode", "Decode"])
text = st.text_input("Enter your message:", "")
shift = st.slider("Choose the shift amount:", min_value=1, max_value=25, value=3)

if st.button("Submit"):
    if text == "":
        st.warning("Please enter a message to continue.")
    else:
        if direction.lower() == "encode":
            result = encrypt(text.lower(), shift)
            st.success(f"✅ Encoded message: `{result}`")
        elif direction.lower() == "decode":
            result = decrypt(text.lower(), shift)
            st.success(f"✅ Decoded message: `{result}`")

st.markdown("---")
st.caption("Made with ❤️ by Mounil | Day 31 of #100DaysOfCode")
