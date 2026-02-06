## 🧬 Bio-Quest RPG

A Python-based terminal role-playing game where players must verify their identity, login, and embark on a biological adventure. This project demonstrates fundamental Python concepts like Object-Oriented Programming (OOP), modular file structures, and user input handling.

## 📂 Project Structure

- The project is organized into specific sections to keep the code modular and clean:
- main_section.py: The entry point of the application.
- game_controller.py: The "brain" of the game that coordinates between different sections.
- home_section.py: Handles the initial landing screen and verification.
- login_section.py: Manages user authentication with attempt limits.
- player_section.py: Handles character creation, profiles, and updates.

## 🚀 Getting Started

Prerequisites
 
 - Python 3.x installed on your machine.
 - A terminal or VS Code.

How to Run

 - Open your terminal in the bio-quest-rpg folder.

Run the main script:

Bash

 - python main_section.py

## 🎮 Core Features

🔐 Authentication System
The game includes a security layer where players must:

- Pass a verification check in the Home Section.
- Login with a specific username and password (default: R / 5).
- Manage limited login attempts (max 3) before being locked out.

## 👤 Character Management

Once logged in, the Main Menu allows players to:

- Create/Update: Define your biological character's traits.
- View Profile: Check your current stats and character details.
- Delete: Remove character data to start fresh.

## 🗺️ The Bio-Quest

The main game loop where the biological RPG elements take place (currently in development).

## 🛠️ Built With

Python 3 - The core programming language.

VS Code - The recommended IDE for development.

## 📝 License

This project is for educational purposes as part of the Python Roadmap Fundamentals.