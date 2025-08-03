import streamlit as st
from PyPDF2 import PdfReader, PdfWriter, PdfMerger
from gtts import gTTS
import io
from streamlit_sortables import sort_items

st.set_page_config(page_title="📚 PDF Toolbox", layout="centered", page_icon="📁")

st.title("📚 PDF Toolbox")
st.caption("Split, Merge, and Convert PDFs to Audio — all in one place!")

# Sidebar navigation
tool = st.sidebar.radio(
    "Choose a Tool:",
    ["🔪 Split PDF", "🗃️ Merge PDFs", "🎧 PDF to Audio"]
)

# 1. PDF Splitter
if tool == "🔪 Split PDF":
    st.header("🔪 Split PDF")
    uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])
    
    if uploaded_file:
        reader = PdfReader(uploaded_file)
        total_pages = len(reader.pages)
        st.success(f"✅ Uploaded! Total Pages: {total_pages}")

        start_page = st.number_input("Start Page (1-based)", min_value=1, max_value=total_pages, value=1)
        end_page = st.number_input("End Page (inclusive)", min_value=1, max_value=total_pages, value=total_pages)

        if start_page > end_page:
            st.error("❌ Start page must be less than or equal to end page.")
        elif st.button("✂️ Split PDF"):
            writer = PdfWriter()
            for i in range(start_page - 1, end_page):
                writer.add_page(reader.pages[i])
            output = io.BytesIO()
            writer.write(output)
            output.seek(0)
            st.success("✅ PDF split successfully!")
            st.download_button("📥 Download Split PDF", output, file_name="split.pdf", mime="application/pdf")

# 2. PDF Merger
elif tool == "🗃️ Merge PDFs":
    st.header("🗃️ Merge PDFs")
    uploads = st.file_uploader("📤 Upload PDFs", type="pdf", accept_multiple_files=True)

    if uploads:
        file_names = [u.name for u in uploads]
        st.subheader("🔀 Arrange Order (drag and drop):")
        ordered_names = sort_items(file_names)
        name_to_file = {u.name: u for u in uploads}
        ordered_files = [name_to_file[name] for name in ordered_names]

        if st.button("🔗 Merge PDFs"):
            merger = PdfMerger()
            for pdf in ordered_files:
                merger.append(pdf)
            merged = io.BytesIO(); merger.write(merged); merger.close()

            st.success("🎉 PDFs merged successfully!")
            st.download_button("📥 Download Merged PDF", merged.getvalue(), file_name="merged.pdf", mime="application/pdf")

# 3. PDF to Audio
elif tool == "🎧 PDF to Audio":
    st.header("🎧 PDF to Audio Converter")
    pdf_file = st.file_uploader("📤 Upload your PDF", type=["pdf"])
    
    if pdf_file:
        reader = PdfReader(pdf_file)
        total_pages = len(reader.pages)
        st.success(f"✅ PDF Loaded: {total_pages} pages found.")

        st.subheader("🔢 Select Page Range")
        start_page = st.number_input("Start Page", min_value=1, max_value=total_pages, value=1)
        end_page = st.number_input("End Page", min_value=start_page, max_value=total_pages, value=total_pages)

        st.subheader("🌐 Choose Language")
        language = st.selectbox("Select language", [
            ("English", "en"),
            ("French", "fr"),
            ("German", "de"),
            ("Spanish", "es")
        ])
        lang_code = language[1]

        if st.button("🎙️ Convert to Audio"):
            text = ""
            for i in range(start_page - 1, end_page):
                page = reader.pages[i]
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"

            if not text.strip():
                st.error("❌ No readable text found in selected pages.")
            else:
                st.info("🔄 Generating audio...")
                tts = gTTS(text, lang=lang_code)
                mp3_fp = io.BytesIO()
                tts.write_to_fp(mp3_fp)
                mp3_fp.seek(0)
                st.success("✅ Audio ready!")

                st.audio(mp3_fp, format="audio/mp3")
                st.download_button("📥 Download MP3", data=mp3_fp, file_name="converted_audio.mp3", mime="audio/mpeg")
