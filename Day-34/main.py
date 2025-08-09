import streamlit as st
from pypdf import PdfReader, PdfWriter
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import io

def create_watermark(text, page_size=letter):
    packet = io.BytesIO()
    can = canvas.Canvas(packet, pagesize=page_size)
    can.setFont("Helvetica-Bold", 50)
    can.setFillColorRGB(0.5, 0.5, 0.5, alpha=0.3)
    can.saveState()
    can.translate(page_size[0] / 2, page_size[1] / 2)
    can.rotate(45)
    can.drawCentredString(0, 0, text)
    can.restoreState()
    can.save()
    packet.seek(0)
    return PdfReader(packet)

def add_watermark_to_pdf(input_pdf_bytes, watermark_text):
    pdf_reader = PdfReader(io.BytesIO(input_pdf_bytes))
    pdf_writer = PdfWriter()

    first_page = pdf_reader.pages[0]
    page_width = first_page.mediabox.width
    page_height = first_page.mediabox.height
    watermark_pdf = create_watermark(watermark_text, page_size=(page_width, page_height))
    watermark_page = watermark_pdf.pages[0]

    for page in pdf_reader.pages:
        page.merge_page(watermark_page)
        pdf_writer.add_page(page)

    output_stream = io.BytesIO()
    pdf_writer.write(output_stream)
    output_stream.seek(0)
    return output_stream

# Streamlit UI
st.title("PDF Watermarker")

uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])

watermark_text = st.text_input("Enter watermark text", value="CONFIDENTIAL")

if uploaded_file and watermark_text:
    if st.button("Add Watermark"):
        with st.spinner("Processing..."):
            result_pdf = add_watermark_to_pdf(uploaded_file.read(), watermark_text)
            st.success("Watermark added successfully!")
            st.download_button(
                label="Download Watermarked PDF",
                data=result_pdf,
                file_name="watermarked_output.pdf",
                mime="application/pdf",
            )
