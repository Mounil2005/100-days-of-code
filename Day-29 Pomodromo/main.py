import tkinter as tk
import math
import random
import os
import threading

# ---------------------------- CONSTANTS ------------------------------- #
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 15
reps = 0
timer = None
pomodoros_completed = 0

# ---------------------------- QUOTES ------------------------------- #
quotes = [
    "Stay focused. Stay determined.",
    "One Pomodoro at a time!",
    "You're doing great! Keep going.",
    "Small steps lead to big wins.",
    "Discipline beats motivation!",
    "Breaks help your brain reset."
]

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps, pomodoros_completed, timer
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="25:00")
    title_label.config(text="Timer", fg="black")
    checkmarks.config(text="")
    quote_label.config(text=random.choice(quotes))
    reps = 0
    pomodoros_completed = 0
    update_bg("white")


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        title_label.config(text="🌙 Long Break", fg="#4e9fff")
        update_bg("#cce5ff")
    elif reps % 2 == 0:
        count_down(short_break_sec)
        title_label.config(text="☕ Short Break", fg="#33cc99")
        update_bg("#d6fff5")
    else:
        count_down(work_sec)
        title_label.config(text="🍅 Work", fg="#e7305b")
        update_bg("#ffe5e0")

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    minutes = math.floor(count / 60)
    seconds = count % 60
    time_text = f"{minutes:02d}:{seconds:02d}"
    canvas.itemconfig(timer_text, text=time_text)
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        global pomodoros_completed
        if reps % 2 == 1:
            pomodoros_completed += 1
            checkmarks.config(text="✅" * pomodoros_completed)
        quote_label.config(text=random.choice(quotes))
        
        start_timer()

def manual_work():
    global reps
    window.after_cancel(timer)
    reps += 1
    title_label.config(text="🍅 Work", fg="#e7305b")
    update_bg("#ffe5e0")
    count_down(WORK_MIN * 60)

def manual_short():
    global timer
    window.after_cancel(timer)
    title_label.config(text="☕ Short Break", fg="#33cc99")
    update_bg("#d6fff5")
    count_down(SHORT_BREAK_MIN * 60)

def manual_long():
    global timer
    window.after_cancel(timer)
    title_label.config(text="🌙 Long Break", fg="#4e9fff")
    update_bg("#cce5ff")
    count_down(LONG_BREAK_MIN * 60)

# ---------------------------- UI SETUP ------------------------------- #
def update_bg(color):
    canvas.config(bg=color)
    window.config(bg=color)
    title_label.config(bg=color)
    quote_label.config(bg=color)
    checkmarks.config(bg=color)



# ---------------------------- TKINTER WINDOW ------------------------------- #
window = tk.Tk()
window.title("Pomodromo 🍅")
window.config(padx=100, pady=50, bg="white")

title_label = tk.Label(text="Pomodromo Timer", font=("Courier", 35, "bold"), fg="black", bg="white")
title_label.grid(column=1, row=0)

canvas = tk.Canvas(width=300, height=300, bg="white", highlightthickness=0)
# tomato_img = tk.PhotoImage(file="tomato.png")  # Optional: use any image

img_path = os.path.join(os.path.dirname(__file__), "tomato.png")
tomato_img = tk.PhotoImage(file=img_path)

canvas.create_image(150, 150, image=tomato_img)
timer_text = canvas.create_text(150, 180, text="25:00", fill="black", font=("Courier", 30, "bold"))
canvas.grid(column=1, row=1)

start_button = tk.Button(text="▶ Start", font=("Arial", 12, "bold"), bg="#a3f7bf", command=start_timer)
start_button.grid(column=0, row=2)

reset_button = tk.Button(text="🔄 Reset", font=("Arial", 12, "bold"), bg="#ffb3ba", command=reset_timer)
reset_button.grid(column=2, row=2)

manual_frame = tk.Frame(window, bg="white")
manual_frame.grid(column=1, row=5, pady=10)

btn_work = tk.Button(manual_frame, text="🍅 Work", command=manual_work, bg="#ffe0e0", font=("Arial", 10))
btn_short = tk.Button(manual_frame, text="☕ Short Break", command=manual_short, bg="#d0ffe7", font=("Arial", 10))
btn_long = tk.Button(manual_frame, text="🌙 Long Break", command=manual_long, bg="#dde9ff", font=("Arial", 10))

btn_work.grid(row=0, column=0, padx=5)
btn_short.grid(row=0, column=1, padx=5)
btn_long.grid(row=0, column=2, padx=5)


checkmarks = tk.Label(text="", fg="green", bg="white", font=("Arial", 14))
checkmarks.grid(column=1, row=3)

quote_label = tk.Label(text=random.choice(quotes), wraplength=250, font=("Arial", 12, "italic"), bg="white")
quote_label.grid(column=1, row=4, pady=20)

window.mainloop()
