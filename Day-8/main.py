# import streamlit as st
# from PIL import Image
# import io

# st.set_page_config(page_title="📐 Image Resizer", page_icon="🖼️", layout="centered")

# # Title
# st.title("📐 Image Resizer App")
# st.caption("Resize any image with optional aspect ratio lock")

# # Upload Image
# uploaded_image = st.file_uploader("📂 Upload your image (JPG or PNG)", type=["jpg", "jpeg", "png"])

# if uploaded_image:
#     img = Image.open(uploaded_image)
#     st.image(img, caption="Original Image", use_container_width=True)

#     st.markdown("---")
#     st.subheader("Resize Options")

#     # Original dimensions
#     orig_width, orig_height = img.size

#     # Checkbox for aspect ratio
#     keep_aspect = st.checkbox("🔒 Maintain aspect ratio", value=True)

#     # Resize inputs
#     new_width = st.number_input("Width (px)", min_value=1, max_value=5000, value=orig_width)
    
#     if keep_aspect:
#         # Calculate proportional height
#         aspect_ratio = orig_height / orig_width
#         new_height = int(new_width * aspect_ratio)
#         st.markdown(f"Height auto-calculated: **{new_height}px**")
#     else:
#         new_height = st.number_input("Height (px)", min_value=1, max_value=5000, value=orig_height)

#     if st.button("🔄 Resize Image"):
#         resized_img = img.resize((new_width, new_height))
#         st.success("✅ Image resized successfully!")
#         st.image(resized_img, caption="Resized Image", use_container_width=True)

#         # Download resized image
#         img_bytes = io.BytesIO()
#         resized_img.save(img_bytes, format="PNG")
#         st.download_button(
#             label="📥 Download Resized Image",
#             data=img_bytes.getvalue(),
#             file_name="resized_image.png",
#             mime="image/png"
#         )


import streamlit as st
from PIL import Image
import io
import os

st.set_page_config(page_title="📐 Image Resizer & Compressor", page_icon="🖼️")

st.title("📐 Image Resizer & Compressor")
st.caption("Resize any image with optional aspect ratio lock and compression")

# Upload image
uploaded_image = st.file_uploader("📂 Upload a JPG or PNG image", type=["jpg", "jpeg", "png"])

if uploaded_image:
    # Load image
    img = Image.open(uploaded_image)
    orig_width, orig_height = img.size

    # File size in KB
    original_size_kb = len(uploaded_image.getvalue()) // 1024

    st.image(img, caption="Original Image", use_container_width=True)

    st.markdown(f"**Original Size**: {orig_width} × {orig_height} px | {original_size_kb} KB")

    st.markdown("---")
    st.subheader("Resize Options")

    keep_aspect = st.checkbox("🔒 Maintain Aspect Ratio", value=True)
    new_width = st.number_input("Width (px)", min_value=1, max_value=5000, value=orig_width)

    if keep_aspect:
        aspect_ratio = orig_height / orig_width
        new_height = int(new_width * aspect_ratio)
        st.markdown(f"Height auto-calculated: **{new_height}px**")
    else:
        new_height = st.number_input("Height (px)", min_value=1, max_value=5000, value=orig_height)

    st.markdown("---")
    st.subheader("Compression (JPG only)")
    compress = st.checkbox("📦 Enable Compression")
    quality = 100
    if compress:
        quality = st.slider("Compression Quality", min_value=10, max_value=100, value=80, step=5)

    if st.button("🔄 Resize Now"):
        resized_img = img.resize((new_width, new_height))

        # Save to BytesIO
        img_bytes = io.BytesIO()
        img_format = img.format if img.format in ["JPEG", "PNG"] else "PNG"

        if img_format == "JPEG" and compress:
            resized_img.save(img_bytes, format=img_format, quality=quality, optimize=True)
        else:
            resized_img.save(img_bytes, format=img_format)

        resized_img_bytes = img_bytes.getvalue()
        resized_img_size_kb = len(resized_img_bytes) // 1024

        st.success("✅ Image resized successfully!")
        st.image(resized_img, caption="Resized Image", use_container_width=True)

        st.markdown(f"**Resized Size**: {new_width} × {new_height} px | {resized_img_size_kb} KB")

        st.download_button(
            label="📥 Download Resized Image",
            data=resized_img_bytes,
            file_name=f"resized_image.{img_format.lower()}",
            mime=f"image/{img_format.lower()}"
        )
else:
    st.info("👆 Upload an image to get started.")
