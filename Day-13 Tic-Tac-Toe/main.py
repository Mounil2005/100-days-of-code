# import tkinter as tk
# from tkinter import messagebox
# import random

# root = tk.Tk()
# root.title("❌⭕ Tic-Tac-Toe Game")
# root.geometry("320x400")
# root.configure(bg="#F0F4F8")

# # Game state
# current_player = "X"
# board = [""] * 9
# single_player = False

# # Fonts & Colors
# font = ("Arial", 20)
# btn_bg = "#BBDEFB"
# btn_active_bg = "#90CAF9"
# turn_bg = "#E3F2FD"
# win_color = "#81C784"

# # Player turn label
# turn_label = tk.Label(root, text="", font=("Arial", 16, "bold"),
#                       bg=turn_bg, fg="black", pady=10)
# turn_label.pack(fill="x")

# frame = tk.Frame(root, bg="#F0F4F8")
# frame.pack()

# def check_winner():
#     win_patterns = [
#         (0,1,2), (3,4,5), (6,7,8),
#         (0,3,6), (1,4,7), (2,5,8),
#         (0,4,8), (2,4,6)
#     ]
#     for i, j, k in win_patterns:
#         if board[i] == board[j] == board[k] != "":
#             return board[i]
#     if "" not in board:
#         return "Draw"
#     return None

# def on_click(i):
#     global current_player
#     if board[i] == "":
#         board[i] = current_player
#         buttons[i].config(text=current_player, state="disabled")
#         winner = check_winner()
#         if winner:
#             show_result(winner)
#         else:
#             if single_player:
#                 current_player = "O"
#                 turn_label.config(text="Computer's Turn")
#                 root.after(500, computer_move)
#             else:
#                 current_player = "O" if current_player == "X" else "X"
#                 turn_label.config(text=f"Player {current_player}'s Turn")

# def computer_move():
#     global current_player
#     available = [i for i, val in enumerate(board) if val == ""]
#     if available:
#         move = random.choice(available)
#         board[move] = "O"
#         buttons[move].config(text="O", state="disabled")
#         winner = check_winner()
#         if winner:
#             show_result(winner)
#         else:
#             current_player = "X"
#             turn_label.config(text="Player X's Turn")

# def show_result(winner):
#     if winner == "Draw":
#         messagebox.showinfo("Result", "It's a draw!")
#     else:
#         messagebox.showinfo("Result", f"{winner} wins!")
#         highlight_winner(winner)
#     disable_all_buttons()

# def highlight_winner(winner):
#     for i, j, k in [(0,1,2), (3,4,5), (6,7,8),
#                     (0,3,6), (1,4,7), (2,5,8),
#                     (0,4,8), (2,4,6)]:
#         if board[i] == board[j] == board[k] == winner:
#             buttons[i].config(bg=win_color)
#             buttons[j].config(bg=win_color)
#             buttons[k].config(bg=win_color)

# def disable_all_buttons():
#     for btn in buttons:
#         btn.config(state="disabled")

# def reset_game():
#     global board, current_player
#     board = [""] * 9
#     current_player = "X"
#     for btn in buttons:
#         btn.config(text="", state="normal", bg=btn_bg)
#     if single_player:
#         turn_label.config(text="Player X's Turn")
#     else:
#         turn_label.config(text="Player X's Turn")

# def set_mode(mode):
#     global single_player
#     single_player = (mode == "single")
#     mode_popup.destroy()
#     reset_game()

# # Game buttons
# buttons = []
# for i in range(9):
#     btn = tk.Button(frame, text="", font=font, width=5, height=2,
#                     bg=btn_bg, activebackground=btn_active_bg,
#                     command=lambda i=i: on_click(i))
#     btn.grid(row=i//3, column=i%3, padx=5, pady=5)
#     buttons.append(btn)

# # Restart Button
# tk.Button(root, text="🔁 Restart Game", font=("Arial", 12),
#           bg="#FFCDD2", fg="black", command=reset_game).pack(pady=10)

# # Mode selection popup
# mode_popup = tk.Toplevel(root)
# mode_popup.title("Choose Mode")
# mode_popup.geometry("300x150")
# tk.Label(mode_popup, text="Select Game Mode:", font=("Arial", 14)).pack(pady=10)

# tk.Button(mode_popup, text="🎮 Single Player (vs AI)", font=("Arial", 12),
#           command=lambda: set_mode("single")).pack(pady=5)

# tk.Button(mode_popup, text="👥 Two Player", font=("Arial", 12),
#           command=lambda: set_mode("multi")).pack(pady=5)

# mode_popup.transient(root)
# mode_popup.grab_set()
# root.wait_window(mode_popup)

# root.mainloop()



import streamlit as st
import random

st.set_page_config(page_title="Tic-Tac-Toe", layout="centered")
st.title("❌⭕ Tic-Tac-Toe Game")

# Initialize session state
if "board" not in st.session_state:
    st.session_state.board = [""] * 9
    st.session_state.current_player = "X"
    st.session_state.game_over = False
    st.session_state.mode = None

def check_winner():
    b = st.session_state.board
    lines = [
        (0,1,2), (3,4,5), (6,7,8),
        (0,3,6), (1,4,7), (2,5,8),
        (0,4,8), (2,4,6)
    ]
    for i, j, k in lines:
        if b[i] == b[j] == b[k] != "":
            return b[i]
    if "" not in b:
        return "Draw"
    return None

def computer_move():
    available = [i for i, val in enumerate(st.session_state.board) if val == ""]
    if available:
        move = random.choice(available)
        st.session_state.board[move] = "O"

def reset_game():
    st.session_state.board = [""] * 9
    st.session_state.current_player = "X"
    st.session_state.game_over = False

# Game mode selection
if st.session_state.mode is None:
    st.subheader("Choose Game Mode")
    if st.button("🎮 Single Player (vs Computer)"):
        st.session_state.mode = "single"
    if st.button("👥 Two Player"):
        st.session_state.mode = "two"
    st.stop()

# Display current turn
if st.session_state.game_over:
    winner = check_winner()
    if winner == "Draw":
        st.success("It's a draw!")
    else:
        st.success(f"🎉 {winner} wins!")
else:
    if st.session_state.mode == "single" and st.session_state.current_player == "O":
        computer_move()
        winner = check_winner()
        if winner:
            st.session_state.game_over = True
        else:
            st.session_state.current_player = "X"
    st.info(f"Player {st.session_state.current_player}'s Turn")

# Game board UI
cols = st.columns(3)
for i in range(9):
    with cols[i % 3]:
        if st.button(st.session_state.board[i] or " ", key=i, use_container_width=True):
            if not st.session_state.board[i] and not st.session_state.game_over:
                st.session_state.board[i] = st.session_state.current_player
                winner = check_winner()
                if winner:
                    st.session_state.game_over = True
                else:
                    st.session_state.current_player = "O" if st.session_state.current_player == "X" else "X"

# Restart button
if st.button("🔁 Restart Game"):
    reset_game()

# Reset mode button
if st.button("🔄 Change Mode"):
    st.session_state.mode = None
    reset_game()

