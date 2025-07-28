# 🐍 Snake Game using Python Turtle

A simple version of the classic Snake Game built with Python's built-in `turtle` module. This game was created as part of **Day 22** of my [#100DaysOfCode] challenge.

---

## 🎮 Features

- Snake starts with 3 blocks
- Food spawns randomly
- Snake grows as it eats food
- Collision detection:
  - Wall
  - Self
- Score and High Score tracking
- Simple and clean turtle graphics

---

## 📸 Preview

[!Screenshot][image.png]

🛠 Tech Stack
Python 3
Turtle module (standard library)

⌨️ Controls
↑ Arrow Up → Move up

↓ Arrow Down → Move down

← Arrow Left → Move left

→ Arrow Right → Move right

🧠 Logic Overview

The snake is made of square Turtle objects.

Movement is grid-based (20x20 pixel steps).

The snake grows by adding new segments to the list.

The body follows the head by tracking positions frame-by-frame.

Score increases by 10 for each food eaten.

High score is stored during the session (not persisted to file).