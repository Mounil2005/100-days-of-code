# import streamlit as st
# from PyPDF2 import PdfMerger
# import io

# st.set_page_config(page_title="PDF Merger")

# st.title("🗃️ PDF Merger App")
# st.caption("Upload multiple PDF files and merge them into one 📄")

# uploaded_files = st.file_uploader("📤 Upload PDF files", type=["pdf"], accept_multiple_files=True)

# if uploaded_files:
#     st.write(f"✅ {len(uploaded_files)} file(s) uploaded.")
    
#     if st.button("🔗 Merge PDFs"):
#         merger = PdfMerger()

#         for pdf in uploaded_files:
#             merger.append(pdf)

#         # Output in memory
#         merged_pdf_bytes = io.BytesIO()
#         merger.write(merged_pdf_bytes)
#         merger.close()

#         st.success("🎉 PDFs merged successfully!")
        
#         st.download_button(
#             label="📥 Download Merged PDF",
#             data=merged_pdf_bytes.getvalue(),
#             file_name="merged_output.pdf",
#             mime="application/pdf"
#         )



# import streamlit as st
# from PyPDF2 import PdfMerger
# import io

# st.set_page_config(page_title="🗃️ PDF Merger with Reordering", page_icon="📄")

# st.title("🗃️ PDF Merger with Reordering")
# st.caption("Upload multiple PDFs, reorder them, and merge 📑")

# uploaded_files = st.file_uploader("📤 Upload PDF files", type=["pdf"], accept_multiple_files=True)

# if uploaded_files:
#     st.write(f"✅ {len(uploaded_files)} file(s) uploaded.")

#     st.subheader("📚 Reorder PDFs")

#     # Default order
#     file_names = [file.name for file in uploaded_files]

#     # Create sliders to define new order
#     order_indices = []
#     for i, file in enumerate(uploaded_files):
#         index = st.number_input(
#             f"Order for: `{file.name}`", 
#             min_value=1, 
#             max_value=len(uploaded_files), 
#             value=i + 1, 
#             key=f"order_{file.name}"
#         )
#         order_indices.append((index, file))

#     # Sort files based on selected order
#     ordered_files = [f for _, f in sorted(order_indices)]

#     if st.button("🔗 Merge PDFs"):
#         merger = PdfMerger()
#         for pdf in ordered_files:
#             merger.append(pdf)

#         merged_pdf_bytes = io.BytesIO()
#         merger.write(merged_pdf_bytes)
#         merger.close()

#         st.success("🎉 PDFs merged successfully!")
#         st.download_button(
#             label="📥 Download Merged PDF",
#             data=merged_pdf_bytes.getvalue(),
#             file_name="merged_output.pdf",
#             mime="application/pdf"
#         )


import streamlit as st
from streamlit_sortables import sort_items
from PyPDF2 import PdfMerger
import io

st.set_page_config(page_title="🗃️ PDF Merger ", page_icon="📄")
st.title("🗃️ PDF Merger")
st.caption("Upload PDFs, drag to reorder, and merge with ease 📑")

uploads = st.file_uploader("📤 Upload PDFs", type="pdf", accept_multiple_files=True)

if uploads:
    # Extract filenames
    file_names = [u.name for u in uploads]

    # Display sortable list
    st.subheader("🔀 Arrange Order (drag and drop):")
    ordered_names = sort_items(file_names)  # returns list in new order :contentReference[oaicite:1]{index=1}

    # Map back to file objects
    name_to_file = {u.name: u for u in uploads}
    ordered_files = [name_to_file[name] for name in ordered_names]

    if st.button("🔗 Merge PDFs"):
        merger = PdfMerger()
        for pdf in ordered_files:
            merger.append(pdf)
        merged = io.BytesIO(); merger.write(merged); merger.close()

        st.success("🎉 PDFs merged in your chosen order!")
        st.download_button(
            label="📥 Download Merged PDF",
            data=merged.getvalue(),
            file_name="merged.pdf",
            mime="application/pdf"
        )
