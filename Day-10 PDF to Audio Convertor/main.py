

import streamlit as st
from PyPDF2 import PdfReader
from gtts import gTTS
import io

st.set_page_config(page_title="📘 PDF to Audio Converter", page_icon="🔊")

st.title("📘 PDF to Audio Converter")
st.caption("Upload a PDF, select page range & language, and convert it to an MP3 🔊")

pdf_file = st.file_uploader("📤 Upload your PDF", type=["pdf"])

if pdf_file:
    reader = PdfReader(pdf_file)
    total_pages = len(reader.pages)

    st.success(f"✅ PDF Loaded: {total_pages} pages found.")

    # Feature 1: Page Range Selection
    st.subheader("🔢 Select Page Range to Convert")
    start_page = st.number_input("Start Page", min_value=1, max_value=total_pages, value=1)
    end_page = st.number_input("End Page", min_value=start_page, max_value=total_pages, value=total_pages)

    # Feature 2: Language Selection
    st.subheader("🌐 Choose Language for Audio")
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
            st.error("❌ Could not extract any readable text from the selected pages.")
        else:
            st.info("🔄 Generating audio... Please wait.")

            tts = gTTS(text, lang=lang_code)
            mp3_fp = io.BytesIO()
            tts.write_to_fp(mp3_fp)
            mp3_fp.seek(0)

            st.success("✅ Audio ready!")

            st.audio(mp3_fp, format="audio/mp3")

            st.download_button(
                label="📥 Download MP3",
                data=mp3_fp,
                file_name="converted_audio.mp3",
                mime="audio/mpeg"
            )
