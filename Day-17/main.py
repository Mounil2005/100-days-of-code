
import tkinter as tk
import random

# ASCII Art
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choices = [rock, paper, scissors]
choice_names = ["Rock", "Paper", "Scissors"]

# Main logic
def play(user_choice):
    computer_choice = random.randint(0, 2)
    
    user_label.config(text=f"You chose: {choice_names[user_choice]}\n{choices[user_choice]}")
    comp_label.config(text=f"Computer chose: {choice_names[computer_choice]}\n{choices[computer_choice]}")

    if user_choice == computer_choice:
        result.set("It's a Draw!")
        result_label.config(fg="#FFA500")  # Orange
    elif (user_choice == 0 and computer_choice == 2) or \
         (user_choice == 1 and computer_choice == 0) or \
         (user_choice == 2 and computer_choice == 1):
        result.set("You Win!")
        result_label.config(fg="#28a745")  # Green
    else:
        result.set("You Lose!")
        result_label.config(fg="#dc3545")  # Red

# Reset the game state
def restart_game():
    user_label.config(text="")
    comp_label.config(text="")
    result.set("Choose your move to begin!")
    result_label.config(fg="black")

# Setup window
root = tk.Tk()
root.title("Rock Paper Scissors Game")
root.geometry("750x700")
root.config(bg="#e0f7fa")  # Light cyan background

# Title
title_frame = tk.Frame(root, bg="#00acc1", pady=10)
title_frame.pack(fill="x")
tk.Label(title_frame, text="🤖 Rock Paper Scissors 🎮", font=("Helvetica", 24, "bold"), fg="white", bg="#00acc1").pack()

# Button Frame
button_frame = tk.Frame(root, bg="#e0f7fa")
button_frame.pack(pady=20)

btn_style = {"font": ("Arial", 14, "bold"), "width": 12, "padx": 10, "pady": 10}

tk.Button(button_frame, text="🪨 Rock", bg="#90caf9", command=lambda: play(0), **btn_style).grid(row=0, column=0, padx=10)
tk.Button(button_frame, text="📄 Paper", bg="#a5d6a7", command=lambda: play(1), **btn_style).grid(row=0, column=1, padx=10)
tk.Button(button_frame, text="✂️ Scissors", bg="#f48fb1", command=lambda: play(2), **btn_style).grid(row=0, column=2, padx=10)

# Player and computer choice display
user_label = tk.Label(root, text="", font=("Courier", 12), justify="left", bg="#e0f7fa")
user_label.pack(pady=10)

comp_label = tk.Label(root, text="", font=("Courier", 12), justify="left", bg="#e0f7fa")
comp_label.pack(pady=10)

# Result Display
result = tk.StringVar()
result.set("Choose your move to begin!")

result_label = tk.Label(root, textvariable=result, font=("Helvetica", 18, "bold"), bg="#e0f7fa")
result_label.pack(pady=20)

tk.Button(root, text="🔁 Restart", font=("Arial", 12, "bold"), bg="#ffcc80", fg="black", command=restart_game).pack(pady=10)


# Footer
tk.Label(root, text="Made with ❤️ using Python Tkinter", font=("Arial", 10), bg="#e0f7fa", fg="gray").pack(side="bottom", pady=10)

root.mainloop()
