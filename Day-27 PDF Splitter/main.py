import streamlit as st
from PyPDF2 import PdfReader, PdfWriter
import io

st.set_page_config(page_title="PDF Splitter", layout="centered")
st.title("📄 PDF Splitter Tool")

uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])

if uploaded_file:
    reader = PdfReader(uploaded_file)
    total_pages = len(reader.pages)
    st.success(f"Uploaded! Total Pages: {total_pages}")

    # Input range
    start_page = st.number_input("Start Page (1-based)", min_value=1, max_value=total_pages, value=1)
    end_page = st.number_input("End Page (inclusive)", min_value=1, max_value=total_pages, value=total_pages)

    if start_page > end_page:
        st.error("Start page must be less than or equal to end page.")

    if st.button("Split PDF"):
        writer = PdfWriter()
        for i in range(start_page - 1, end_page):
            writer.add_page(reader.pages[i])

        output_stream = io.BytesIO()
        writer.write(output_stream)
        output_stream.seek(0)

        st.success("✅ PDF split successfully!")
        st.download_button("Download Split PDF", data=output_stream, file_name="split.pdf", mime="application/pdf")
