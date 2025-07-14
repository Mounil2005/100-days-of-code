# 📐 Image Resizer + Compressor Web App

**Day 8 of #100DaysOfCode**

An interactive web app built with **Streamlit** that lets you:
- Resize any JPG or PNG image
- Maintain or break aspect ratio
- Compress JPGs with adjustable quality
- Preview and download the resized image

---

## 🖼️ Features

- 📂 Upload JPG/PNG image
- 🔢 Resize by width (height auto-adjusts if aspect ratio is locked)
- 🔒 Aspect ratio toggle (lock/unlock)
- 📏 Display original and resized dimensions + file sizes
- 📦 Enable compression for JPGs with quality slider
- 👁️ Preview before download
- 📥 Download resized image instantly

---

## 🛠️ Tech Stack

| Tech        | Purpose                    |
|-------------|----------------------------|
| Streamlit   | Web UI framework           |
| Pillow (PIL)| Image resizing & handling  |
| io.BytesIO  | In-memory file processing  |

---

