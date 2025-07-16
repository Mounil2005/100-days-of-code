# 🔊 PDF to Audio Converter

🎯 **Day 10 of #100DaysOfCode**

This Streamlit web app allows users to upload any PDF file, choose specific pages, select a language, and convert the extracted text into an MP3 audio file using Google Text-to-Speech (`gTTS`).  
It’s useful for productivity, accessibility, language learning, or listening to your notes on the go!

---

## 🚀 Features

- 📤 Upload any PDF file
- 🔢 Select page range (e.g., pages 2–5)
- 🌐 Choose from multiple output languages:
  - English (`en`)
  - Hindi (`hi`) — requires Hindi text
  - Tamil (`ta`) — requires Tamil script
  - Bengali (`bn`) — requires Bengali script
- 🎙️ Convert extracted text to speech using `gTTS`
- 📥 Download the generated MP3 file
- 💡 Works fully in memory — no file is saved server-side

---

## 🛠 Tech Stack

| Tool          | Purpose                       |
|---------------|-------------------------------|
| `Streamlit`   | Frontend + web framework      |
| `PyPDF2`      | PDF reading + text extraction |
| `gTTS`        | Text-to-Speech conversion     |
| `io.BytesIO`  | In-memory audio streaming     |

