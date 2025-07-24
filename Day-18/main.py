# import tkinter as tk
# import time
# import random

# # Sample quotes
# quotes = [
#     "The quick brown fox jumps over the lazy dog",
#     "Typing is a fundamental skill for productivity",
#     "Practice makes perfect in everything we do",
#     "Python is a great language for beginners",
#     "Discipline is the bridge between goals and success"
# ]

# # Global start time
# start_time = None

# def start_typing(event):
#     global start_time
#     if start_time is None:
#         start_time = time.time()

# def calculate_result():
#     global start_time

#     end_time = time.time()
#     total_time = end_time - start_time

#     typed_text = input_text.get("1.0", tk.END).strip()
#     original_text = quote_label.cget("text")

#     # Calculate WPM
#     total_words = len(typed_text.split())
#     wpm = (total_words / total_time) * 60

#     # Calculate Accuracy
#     correct_chars = 0
#     for i in range(min(len(typed_text), len(original_text))):
#         if typed_text[i] == original_text[i]:
#             correct_chars += 1
#     accuracy = (correct_chars / len(original_text)) * 100

#     result_label.config(
#         text=f"WPM: {wpm:.2f}   Accuracy: {accuracy:.2f}%",
#         fg="blue"
#     )

# def reset_test():
#     global start_time
#     start_time = None
#     quote = random.choice(quotes)
#     quote_label.config(text=quote)
#     input_text.delete("1.0", tk.END)
#     result_label.config(text="")

# # GUI Setup
# root = tk.Tk()
# root.title("Typing Speed Tester")
# root.geometry("700x400")
# root.config(padx=20, pady=20, bg="#f4f1ee")

# # Quote Display
# quote_label = tk.Label(root, text=random.choice(quotes), font=("Helvetica", 16), wraplength=600, bg="#f4f1ee")
# quote_label.pack(pady=20)

# # Input Box
# input_text = tk.Text(root, height=6, width=80, font=("Helvetica", 14))
# input_text.pack()
# input_text.bind("<KeyPress>", start_typing)

# # Buttons
# btn_frame = tk.Frame(root, bg="#f4f1ee")
# btn_frame.pack(pady=10)

# submit_btn = tk.Button(btn_frame, text="Check Result", command=calculate_result, bg="#98c1d9", font=("Helvetica", 12))
# submit_btn.pack(side="left", padx=10)

# reset_btn = tk.Button(btn_frame, text="Try Again", command=reset_test, bg="#ee6c4d", font=("Helvetica", 12))
# reset_btn.pack(side="left", padx=10)

# # Result Label
# result_label = tk.Label(root, text="", font=("Helvetica", 14), bg="#f4f1ee")
# result_label.pack(pady=20)

# root.mainloop()


# import tkinter as tk
# from tkinter import scrolledtext
# import time
# import random

# # Sample quotes
# quotes = [
#     "The quick brown fox jumps over the lazy dog.",
#     "Typing is a fundamental skill for productivity.",
#     "Practice makes perfect in everything we do.",
#     "Python is a great language for beginners.",
#     "Discipline is the bridge between goals and success.",
#     "Simplicity is the soul of efficiency.",
#     "Artificial intelligence is the new electricity."
# ]

# # Globals
# start_time = None
# timer_running = False

# def start_typing(event):
#     global start_time, timer_running
#     if not timer_running:
#         start_time = time.time()
#         timer_running = True
#         update_timer()

# def update_timer():
#     if timer_running:
#         elapsed = int(time.time() - start_time)
#         timer_label.config(text=f"⏱ Time: {elapsed} sec")
#         root.after(1000, update_timer)

# def calculate_result():
#     global timer_running
#     timer_running = False
#     end_time = time.time()
#     total_time = end_time - start_time

#     typed_text = input_text.get("1.0", tk.END).strip()
#     original_text = quote_label.cget("text")

#     # Calculate WPM
#     total_words = len(typed_text.split())
#     wpm = (total_words / total_time) * 60 if total_time > 0 else 0

#     # Accuracy
#     correct_chars = sum(1 for i in range(min(len(typed_text), len(original_text))) if typed_text[i] == original_text[i])
#     accuracy = (correct_chars / len(original_text)) * 100 if len(original_text) > 0 else 0

#     result_label.config(
#         text=f"🏁 WPM: {wpm:.2f}   🎯 Accuracy: {accuracy:.2f}%",
#         fg="#003049"
#     )

# def reset_test():
#     global start_time, timer_running
#     start_time = None
#     timer_running = False
#     quote = random.choice(quotes)
#     quote_label.config(text=quote)
#     input_text.delete("1.0", tk.END)
#     result_label.config(text="")
#     timer_label.config(text="⏱ Time: 0 sec")

# # GUI Setup
# root = tk.Tk()
# root.title("Typing Speed Tester")
# root.geometry("800x500")
# root.config(bg="#f1faee")

# # Fonts & Colors
# main_font = ("Segoe UI", 14)
# heading_font = ("Segoe UI", 20, "bold")

# # Title
# title_label = tk.Label(root, text="🖋 Typing Speed Tester", font=heading_font, bg="#f1faee", fg="#1d3557")
# title_label.pack(pady=10)

# # Quote Display (scrollable if long)
# quote_frame = tk.Frame(root, bg="#f1faee")
# quote_frame.pack(pady=5)

# quote_scroll = scrolledtext.ScrolledText(quote_frame, height=4, wrap=tk.WORD, font=main_font, bg="#e0fbfc", relief="flat", bd=2)
# quote_scroll.pack()
# quote = random.choice(quotes)
# quote_scroll.insert(tk.END, quote)
# quote_scroll.config(state='disabled')
# quote_label = tk.Label(root, text=quote, font=main_font, wraplength=750, bg="#f1faee", fg="#2a2a2a")
# quote_label.pack(pady=5)

# # Input Text Box
# input_text = tk.Text(root, height=6, width=90, font=main_font, wrap=tk.WORD, bg="#ffffff", relief="groove")
# input_text.pack(pady=10)
# input_text.bind("<KeyPress>", start_typing)

# # Timer + Result
# timer_label = tk.Label(root, text="⏱ Time: 0 sec", font=("Segoe UI", 12), bg="#f1faee", fg="#264653")
# timer_label.pack()

# result_label = tk.Label(root, text="", font=("Segoe UI", 14), bg="#f1faee")
# result_label.pack(pady=10)

# # Buttons
# btn_frame = tk.Frame(root, bg="#f1faee")
# btn_frame.pack(pady=10)

# submit_btn = tk.Button(btn_frame, text="✅ Submit", command=calculate_result, bg="#90be6d", fg="white", font=("Segoe UI", 12), padx=20)
# submit_btn.pack(side="left", padx=10)

# reset_btn = tk.Button(btn_frame, text="🔄 Try Again", command=reset_test, bg="#f28482", fg="white", font=("Segoe UI", 12), padx=20)
# reset_btn.pack(side="left", padx=10)

# root.mainloop()



# import tkinter as tk
# from tkinter import scrolledtext
# import random
# import time

# quotes = [
#     "The quick brown fox jumps over the lazy dog.",
#     "Discipline is the bridge between goals and success.",
#     "Typing is a fundamental skill for productivity and speed.",
#     "Python is a great language for developing applications rapidly.",
#     "Simplicity is the soul of efficiency in design and development."
# ]

# start_time = None
# timer_running = False

# def start_timer(event):
#     global start_time, timer_running
#     if not timer_running:
#         start_time = time.time()
#         timer_running = True
#         update_timer()

# def update_timer():
#     if timer_running:
#         elapsed = int(time.time() - start_time)
#         timer_label.config(text=f"⏱ Time: {elapsed}s")
#         root.after(1000, update_timer)

# def update_highlight(event=None):
#     typed = input_text.get("1.0", tk.END).strip()
#     original = quote_text.get("1.0", tk.END).strip()

#     quote_text.tag_remove("correct", "1.0", tk.END)
#     quote_text.tag_remove("incorrect", "1.0", tk.END)

#     for i in range(len(typed)):
#         if i >= len(original):
#             break
#         tag = "correct" if typed[i] == original[i] else "incorrect"
#         quote_text.tag_add(tag, f"1.{i}", f"1.{i+1}")
#         quote_text.see(f"1.{i+1}")  # auto scroll to next char

# def calculate_result():
#     global timer_running
#     timer_running = False
#     end_time = time.time()
#     total_time = end_time - start_time

#     typed_text = input_text.get("1.0", tk.END).strip()
#     original_text = quote_text.get("1.0", tk.END).strip()

#     total_words = len(typed_text.split())
#     wpm = (total_words / total_time) * 60 if total_time > 0 else 0

#     correct_chars = sum(1 for i in range(min(len(typed_text), len(original_text))) if typed_text[i] == original_text[i])
#     accuracy = (correct_chars / len(original_text)) * 100 if len(original_text) > 0 else 0

#     result_label.config(text=f"🏁 WPM: {wpm:.2f}   🎯 Accuracy: {accuracy:.2f}%")

# def reset_test():
#     global start_time, timer_running
#     start_time = None
#     timer_running = False
#     new_quote = random.choice(quotes)

#     quote_text.config(state="normal")
#     quote_text.delete("1.0", tk.END)
#     quote_text.insert(tk.END, new_quote)
#     quote_text.config(state="disabled")

#     input_text.delete("1.0", tk.END)
#     result_label.config(text="")
#     timer_label.config(text="⏱ Time: 0s")

# # Main GUI
# root = tk.Tk()
# root.title("Typing Speed Tester")
# root.geometry("850x500")
# root.config(bg="#f7f5f2")

# title = tk.Label(root, text="⌨️ Typing Speed Tester", font=("Segoe UI", 20, "bold"), bg="#f7f5f2", fg="#1d3557")
# title.pack(pady=10)

# # Scrollable Quote Area
# quote_frame = tk.Frame(root, bg="#f7f5f2")
# quote_frame.pack(pady=5)

# quote_text = scrolledtext.ScrolledText(quote_frame, wrap=tk.WORD, height=5, font=("Consolas", 14), bg="#f0efeb", relief="flat")
# quote_text.pack()
# quote_text.insert(tk.END, random.choice(quotes))
# quote_text.config(state="disabled")

# # Text highlight tags
# quote_text.tag_config("correct", foreground="green")
# quote_text.tag_config("incorrect", foreground="red")

# # Input
# input_text = tk.Text(root, height=6, width=100, font=("Consolas", 14), wrap=tk.WORD, relief="ridge", bd=2)
# input_text.pack(pady=10)
# input_text.bind("<KeyPress>", start_timer)
# input_text.bind("<KeyRelease>", update_highlight)

# # Timer & Result
# timer_label = tk.Label(root, text="⏱ Time: 0s", font=("Segoe UI", 12), bg="#f7f5f2", fg="#6c757d")
# timer_label.pack()

# result_label = tk.Label(root, text="", font=("Segoe UI", 14), bg="#f7f5f2")
# result_label.pack(pady=10)

# # Buttons
# btn_frame = tk.Frame(root, bg="#f7f5f2")
# btn_frame.pack()

# submit_btn = tk.Button(btn_frame, text="✅ Submit", command=calculate_result, bg="#06d6a0", fg="white", font=("Segoe UI", 12), padx=15)
# submit_btn.pack(side="left", padx=10)

# reset_btn = tk.Button(btn_frame, text="🔄 Reset", command=reset_test, bg="#ef476f", fg="white", font=("Segoe UI", 12), padx=15)
# reset_btn.pack(side="left", padx=10)

# root.mainloop()


# import tkinter as tk
# from tkinter import scrolledtext
# import random
# import time

# # List of quotes (can expand)
# quotes = [
#     "The quick brown fox jumps over the lazy dog.",
#     "Discipline is the bridge between goals and success.",
#     "Typing is a fundamental skill for productivity and speed.",
#     "Python is a great language for developing applications rapidly.",
#     "Simplicity is the soul of efficiency in design and development.",
#     "Artificial intelligence is the new electricity in the world of tech.",
#     "Logic will get you from A to B. Imagination will take you everywhere.",
#     "Success is not final, failure is not fatal: It is the courage to continue that counts.",
#     "Hard work beats talent when talent doesn’t work hard.",
#     "You miss 100% of the shots you don’t take.",
#     "Whether you think you can or you think you can’t, you’re right.",
#     "Creativity is intelligence having fun.",
#     "Great things never come from comfort zones."
# ]

# # Globals
# start_time = None
# timer_running = False

# def generate_long_quote():
#     return " ".join(random.sample(quotes, 5))  # 5 random sentences

# def start_timer(event):
#     global start_time, timer_running
#     if not timer_running:
#         start_time = time.time()
#         timer_running = True
#         update_timer()

# def update_timer():
#     if timer_running:
#         elapsed = int(time.time() - start_time)
#         timer_label.config(text=f"⏱ Time: {elapsed}s")
#         update_live_stats()
#         root.after(1000, update_timer)

# def update_highlight(event=None):
#     typed = input_text.get("1.0", tk.END).strip()
#     original = quote_text.get("1.0", tk.END).strip()

#     quote_text.tag_remove("correct", "1.0", tk.END)
#     quote_text.tag_remove("incorrect", "1.0", tk.END)

#     for i in range(len(typed)):
#         if i >= len(original):
#             break
#         tag = "correct" if typed[i] == original[i] else "incorrect"
#         quote_text.tag_add(tag, f"1.{i}", f"1.{i+1}")
#         quote_text.see(f"1.{i+1}")

# def update_live_stats():
#     if not timer_running:
#         return
#     typed = input_text.get("1.0", tk.END).strip()
#     original = quote_text.get("1.0", tk.END).strip()

#     elapsed_time = time.time() - start_time
#     total_words = len(typed.split())
#     wpm = (total_words / elapsed_time) * 60 if elapsed_time > 0 else 0

#     correct_chars = sum(1 for i in range(min(len(typed), len(original))) if typed[i] == original[i])
#     accuracy = (correct_chars / len(original)) * 100 if len(original) > 0 else 0

#     live_stats_label.config(text=f"📈 WPM: {wpm:.2f}   🎯 Accuracy: {accuracy:.2f}%")

# def calculate_result():
#     global timer_running
#     timer_running = False
#     update_live_stats()

# def reset_test():
#     global start_time, timer_running
#     start_time = None
#     timer_running = False

#     new_quote = generate_long_quote()
#     quote_text.config(state="normal")
#     quote_text.delete("1.0", tk.END)
#     quote_text.insert(tk.END, new_quote)
#     quote_text.config(state="disabled")

#     input_text.delete("1.0", tk.END)
#     result_label.config(text="")
#     live_stats_label.config(text="")
#     timer_label.config(text="⏱ Time: 0s")

# # --- GUI Setup ---
# root = tk.Tk()
# root.title("Typing Speed Tester")
# root.geometry("900x600")
# root.config(bg="#f5f5f5")

# title = tk.Label(root, text="⌨️ Typing Speed Tester", font=("Segoe UI", 20, "bold"), bg="#f5f5f5", fg="#1d3557")
# title.pack(pady=10)

# # Scrollable Quote Display
# quote_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, height=7, font=("Consolas", 14), bg="#f0efeb", relief="flat")
# quote_text.pack(padx=20, pady=10)
# quote_text.insert(tk.END, generate_long_quote())
# quote_text.config(state="disabled")

# # Highlight tags
# quote_text.tag_config("correct", foreground="green")
# quote_text.tag_config("incorrect", foreground="red")

# # Input Area
# input_text = tk.Text(root, height=8, width=100, font=("Consolas", 14), wrap=tk.WORD, relief="ridge", bd=2)
# input_text.pack(pady=10)
# input_text.bind("<KeyPress>", start_timer)
# input_text.bind("<KeyRelease>", update_highlight)

# # Timer + Real-Time Stats
# timer_label = tk.Label(root, text="⏱ Time: 0s", font=("Segoe UI", 12), bg="#f5f5f5", fg="#6c757d")
# timer_label.pack()

# live_stats_label = tk.Label(root, text="", font=("Segoe UI", 13), bg="#f5f5f5", fg="#2a2a2a")
# live_stats_label.pack(pady=5)

# # Final Result (after Submit)
# result_label = tk.Label(root, text="", font=("Segoe UI", 14), bg="#f5f5f5")
# result_label.pack(pady=5)

# # Buttons
# btn_frame = tk.Frame(root, bg="#f5f5f5")
# btn_frame.pack(pady=10)

# submit_btn = tk.Button(btn_frame, text="✅ Submit", command=calculate_result, bg="#06d6a0", fg="white", font=("Segoe UI", 12), padx=15)
# submit_btn.pack(side="left", padx=10)

# reset_btn = tk.Button(btn_frame, text="🔄 Reset", command=reset_test, bg="#ef476f", fg="white", font=("Segoe UI", 12), padx=15)
# reset_btn.pack(side="left", padx=10)

# root.mainloop()


import tkinter as tk
from tkinter import scrolledtext
import random
import time

quotes = [
    "The quick brown fox jumps over the lazy dog.",
    "Discipline is the bridge between goals and success.",
    "Typing is a fundamental skill for productivity and speed.",
    "Python is a great language for developing applications rapidly.",
    "Simplicity is the soul of efficiency in design and development.",
    "Artificial intelligence is the new electricity in the world of tech.",
    "Logic will get you from A to B. Imagination will take you everywhere.",
    "Success is not final, failure is not fatal: It is the courage to continue that counts.",
    "Hard work beats talent when talent doesn’t work hard.",
    "You miss 100% of the shots you don’t take.",
    "Whether you think you can or you think you can’t, you’re right.",
    "Creativity is intelligence having fun.",
    "Great things never come from comfort zones."
]

start_time = None
timer_running = False
selected_duration = 60  # default

def generate_long_quote():
    return " ".join(random.sample(quotes, 5))

def start_timer(event):
    global start_time, timer_running
    if not timer_running:
        start_time = time.time()
        timer_running = True
        countdown(selected_duration)

def countdown(seconds_left):
    global timer_running
    if seconds_left >= 0 and timer_running:
        timer_label.config(text=f"⏱ Time Left: {seconds_left}s")
        update_live_stats()
        root.after(1000, lambda: countdown(seconds_left - 1))
    else:
        timer_running = False
        input_text.config(state="disabled")
        update_live_stats()
        result_label.config(text="⏰ Time's up! Final stats below.")

def update_highlight(event=None):
    typed = input_text.get("1.0", tk.END).strip()
    original = quote_text.get("1.0", tk.END).strip()

    quote_text.tag_remove("correct", "1.0", tk.END)
    quote_text.tag_remove("incorrect", "1.0", tk.END)

    for i in range(len(typed)):
        if i >= len(original):
            break
        tag = "correct" if typed[i] == original[i] else "incorrect"
        quote_text.tag_add(tag, f"1.{i}", f"1.{i+1}")
        quote_text.see(f"1.{i+1}")

def update_live_stats():
    if not timer_running and start_time is None:
        return
    typed = input_text.get("1.0", tk.END).strip()
    original = quote_text.get("1.0", tk.END).strip()

    elapsed_time = time.time() - start_time if start_time else 1
    total_words = len(typed.split())
    wpm = (total_words / elapsed_time) * 60 if elapsed_time > 0 else 0

    correct_chars = sum(1 for i in range(min(len(typed), len(original))) if typed[i] == original[i])
    accuracy = (correct_chars / len(original)) * 100 if len(original) > 0 else 0

    live_stats_label.config(text=f"📈 WPM: {wpm:.2f}   🎯 Accuracy: {accuracy:.2f}%")

def calculate_result():
    global timer_running
    timer_running = False
    input_text.config(state="disabled")
    update_live_stats()
    result_label.config(text="✅ Test submitted!")

def reset_test():
    global start_time, timer_running
    start_time = None
    timer_running = False

    quote_text.config(state="normal")
    quote_text.delete("1.0", tk.END)
    quote_text.insert(tk.END, generate_long_quote())
    quote_text.config(state="disabled")

    input_text.config(state="normal")
    input_text.delete("1.0", tk.END)
    result_label.config(text="")
    live_stats_label.config(text="")
    timer_label.config(text="⏱ Time Left: 0s")

def set_duration():
    global selected_duration
    selected_duration = int(duration_var.get())

# --- GUI Setup ---
root = tk.Tk()
root.title("Typing Speed Tester with Custom Timer")
root.geometry("900x650")
root.config(bg="#f5f5f5")

title = tk.Label(root, text="⌨️ Typing Speed Tester", font=("Segoe UI", 20, "bold"), bg="#f5f5f5", fg="#1d3557")
title.pack(pady=10)

# Duration selector
duration_var = tk.StringVar(value="60")
duration_frame = tk.Frame(root, bg="#f5f5f5")
duration_frame.pack()

tk.Label(duration_frame, text="⏳ Select Duration:", font=("Segoe UI", 12), bg="#f5f5f5").pack(side="left", padx=5)
tk.Radiobutton(duration_frame, text="15s", variable=duration_var, value="15", bg="#f5f5f5", command=set_duration).pack(side="left")
tk.Radiobutton(duration_frame, text="30s", variable=duration_var, value="30", bg="#f5f5f5", command=set_duration).pack(side="left")
tk.Radiobutton(duration_frame, text="60s", variable=duration_var, value="60", bg="#f5f5f5", command=set_duration).pack(side="left")

# Scrollable Quote Display
quote_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, height=7, font=("Consolas", 14), bg="#f0efeb", relief="flat")
quote_text.pack(padx=20, pady=10)
quote_text.insert(tk.END, generate_long_quote())
quote_text.config(state="disabled")

# Highlight tags
quote_text.tag_config("correct", foreground="green")
quote_text.tag_config("incorrect", foreground="red")

# Input Text Box
input_text = tk.Text(root, height=8, width=100, font=("Consolas", 14), wrap=tk.WORD, relief="ridge", bd=2)
input_text.pack(pady=10)
input_text.bind("<KeyPress>", start_timer)
input_text.bind("<KeyRelease>", update_highlight)

# Timer & Stats
timer_label = tk.Label(root, text="⏱ Time Left: 0s", font=("Segoe UI", 12), bg="#f5f5f5", fg="#6c757d")
timer_label.pack()

live_stats_label = tk.Label(root, text="", font=("Segoe UI", 13), bg="#f5f5f5", fg="#2a2a2a")
live_stats_label.pack(pady=5)

result_label = tk.Label(root, text="", font=("Segoe UI", 14), bg="#f5f5f5")
result_label.pack(pady=5)

# Buttons
btn_frame = tk.Frame(root, bg="#f5f5f5")
btn_frame.pack(pady=10)

submit_btn = tk.Button(btn_frame, text="✅ Submit Early", command=calculate_result, bg="#06d6a0", fg="white", font=("Segoe UI", 12), padx=15)
submit_btn.pack(side="left", padx=10)

reset_btn = tk.Button(btn_frame, text="🔄 Reset", command=reset_test, bg="#ef476f", fg="white", font=("Segoe UI", 12), padx=15)
reset_btn.pack(side="left", padx=10)

root.mainloop()
