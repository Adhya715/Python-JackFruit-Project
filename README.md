# Python-JackFruit-Project

[![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)
[![GUI](https://img.shields.io/badge/Interface-Tkinter%20%7C%20CustomTkinter-green.svg)](https://github.com/TomSchimansky/CustomTkinter)
[![Status](https://img.shields.io/badge/Status-Active-success.svg)]()

> A feature-rich, multi-functional desktop application suite featuring a To-Do Chatbot, Sudoku Solver with Backtracking, Encryption Toolkit, and Games—all wrapped in a modern, dark-themed GUI.

---

## 📖 Overview

This project is a modular application launcher built using **Python** and **CustomTkinter**. It serves as a centralized hub to launch four distinct applications, demonstrating proficiency in **Object-Oriented Programming (OOP)**, **Algorithm Design**, and **GUI Development**.

The goal was to move beyond simple command-line scripts and create cohesive, interactive tools with a unified user experience.

---

## ✨ Key Modules

### 1. 📝 Aesthetic To-Do Chatbot
A conversational task manager that mimics a messaging app interface. It doesn't just list tasks; it talks to you.
- **Features:**
    - Natural language-style commands (`add`, `show`, `delete`, `done`).
    - **Priority Management:** Set tasks to High/Medium/Low priority.
    - **Search Functionality:** Filter tasks by keywords.
    - **Analytics:** `count` command shows completion statistics.

### 2. 🔐 Encryption & Decryption Toolkit
A cybersecurity utility for learning classical ciphers.
- **Supported Ciphers:** ROT13, Atbash, Vigenere, and Rail Fence.
- **Smart Decryption:** Includes a **Brute Force / "Try All"** mode to attempt cracking messages without a key.
- **UI:** Clean split-pane design for input and output with copy-to-clipboard functionality.

### 3. 🧩 Sudoku Solver (AI Powered)
A visualization of the **Recursive Backtracking Algorithm**.
- **Generation:** Creates valid Sudoku puzzles with varying difficulty.
- **Solver:** Instantly solves any valid board using algorithmic recursion.
- **Interactive:** Play the game yourself or let the bot solve it for you.

### 4. 🎮 Rock-Paper-Scissors
A classic game implementation to demonstrate game logic and state management within a GUI.
- **Features:** Score tracking, turn-based logic, and win-condition checks.

---

## 🛠️ Technical Stack

* **Language:** Python 3.10+
* **GUI Libraries:** * `tkinter` (Core widget management)
    * `customtkinter` (Modern UI elements, Dark Mode)
* **Algorithms:** * Recursive Backtracking (Sudoku)
    * String Manipulation & Modular Arithmetic (Cryptography)
* **Data Structures:** Lists, Dictionaries, Matrices (2D Lists).

---

## 📸 Screenshots

| **Main Launcher** | **Encryption Toolkit** |
|:---:|:---:|
| ![Launcher](https://via.placeholder.com/400x300?text=App+Launcher+UI) | ![Crypto](https://via.placeholder.com/400x300?text=Encryption+UI) |

| **To-Do Chatbot** | **Sudoku Solver** |
|:---:|:---:|
| ![Chatbot](https://via.placeholder.com/400x300?text=Chatbot+Interface) | ![Sudoku](https://via.placeholder.com/400x300?text=Sudoku+Solver) |

---

## 🚀 Installation & Usage

### Prerequisites
Ensure you have Python installed. You will need to install `customtkinter` as it is an external library.

```bash
pip install customtkinter
