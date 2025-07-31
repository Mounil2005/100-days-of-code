import streamlit as st
import random

st.set_page_config(page_title="Hangman Game", page_icon="🎮")

st.title("🎯 Hangman Game")

# Hangman stages
stages = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
''', r'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', r'''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', r'''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

# Initialize session state
if "chosen_word" not in st.session_state:
    st.session_state.chosen_word = random.choice(["aardvark", "baboon", "camel"])
    st.session_state.lives = 6
    st.session_state.correct_letters = []
    st.session_state.game_over = False
    st.session_state.display = ["_"] * len(st.session_state.chosen_word)

# Input
if not st.session_state.game_over:
    guess = st.text_input("Guess a letter: ").lower()

    if guess and guess.isalpha() and len(guess) == 1:
        if guess in st.session_state.chosen_word:
            for idx, letter in enumerate(st.session_state.chosen_word):
                if letter == guess:
                    st.session_state.display[idx] = guess
            if guess not in st.session_state.correct_letters:
                st.session_state.correct_letters.append(guess)
        else:
            if guess not in st.session_state.correct_letters:
                st.session_state.lives -= 1

        if "_" not in st.session_state.display:
            st.session_state.game_over = True
            st.success("🎉 You win!")
        elif st.session_state.lives == 0:
            st.session_state.game_over = True
            st.error(f"💀 You lose! The word was: {st.session_state.chosen_word}")

# Output
st.markdown("### Word:")
st.write(" ".join(st.session_state.display))
st.markdown("### Hangman Status:")
st.code(stages[st.session_state.lives], language="text")
st.write(f"Lives Remaining: {st.session_state.lives}")

# Restart option
if st.session_state.game_over:
    if st.button("Play Again 🔁"):
        st.session_state.clear()
        st.experimental_rerun()
