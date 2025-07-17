
import streamlit as st
import qrcode
from PIL import Image
from io import BytesIO

st.set_page_config(page_title="QR Code Generator", page_icon="🔳")

st.title("QR Code Generator")
st.write("Generate a custom QR Code for your text or URL.")

# User input
data = st.text_input("Enter the text or URL to encode", "https://example.com")

# Color customization
col1, col2 = st.columns(2)
with col1:
    fill_color = st.color_picker("Choose QR color", "#000000")
with col2:
    back_color = st.color_picker("Choose background color", "#ffffff")

# Generate QR Code
if st.button("Generate QR Code"):
    qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=4
    )
    qr.add_data(data)
    qr.make(fit=True)

    # Convert to standard RGB image
    img = qr.make_image(fill_color=fill_color, back_color=back_color).convert("RGB")

    # Display in Streamlit
    st.image(img, caption="Your QR Code", use_container_width=True)

    # Prepare image for download
    buffered = BytesIO()
    img.save(buffered, format="PNG")

    st.download_button(
        label="Download QR Code",
        data=buffered.getvalue(),
        file_name="qr_code.png",
        mime="image/png"
    )
