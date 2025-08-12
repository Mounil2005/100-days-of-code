# import random

# EASY_LEVEL_TURNS = 10
# HARD_LEVEL_TURNS = 5

# # Function to set difficulty
# def set_difficulty():
#     level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
#     if level == "easy":
#         return EASY_LEVEL_TURNS
#     else:
#         return HARD_LEVEL_TURNS

# # Function to check user's guess against actual answer
# def check_answer(user_guess, actual_answer, turns):
#     if user_guess > actual_answer:
#         print("Too high.")
#         return turns - 1
#     elif user_guess < actual_answer:
#         print("Too low.")
#         return turns - 1
#     else:
#         print(f"You got it! The answer was {actual_answer}")
#         return 0

# # Main game logic
# def game():
#     print("\nWelcome to the Number Guessing Game!")
#     print("I'm thinking of a number between 1 and 100.")

#     answer = random.randint(1, 100)
#     # Uncomment below for debugging
#     # print(f"Pssst, the correct answer is {answer}")

#     turns = set_difficulty()
#     guess = 0

#     while guess != answer:
#         print(f"You have {turns} attempts remaining to guess the number.")
#         guess = int(input("Make a guess: "))
#         turns = check_answer(guess, answer, turns)

#         if turns == 0:
#             print("You've run out of guesses, you lose.")
#             return
#         elif guess != answer:
#             print("Guess again.")

# # Play Again Loop
# while True:
#     game()
#     play_again = input("\nDo you want to play again? (yes/no): ").lower()
#     if play_again != "yes":
#         print("Thanks for playing! Goodbye!")
#         break



# import streamlit as st
# import random

# # --- Configuration ---
# st.set_page_config(page_title="Number Guessing Game", page_icon="🎯")

# EASY_LEVEL_TURNS = 10
# HARD_LEVEL_TURNS = 5

# # --- Initialize session state defaults ---
# defaults = {
#     "answer": None,
#     "turns": 0,
#     "starting_turns": 0,
#     "attempts": 0,
#     "guess_input": 1,
#     "game_over": False,
#     "started": False,
#     "last_msg": "",
#     "last_type": "",
#     "best_score": None,  # fewest attempts to win
# }

# for k, v in defaults.items():
#     if k not in st.session_state:
#         st.session_state[k] = v


# # --- Helper functions ---
# def start_game(level: str):
#     """Start a new game with the chosen difficulty."""
#     st.session_state.answer = random.randint(1, 100)
#     st.session_state.starting_turns = EASY_LEVEL_TURNS if level == "Easy" else HARD_LEVEL_TURNS
#     st.session_state.turns = st.session_state.starting_turns
#     st.session_state.attempts = 0
#     st.session_state.game_over = False
#     st.session_state.started = True
#     st.session_state.last_msg = ""
#     st.session_state.last_type = ""


# def process_guess():
#     """Process the user's guess saved in session_state['guess_input']."""  
#     guess = int(st.session_state.get("guess_input", 1))
#     st.session_state.attempts += 1
#     answer = st.session_state.answer

#     if guess > answer:
#         st.session_state.turns -= 1
#         st.session_state.last_msg = "Too high! Try a smaller number."
#         st.session_state.last_type = "warning"
#     elif guess < answer:
#         st.session_state.turns -= 1
#         st.session_state.last_msg = "Too low! Try a larger number."
#         st.session_state.last_type = "warning"
#     else:
#         st.session_state.last_msg = f"🎉 Correct — the number was {answer}!"
#         st.session_state.last_type = "success"
#         st.session_state.game_over = True
#         if st.session_state.best_score is None or st.session_state.attempts < st.session_state.best_score:
#             st.session_state.best_score = st.session_state.attempts

#     if st.session_state.turns <= 0 and not st.session_state.game_over:
#         st.session_state.last_msg = f"💀 You've run out of guesses. The number was {answer}."
#         st.session_state.last_type = "error"
#         st.session_state.game_over = True


# def reset_to_start():
#     """Reset gameplay-related state."""
#     st.session_state.answer = None
#     st.session_state.turns = 0
#     st.session_state.starting_turns = 0
#     st.session_state.attempts = 0
#     st.session_state.guess_input = 1
#     st.session_state.game_over = False
#     st.session_state.started = False
#     st.session_state.last_msg = ""
#     st.session_state.last_type = ""


# # --- UI ---
# st.title("🎯 Number Guessing Game (Streamlit)")
# st.write("I'm thinking of a number between **1 and 100**. Choose a difficulty and try to guess it!")

# if st.session_state.best_score is not None:
#     st.info(f"🏆 Best score (fewest attempts): **{st.session_state.best_score}**")

# if not st.session_state.started:
#     difficulty = st.radio("Choose difficulty:", ("Easy", "Hard"), index=0)
#     if st.button("Start Game"):
#         start_game(difficulty)

# if st.session_state.started and not st.session_state.game_over:
#     st.write(f"🔢 Attempts remaining: **{st.session_state.turns}**")
#     with st.form(key="guess_form"):
#         st.number_input("Enter your guess:", min_value=1, max_value=100, step=1, key="guess_input")
#         submitted = st.form_submit_button("Submit Guess")
#         if submitted:
#             process_guess()

#     if st.session_state.last_msg:
#         if st.session_state.last_type == "warning":
#             st.warning(st.session_state.last_msg)
#         elif st.session_state.last_type == "success":
#             st.success(st.session_state.last_msg)
#         elif st.session_state.last_type == "error":
#             st.error(st.session_state.last_msg)
#         else:
#             st.write(st.session_state.last_msg)

#     if not st.session_state.game_over and st.session_state.turns > 0:
#         st.write("Try again!")

# if st.session_state.game_over:
#     if st.session_state.last_msg:
#         if st.session_state.last_type == "success":
#             st.success(st.session_state.last_msg)
#         elif st.session_state.last_type == "error":
#             st.error(st.session_state.last_msg)
#         else:
#             st.write(st.session_state.last_msg)

#     col_a, col_b = st.columns(2)
#     with col_a:
#         if st.button("Play Again (same difficulty)"):
#             level = "Easy" if st.session_state.starting_turns == EASY_LEVEL_TURNS else "Hard"
#             start_game(level)
#     with col_b:
#         if st.button("Reset / Choose Difficulty"):
#             reset_to_start()


import streamlit as st
import random
import time
from datetime import datetime

# --- Configuration ---
st.set_page_config(page_title="Number Guessing Game", page_icon="🎯", layout="wide")

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

# --- Initialize session state defaults ---
defaults = {
    "answer": None,
    "turns": 0,
    "starting_turns": 0,
    "attempts": 0,
    "guess_input": 1,
    "game_over": False,
    "started": False,
    "last_msg": "",
    "last_type": "",
    "best_score": None,
    "games_played": 0,
    "games_won": 0,
    "start_time": None,
    "guess_history": [],
    "current_difficulty": "Easy"
}

for k, v in defaults.items():
    if k not in st.session_state:
        st.session_state[k] = v

# --- Helper functions ---
def start_game(level: str):
    """Start a new game with the chosen difficulty."""
    st.session_state.answer = random.randint(1, 100)
    st.session_state.starting_turns = EASY_LEVEL_TURNS if level == "Easy" else HARD_LEVEL_TURNS
    st.session_state.turns = st.session_state.starting_turns
    st.session_state.attempts = 0
    st.session_state.game_over = False
    st.session_state.started = True
    st.session_state.last_msg = ""
    st.session_state.last_type = ""
    st.session_state.games_played += 1
    st.session_state.start_time = time.time()
    st.session_state.guess_history = []
    st.session_state.current_difficulty = level
    st.session_state.guess_input = 50  # Better starting point

def process_guess():
    """Process the user's guess with improved error handling."""
    try:
        guess = int(st.session_state.get("guess_input", 50))
        
        # Validate input range
        if guess < 1 or guess > 100:
            st.session_state.last_msg = "Please enter a number between 1 and 100."
            st.session_state.last_type = "error"
            return
            
        # Check for duplicate guess
        if guess in st.session_state.guess_history:
            st.session_state.last_msg = f"You already guessed {guess}! Try a different number."
            st.session_state.last_type = "warning"
            return
            
        st.session_state.guess_history.append(guess)
        st.session_state.attempts += 1
        answer = st.session_state.answer

        if guess > answer:
            st.session_state.turns -= 1
            difference = guess - answer
            hint = get_hint(difference)
            st.session_state.last_msg = f"Too high! Try a smaller number. {hint}"
            st.session_state.last_type = "warning"
        elif guess < answer:
            st.session_state.turns -= 1
            difference = answer - guess
            hint = get_hint(difference)
            st.session_state.last_msg = f"Too low! Try a larger number. {hint}"
            st.session_state.last_type = "warning"
        else:
            # Correct guess!
            time_taken = round(time.time() - st.session_state.start_time, 1)
            st.session_state.last_msg = f"🎉 Correct! The number was {answer}! Time: {time_taken}s"
            st.session_state.last_type = "success"
            st.session_state.game_over = True
            st.session_state.games_won += 1
            
            # Update best score
            if st.session_state.best_score is None or st.session_state.attempts < st.session_state.best_score:
                st.session_state.best_score = st.session_state.attempts

        # Check if out of turns
        if st.session_state.turns <= 0 and not st.session_state.game_over:
            st.session_state.last_msg = f"💀 Game over! The number was {answer}."
            st.session_state.last_type = "error"
            st.session_state.game_over = True
            
    except (ValueError, TypeError):
        st.session_state.last_msg = "Please enter a valid number."
        st.session_state.last_type = "error"

def get_hint(difference):
    """Provide contextual hints based on how close the guess is."""
    if difference <= 5:
        return "🔥 Very close!"
    elif difference <= 15:
        return "🟡 Getting warmer!"
    elif difference <= 30:
        return "❄️ Getting colder..."
    else:
        return "🥶 Way off!"

def reset_to_start():
    """Reset gameplay-related state."""
    for key in ["answer", "turns", "starting_turns", "attempts", "guess_input", 
                "game_over", "started", "last_msg", "last_type", "start_time", 
                "guess_history", "current_difficulty"]:
        if key == "guess_input":
            st.session_state[key] = 50
        elif key in st.session_state:
            st.session_state[key] = defaults.get(key, None)

def get_win_rate():
    """Calculate win rate percentage."""
    if st.session_state.games_played == 0:
        return 0
    return round((st.session_state.games_won / st.session_state.games_played) * 100, 1)

# --- UI ---
st.title("Number Guessing Game")
st.markdown("I'm thinking of a number between **1 and 100**. Choose your difficulty and let's play! 🎮")

# Sidebar with statistics
with st.sidebar:
    st.header("📊 Game Statistics")
    if st.session_state.games_played > 0:
        st.metric("Games Played", st.session_state.games_played)
        st.metric("Games Won", st.session_state.games_won)
        st.metric("Win Rate", f"{get_win_rate()}%")
        if st.session_state.best_score:
            st.metric("Best Score", f"{st.session_state.best_score} attempts")
    else:
        st.info("Start playing to see your stats!")
    
    if st.button("🗑️ Reset All Stats"):
        for key in ["games_played", "games_won", "best_score"]:
            st.session_state[key] = defaults[key]
        st.success("Stats reset!")

# Main game area
if not st.session_state.started:
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader("🎮 Choose Your Challenge")
        difficulty = st.radio(
            "Select difficulty:",
            ("Easy", "Hard"),
            index=0,
            help="Easy: 10 attempts | Hard: 5 attempts"
        )
        
        if difficulty == "Easy":
            st.info(f"🟢 Easy Mode: You get {EASY_LEVEL_TURNS} attempts")
        else:
            st.warning(f"🔴 Hard Mode: You only get {HARD_LEVEL_TURNS} attempts!")
    
    with col2:
        st.markdown("<br>", unsafe_allow_html=True)  # Spacing
        if st.button(" Start Game", type="primary", use_container_width=True):
            start_game(difficulty)
            st.rerun()

# Active game
if st.session_state.started and not st.session_state.game_over:
    # Game info header
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Attempts Left", st.session_state.turns)
    with col2:
        st.metric("Current Attempt", st.session_state.attempts + 1)
    with col3:
        st.metric("Difficulty", st.session_state.current_difficulty)
    
    # Guess history
    if st.session_state.guess_history:
        st.write("**Previous guesses:** " + " → ".join(map(str, st.session_state.guess_history)))
    
    # Guess input form
    with st.form(key="guess_form"):
        guess_col1, guess_col2 = st.columns([3, 1])
        with guess_col1:
            st.number_input(
                "Enter your guess (1-100):", 
                min_value=1, 
                max_value=100, 
                step=1, 
                key="guess_input",
                help="Pick a number between 1 and 100"
            )
        with guess_col2:
            submitted = st.form_submit_button("Guess!", type="primary", use_container_width=True)
            
        if submitted:
            process_guess()
            st.rerun()

# Display messages
if st.session_state.last_msg:
    if st.session_state.last_type == "warning":
        st.warning(st.session_state.last_msg)
    elif st.session_state.last_type == "success":
        st.success(st.session_state.last_msg)
        st.balloons()
    elif st.session_state.last_type == "error":
        st.error(st.session_state.last_msg)

# Game over options
if st.session_state.game_over:
    st.markdown("---")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("🔄 Play Again", type="primary", use_container_width=True):
            start_game(st.session_state.current_difficulty)
            st.rerun()
    
    with col2:
        if st.button("🎚️ Change Difficulty", use_container_width=True):
            reset_to_start()
            st.rerun()
            
    with col3:
        if st.button("📊 View Stats", use_container_width=True):
            st.info("Check the sidebar for detailed statistics!")

