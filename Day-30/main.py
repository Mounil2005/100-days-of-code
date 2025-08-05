import tkinter as tk
from tkinter import messagebox, font


questions = [
    {
        "question": "🧮 What is the output of print(2**3)?",
        "options": ["6", "8", "9", "4"],
        "answer": "8"
    },
    {
        "question": "🧠 Which of the following is a mutable data type?",
        "options": ["tuple", "int", "list", "str"],
        "answer": "list"
    },
    {
        "question": "📏 What does 'len()' function do?",
        "options": ["Adds numbers", "Finds length", "Counts characters only", "None"],
        "answer": "Finds length"
    },
    {
        "question": "⚙️ Which keyword is used to define a function in Python?",
        "options": ["func", "define", "def", "function"],
        "answer": "def"
    },
    {
        "question": "📄 What is the file extension for Python files?",
        "options": [".txt", ".java", ".py", ".exe"],
        "answer": ".py"
    }
]


score = 0
q_index = 0
option_buttons = []


def load_question():
    global q_index
    question_label.config(text=questions[q_index]["question"])
    for i in range(4):
        option_buttons[i].config(text=questions[q_index]["options"][i], bg="#f0f0f0", state="normal")

def check_answer(index):
    global score, q_index
    selected = option_buttons[index].cget("text")
    correct = questions[q_index]["answer"]

    for btn in option_buttons:
        btn.config(state="disabled")

    if selected == correct:
        option_buttons[index].config(bg="#a8e6cf")  # green
        score += 1
    else:
        option_buttons[index].config(bg="#ff8b94")  # red
        for i, opt in enumerate(questions[q_index]['options']):
            if opt == correct:
                option_buttons[i].config(bg="#a8e6cf")

    root.after(1000, next_question)

def next_question():
    global q_index
    q_index += 1
    if q_index < len(questions):
        load_question()
    else:
        show_score()

def show_score():
    messagebox.showinfo("🎉 Quiz Completed", f"You scored {score} out of {len(questions)} 🎓")
    root.destroy()


root = tk.Tk()
root.title("Quiz Generator")
root.geometry("700x500")
root.config(bg="#e0f7fa")


app_font = font.Font(family="Segoe UI", size=14, weight="bold")


title = tk.Label(
    root, text="Quiz Generator",
    font=("Helvetica", 22, "bold"), bg="#e0f7fa", fg="#00796b"
)
title.pack(pady=20)


question_label = tk.Label(
    root, text="", font=("Segoe UI", 16),
    bg="#ffffff", fg="#333", wraplength=600, justify="center", relief="solid", bd=2, padx=10, pady=15
)
question_label.pack(pady=20)


btn_frame = tk.Frame(root, bg="#e0f7fa")
btn_frame.pack()

button_colors = ["#ffffff"] * 4

for i in range(4):
    btn = tk.Button(
        btn_frame,
        text="",
        font=app_font,
        bg=button_colors[i],
        fg="#333333",
        activebackground="#b2ebf2",
        relief="ridge",
        bd=3,
        padx=10,
        pady=10,
        width=30,
        cursor="hand2",
        command=lambda i=i: check_answer(i)
    )
    btn.pack(pady=10)
    option_buttons.append(btn)


load_question()
root.mainloop()
