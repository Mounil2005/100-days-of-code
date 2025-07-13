import streamlit as st
from PIL import Image
from rembg import remove
import io

st.set_page_config(page_title="Background Remover")
st.title("🪄 Remove Image Background")


# Upload image
uploaded_image = st.file_uploader("Upload an image (JPG/PNG)", type=["jpg", "jpeg", "png"])

if uploaded_image:
    st.image(uploaded_image, caption="Original Image", use_container_width=True)

    if st.button("Remove Background"):
        with st.spinner("Processing..."):
            input_image = Image.open(uploaded_image)
            output_image = remove(input_image)

            # Show result
            st.image(output_image, caption="Image without Background", use_container_width=True)

            # Download button
            img_bytes = io.BytesIO()
            output_image.save(img_bytes, format="PNG")
            st.download_button(
                label="Download PNG",
                data=img_bytes.getvalue(),
                file_name="no_background.png",
                mime="image/png"
            )

