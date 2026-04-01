# 🤖 Robots Battle (OOP Practice)

A simple Python project demonstrating Object-Oriented Programming (OOP) concepts through an automated battle between two randomized robots.

## 🌟 Overview

This project was created to practice and showcase fundamental OOP principles in Python, including:
- **Classes & Objects**: Modeling robots with specific attributes.
- **Inheritance**: Extending a base robot class to create specialized types.
- **Constructors (`__init__`)**: Initializing robot states and applying class-specific modifiers.
- **Method Overriding & `super()`**: Leveraging parent class functionality while adding unique traits.
- **Randomization**: Using the `random` module for dynamic names, classes, and stats.

## 🤖 Robot Classes

Every battle features two robots, each randomly assigned one of the following classes:

| Class | Description |
| :--- | :--- |
| **🥷 Assassin** | High damage output but very fragile. (Attack x1.7, Health /2) |
| **🛡️ Titan** | Extremely durable but deals lower damage. (Health x2.3, Attack /2) |
| **🎲 Focus (Magician)** | The wildcard. Randomly gains or loses stats upon creation. |

## 🚀 How to Run

1. Make sure you have **Python 3.x** installed.
2. Clone this repository (or download `Main.py`).
3. Run the script:
   ```bash
   python Main.py
   ```

## 🎮 How it Works

1. **Initialization**: The game picks two random names from a list (e.g., *Glorbo*, *King*, *Robo*).
2. **Class Assignment**: Each robot is assigned a random class which modifies its base stats (Level/Attack and Health).
3. **The Fight**:
   - Robots take turns attacking each other.
   - Damage dealt is based on the robot's `lvl` stat.
   - The battle continues in a loop with 1-second intervals between turns.
4. **Victory**: The game ends when one robot's health reaches 0.

## 🛠️ Requirements

- Python 3.6+
- No external libraries required (uses built-in `random` and `time`).

---
*Developed as a learning project for Python OOP.*
