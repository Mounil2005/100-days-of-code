import tkinter as tk
from time import strftime
from datetime import date

# Function to update time
def time():
    string = strftime('%H:%M:%S')   # 24-hour format
    lbl_time.config(text=string)
    lbl_time.after(1000, time)      # refresh every 1 sec

# Function to update date
def show_date():
    today = date.today().strftime("%A, %d %B %Y")  # Example: Friday, 22 August 2025
    lbl_date.config(text=today)

# Main window
root = tk.Tk()
root.title("Digital Clock")
root.geometry("500x250")
root.configure(bg="#1e1e2e")  # Dark background

# Time Label
lbl_time = tk.Label(root, font=("Helvetica", 50, "bold"), bg="#1e1e2e", fg="#00FFAB")
lbl_time.pack(pady=20)

# Date Label
lbl_date = tk.Label(root, font=("Helvetica", 20), bg="#1e1e2e", fg="#FFD700")
lbl_date.pack()

# Initialize
time()
show_date()

root.mainloop()
