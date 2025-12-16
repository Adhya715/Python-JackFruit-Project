import customtkinter as ctk
from tkinter import messagebox, simpledialog, scrolledtext
import tkinter as tk
import random
import string
from datetime import datetime

# Set theme
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# ============================================================================
# TODO APP
# ============================================================================
class TodoChatbot:
    def __init__(self, root):
        self.tasks = []
        self.root = root
        self.root.title("To-Do List Chatbot")
        self.root.geometry("600x600")
        self.root.configure(bg="#f3f0ff")

        title = tk.Label(root, text="✨ To-Do List Chatbot ✨",
                         font=("Helvetica", 20, "bold"),
                         bg="#f3f0ff", fg="#5a2ea6")
        title.pack(pady=(20, 10))

        card = tk.Frame(root, bg="white", bd=0, relief="ridge")
        card.pack(padx=20, pady=10, fill="both", expand=True)

        self.chat_display = tk.Text(card, height=20, width=50,
                                    state='disabled', wrap='word',
                                    bg="white", fg="#333",
                                    font=("Calibri", 12), bd=0, relief="flat")
        self.chat_display.pack(padx=20, pady=20, fill="both", expand=True)

        entry_frame = tk.Frame(root, bg="#f3f0ff")
        entry_frame.pack(pady=10)

        self.user_input = tk.Entry(entry_frame, width=45,
                                   font=("Calibri", 14),
                                   bg="#ffffff", fg="#333",
                                   relief="flat", bd=4,
                                   highlightbackground="#b8a6ff",
                                   highlightcolor="#7c4dff",
                                   highlightthickness=2)
        self.user_input.grid(row=0, column=0, padx=10)
        self.user_input.bind("<Return>", self.process_command)

        send_button = tk.Button(entry_frame, text="Send",
                                font=("Calibri", 12, "bold"),
                                bg="#7b5bff", fg="white",
                                activebackground="#5a38d1",
                                relief="flat", padx=12, pady=6,
                                command=self.process_command)
        send_button.grid(row=0, column=1)

        self.post_message("🌸 To-Do Chatbot!")
        self.show_help()

    def post_message(self, message):
        self.chat_display.configure(state='normal')
        self.chat_display.insert(tk.END, message + "\n")
        self.chat_display.configure(state='disabled')
        self.chat_display.see(tk.END)

    def show_help(self):
        help_text = """📝 Commands: add, show, done, delete, edit, clear, count, search, priority, help"""
        self.post_message(help_text)

    def add_task(self, task):
        self.tasks.append({"task": task, "done": False, "priority": "normal", "created": datetime.now()})
        self.post_message(f'🌟 Task added: "{task}"')

    def show_tasks(self):
        if not self.tasks:
            self.post_message("📭 No tasks yet.")
            return
        lines = ["📌 Tasks:"]
        for i, t in enumerate(self.tasks, 1):
            status = "✔️" if t["done"] else "❌"
            priority_icon = "🔴" if t["priority"] == "high" else "🟡" if t["priority"] == "medium" else "🟢"
            lines.append(f"{i}. {priority_icon} {t['task']} {status}")
        self.post_message("\n".join(lines))

    def mark_done(self, task_id):
        if 0 < task_id <= len(self.tasks):
            self.tasks[task_id - 1]["done"] = True
            self.post_message(f'✅ Task {task_id} done!')
        else:
            self.post_message("⚠️ Invalid ID")

    def delete_task(self, task_id):
        if 0 < task_id <= len(self.tasks):
            self.tasks.pop(task_id - 1)
            self.post_message(f'🗑️ Deleted!')
        else:
            self.post_message("⚠️ Invalid ID")

    def clear_tasks(self):
        self.tasks.clear()
        self.post_message("🧹 Cleared!")

    def edit_task(self, task_id, new_task):
        if 0 < task_id <= len(self.tasks):
            old_task = self.tasks[task_id - 1]["task"]
            self.tasks[task_id - 1]["task"] = new_task
            self.post_message(f'✏️ Task {task_id} updated: "{old_task}" → "{new_task}"')
        else:
            self.post_message("⚠️ Invalid ID")

    def count_tasks(self):
        total = len(self.tasks)
        done = sum(1 for t in self.tasks if t["done"])
        pending = total - done
        self.post_message(f"📊 Total: {total} | ✅ Done: {done} | ⏳ Pending: {pending}")

    def search_task(self, keyword):
        results = [f"{i}. {t['task']}" for i, t in enumerate(self.tasks, 1) if keyword.lower() in t['task'].lower()]
        if results:
            self.post_message("🔍 Search Results:\n" + "\n".join(results))
        else:
            self.post_message(f"❌ No tasks found with keyword '{keyword}'")

    def set_priority(self, task_id, priority):
        if 0 < task_id <= len(self.tasks):
            if priority.lower() in ["high", "medium", "low"]:
                self.tasks[task_id - 1]["priority"] = priority.lower()
                icons = {"high": "🔴", "medium": "🟡", "low": "🟢"}
                self.post_message(f'{icons[priority.lower()]} Priority set to {priority} for task {task_id}')
            else:
                self.post_message("⚠️ Priority must be: high, medium, or low")
        else:
            self.post_message("⚠️ Invalid ID")

    def process_command(self, event=None):
        user_input = self.user_input.get().strip()
        self.user_input.delete(0, tk.END)

        if not user_input:
            return

        self.post_message(f"> {user_input}")
        parts = user_input.split(maxsplit=2)
        command = parts[0].lower()

        if command == "add" and len(parts) > 1:
            self.add_task(" ".join(parts[1:]))
        elif command == "show":
            self.show_tasks()
        elif command == "done" and len(parts) > 1 and parts[1].isdigit():
            self.mark_done(int(parts[1]))
        elif command == "delete" and len(parts) > 1 and parts[1].isdigit():
            self.delete_task(int(parts[1]))
        elif command == "edit" :
            if len(parts) == 1 or not parts[1].isdigit():
                self.post_message("Provide a valid ID.")
            else:
                self.edit_task(int(parts[1]))
        elif command == "clear":
            self.clear_tasks()
        elif command == "count":
            self.count_tasks()
        elif command == "search" and len(parts) > 1:
            self.search_task(" ".join(parts[1:]))
        elif command == "priority" and len(parts) > 2 and parts[1].isdigit():
            self.set_priority(int(parts[1]), parts[2])
        elif command == "help":
            self.show_help()
        else:
            self.post_message("❔ Unknown command. Type 'help' for available commands")

# ============================================================================
# SUDOKU APP
# ============================================================================
def is_valid(board, index, num):
    row = index // 9
    col = index % 9
    for c in range(9):
        if board[row * 9 + c] == num:
            return False
    for r in range(9):
        if board[r * 9 + col] == num:
            return False
    start_row = (row // 3) * 3
    start_col = (col // 3) * 3
    for r in range(start_row, start_row + 3):
        for c in range(start_col, start_col + 3):
            if board[r * 9 + c] == num:
                return False
    return True

def find_empty(board):
    for i in range(81):
        if board[i] == 0:
            return i
    return None

def solve(board):
    index = find_empty(board)
    if index is None:
        return True
    numbers = list(range(1, 10))
    random.shuffle(numbers)
    for num in numbers:
        if is_valid(board, index, num):
            board[index] = num
            if solve(board):
                return True
            board[index] = 0
    return False

def generate_full_board():
    board = [0] * 81
    solve(board)
    return board

def remove_numbers(board, difficulty=40):
    removed = 0
    while removed < difficulty:
        i = random.randint(0, 80)
        if board[i] != 0:
            board[i] = 0
            removed += 1

class SudokuGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Sudoku")
        self.entries = []
        self.puzzle_board = []
        self.solution_board = []
        
        self.main_frame = tk.Frame(root, bg="#1e1f29")
        self.main_frame.pack(fill="both", expand=True, padx=10, pady=10)
        
        title = tk.Label(self.main_frame, text="🧩 Sudoku Solver", 
                        font=("Arial", 16, "bold"), bg="#1e1f29", fg="#fdcb6e")
        title.pack(pady=10)
        
        self.grid_frame = tk.Frame(self.main_frame, bg="#1e1f29")
        self.grid_frame.pack(pady=10)
        
        self.draw_grid()
        
        btn_frame = tk.Frame(self.main_frame, bg="#1e1f29")
        btn_frame.pack(pady=10)
        
        tk.Button(btn_frame, text="Generate", command=self.generate_puzzle,
                 bg="#ff7675", fg="black", font=("Arial", 10, "bold")).pack(side="left", padx=5)
        tk.Button(btn_frame, text="Solve", command=self.show_solution,
                 bg="#74b9ff", fg="black", font=("Arial", 10, "bold")).pack(side="left", padx=5)
        
        self.generate_puzzle()

    def draw_grid(self):
        for i in range(81):
            e = tk.Entry(self.grid_frame, width=2, font=("Arial", 18),
                        justify="center", borderwidth=1, bg="#2d2f3b", fg="#ffffff")
            row = i // 9
            col = i % 9
            padx = 4 if col % 3 == 0 else 2
            pady = 4 if row % 3 == 0 else 2
            e.grid(row=row, column=col, padx=padx, pady=pady)
            self.entries.append(e)

    def load_puzzle(self):
        for i in range(81):
            self.entries[i].config(state="normal")
            self.entries[i].delete(0, tk.END)
            if self.puzzle_board[i] != 0:
                self.entries[i].insert(0, str(self.puzzle_board[i]))
                self.entries[i].config(state="disabled")

    def generate_puzzle(self):
        self.solution_board = generate_full_board()
        self.puzzle_board = self.solution_board.copy()
        remove_numbers(self.puzzle_board, 40)
        self.load_puzzle()

    def show_solution(self):
        for i in range(81):
            self.entries[i].config(state="normal")
            self.entries[i].delete(0, tk.END)
            self.entries[i].insert(0, str(self.solution_board[i]))
            self.entries[i].config(state="disabled")

# ============================================================================
# ROCK PAPER SCISSORS APP
# ============================================================================
class RPSGameUI:
    def __init__(self, root, max_score=3):
        self.root = root
        self.root.title("Rock-Paper-Scissors")
        self.root.geometry("500x550")
        self.root.configure(bg="#1e1f29")
        self.max_score = max_score
        self.p1_choice = None
        self.score_p1 = 0
        self.score_p2 = 0
        self.turn = 1

        title_lbl = tk.Label(self.root, text=f"Rock-Paper-Scissors\nFirst to {max_score} wins!",
                            font=("Arial", 16, "bold"), bg="#1e1f29", fg="#fdcb6e")
        title_lbl.pack(pady=15)

        self.score_lbl = tk.Label(self.root, text="Player 1: 0 | Player 2: 0",
                                 font=("Arial", 14, "bold"), bg="#1e1f29", fg="white")
        self.score_lbl.pack(pady=10)

        self.turn_lbl = tk.Label(self.root, text="Player 1: Choose",
                                font=("Arial", 13), bg="#1e1f29", fg="#a29bfe")
        self.turn_lbl.pack(pady=10)

        btn_frame = tk.Frame(self.root, bg="#1e1f29")
        btn_frame.pack(pady=20)

        tk.Button(btn_frame, text="🪨 Rock", font=("Arial", 13, "bold"),
                 bg="#ff7675", fg="black", width=10, command=lambda: self.select_move("rock")).grid(row=0, column=0, padx=5)
        tk.Button(btn_frame, text="📄 Paper", font=("Arial", 13, "bold"),
                 bg="#74b9ff", fg="black", width=10, command=lambda: self.select_move("paper")).grid(row=0, column=1, padx=5)
        tk.Button(btn_frame, text="✂️ Scissors", font=("Arial", 13, "bold"),
                 bg="#55efc4", fg="black", width=10, command=lambda: self.select_move("scissors")).grid(row=0, column=2, padx=5)

        self.status_lbl = tk.Label(self.root, text="", font=("Arial", 12, "italic"),
                                  bg="#1e1f29", fg="#fdcb6e")
        self.status_lbl.pack(pady=15)

    def select_move(self, move):
        if self.turn == 1:
            self.p1_choice = move
            self.turn = 2
            self.turn_lbl.config(text="Player 2: Your turn")
            self.status_lbl.config(text="Player 1 chose ✔")
        elif self.turn == 2:
            self.evaluate_round(move)
            self.turn = 1
            self.turn_lbl.config(text="Player 1: Choose")

    def evaluate_round(self, p2):
        p1 = self.p1_choice
        if p1 == p2:
            self.status_lbl.config(text="🤝 Tie!")
        elif (p1 == "rock" and p2 == "scissors") or \
             (p1 == "scissors" and p2 == "paper") or \
             (p1 == "paper" and p2 == "rock"):
            self.score_p1 += 1
            self.status_lbl.config(text="✅ P1 wins!")
        else:
            self.score_p2 += 1
            self.status_lbl.config(text="🔥 P2 wins!")

        self.score_lbl.config(text=f"Player 1: {self.score_p1} | Player 2: {self.score_p2}")

        if self.score_p1 == self.max_score:
            messagebox.showinfo("Winner", "Player 1 is Champion!")
            self.root.destroy()
        elif self.score_p2 == self.max_score:
            messagebox.showinfo("Winner", "Player 2 is Champion!")
            self.root.destroy()

# ============================================================================
# ENCRYPTION APP
# ============================================================================
class EncryptionApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Encryption Toolkit")
        self.geometry("1000x700")
        self.resizable(False, False)

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.create_widgets()

    def create_widgets(self):
        main_frame = ctk.CTkFrame(self, corner_radius=0)
        main_frame.grid(row=0, column=0, sticky="nsew")
        main_frame.grid_columnconfigure(0, weight=1)
        main_frame.grid_rowconfigure(1, weight=1)

        header = ctk.CTkLabel(
            main_frame,
            text="🔐 ENCRYPTION TOOLKIT",
            font=ctk.CTkFont(size=28, weight="bold"),
            text_color="#00D4FF"
        )
        header.grid(row=0, column=0, pady=20)

        content_frame = ctk.CTkFrame(main_frame, corner_radius=15)
        content_frame.grid(row=1, column=0, padx=20, pady=(0, 20), sticky="nsew")
        content_frame.grid_columnconfigure(0, weight=1)
        content_frame.grid_rowconfigure(0, weight=1)

        self.tab_frame = ctk.CTkFrame(content_frame, corner_radius=0)
        self.tab_frame.grid(row=0, column=0, sticky="nsew")
        self.tab_frame.grid_columnconfigure(0, weight=1)
        self.tab_frame.grid_rowconfigure(1, weight=1)

        button_frame = ctk.CTkFrame(self.tab_frame, corner_radius=0, fg_color="#1a1a1a")
        button_frame.grid(row=0, column=0, sticky="ew", padx=0, pady=0)
        button_frame.grid_columnconfigure(1, weight=1)

        self.encrypt_btn = ctk.CTkButton(
            button_frame, text="Encrypt", command=self.show_encrypt_tab,
            fg_color="#00D4FF", text_color="black", hover_color="#00A3CC",
            corner_radius=0, height=40
        )
        self.encrypt_btn.grid(row=0, column=0, sticky="ew", padx=1)

        self.decrypt_btn = ctk.CTkButton(
            button_frame, text="Decrypt", command=self.show_decrypt_tab,
            fg_color="gray30", hover_color="gray35", corner_radius=0, height=40
        )
        self.decrypt_btn.grid(row=0, column=2, sticky="ew", padx=1)

        self.content_area = ctk.CTkFrame(self.tab_frame, corner_radius=0)
        self.content_area.grid(row=1, column=0, sticky="nsew", padx=20, pady=20)
        self.content_area.grid_columnconfigure(0, weight=1)
        self.tab_frame.grid_rowconfigure(1, weight=1)

        self.show_encrypt_tab()

    def show_encrypt_tab(self):
        for widget in self.content_area.winfo_children():
            widget.destroy()

        self.encrypt_btn.configure(fg_color="#00D4FF", text_color="black")
        self.decrypt_btn.configure(fg_color="gray30", text_color="white")
        self.content_area.grid_columnconfigure(0, weight=1)
        self.content_area.grid_rowconfigure(3, weight=1)

        ctk.CTkLabel(self.content_area, text="Text to Encrypt:", font=ctk.CTkFont(size=12, weight="bold")).grid(row=0, column=0, sticky="w", pady=(0, 5))
        self.encrypt_input = ctk.CTkTextbox(self.content_area, height=100, corner_radius=10)
        self.encrypt_input.grid(row=1, column=0, sticky="nsew", pady=(0, 15))
        self.content_area.grid_rowconfigure(1, weight=1)

        cipher_frame = ctk.CTkFrame(self.content_area)
        cipher_frame.grid(row=2, column=0, sticky="ew", pady=15)
        ctk.CTkLabel(cipher_frame, text="Cipher Method:", font=ctk.CTkFont(size=11, weight="bold")).pack(side="left", padx=(0, 10))
        self.cipher_var = ctk.StringVar(value="ROT13")
        for cipher in ["ROT13", "Atbash", "Vigenere", "Rail Fence"]:
            ctk.CTkRadioButton(cipher_frame, text=cipher, variable=self.cipher_var, value=cipher).pack(side="left", padx=5)

        key_frame = ctk.CTkFrame(self.content_area)
        key_frame.grid(row=3, column=0, sticky="ew", pady=10)
        ctk.CTkLabel(key_frame, text="Key (for Vigenere/Rail Fence):", font=ctk.CTkFont(size=11)).pack(side="left", padx=(0, 10))
        self.encrypt_key = ctk.CTkEntry(key_frame, placeholder_text="e.g., 'SECRET' or '3'", width=200)
        self.encrypt_key.pack(side="left", padx=5)

        ctk.CTkLabel(self.content_area, text="Encrypted Output:", font=ctk.CTkFont(size=12, weight="bold")).grid(row=4, column=0, sticky="w", pady=(15, 5))
        self.encrypt_output = ctk.CTkTextbox(self.content_area, height=80, corner_radius=10)
        self.encrypt_output.grid(row=5, column=0, sticky="nsew", pady=(0, 15))
        self.content_area.grid_rowconfigure(5, weight=1)

        button_frame = ctk.CTkFrame(self.content_area)
        button_frame.grid(row=6, column=0, sticky="ew")
        button_frame.grid_columnconfigure(0, weight=1)
        ctk.CTkButton(button_frame, text="Encrypt", command=self.perform_encryption, fg_color="#00D4FF", text_color="black", hover_color="#00A3CC", height=35, font=ctk.CTkFont(size=11, weight="bold")).pack(side="left", padx=5)
        ctk.CTkButton(button_frame, text="Copy Output", command=self.copy_encrypt_output, height=35).pack(side="left", padx=5)
        ctk.CTkButton(button_frame, text="Clear", command=lambda: [self.encrypt_input.delete("1.0", "end"), self.encrypt_output.delete("1.0", "end")], height=35).pack(side="left", padx=5)

    def show_decrypt_tab(self):
        for widget in self.content_area.winfo_children():
            widget.destroy()

        self.decrypt_btn.configure(fg_color="#00D4FF", text_color="black")
        self.encrypt_btn.configure(fg_color="gray30", text_color="white")
        self.content_area.grid_columnconfigure(0, weight=1)
        self.content_area.grid_rowconfigure(3, weight=1)

        ctk.CTkLabel(self.content_area, text="Text to Decrypt:", font=ctk.CTkFont(size=12, weight="bold")).grid(row=0, column=0, sticky="w", pady=(0, 5))
        self.decrypt_input = ctk.CTkTextbox(self.content_area, height=100, corner_radius=10)
        self.decrypt_input.grid(row=1, column=0, sticky="nsew", pady=(0, 15))
        self.content_area.grid_rowconfigure(1, weight=1)

        mode_frame = ctk.CTkFrame(self.content_area)
        mode_frame.grid(row=2, column=0, sticky="ew", pady=15)
        ctk.CTkLabel(mode_frame, text="Decryption Mode:", font=ctk.CTkFont(size=11, weight="bold")).pack(side="left", padx=(0, 10))
        self.decrypt_mode_var = ctk.StringVar(value="manual")
        ctk.CTkRadioButton(mode_frame, text="Manual Selection", variable=self.decrypt_mode_var, value="manual", command=self.update_decrypt_ui).pack(side="left", padx=5)
        ctk.CTkRadioButton(mode_frame, text="Try All (Brute Force)", variable=self.decrypt_mode_var, value="brute", command=self.update_decrypt_ui).pack(side="left", padx=5)

        self.cipher_selection_frame = ctk.CTkFrame(self.content_area)
        self.cipher_selection_frame.grid(row=3, column=0, sticky="ew", pady=10)
        self.key_input_frame = ctk.CTkFrame(self.content_area)
        self.key_input_frame.grid(row=4, column=0, sticky="ew", pady=10)
        self.update_decrypt_ui()

        ctk.CTkLabel(self.content_area, text="Decrypted Output:", font=ctk.CTkFont(size=12, weight="bold")).grid(row=5, column=0, sticky="w", pady=(15, 5))
        self.decrypt_output = ctk.CTkTextbox(self.content_area, height=80, corner_radius=10)
        self.decrypt_output.grid(row=6, column=0, sticky="nsew", pady=(0, 15))
        self.content_area.grid_rowconfigure(6, weight=1)

        button_frame = ctk.CTkFrame(self.content_area)
        button_frame.grid(row=7, column=0, sticky="ew")
        button_frame.grid_columnconfigure(0, weight=1)
        ctk.CTkButton(button_frame, text="Decrypt", command=self.perform_decryption, fg_color="#00D4FF", text_color="black", hover_color="#00A3CC", height=35, font=ctk.CTkFont(size=11, weight="bold")).pack(side="left", padx=5)
        ctk.CTkButton(button_frame, text="Copy Output", command=self.copy_decrypt_output, height=35).pack(side="left", padx=5)
        ctk.CTkButton(button_frame, text="Clear", command=lambda: [self.decrypt_input.delete("1.0", "end"), self.decrypt_output.delete("1.0", "end")], height=35).pack(side="left", padx=5)

    def update_decrypt_ui(self):
        for widget in self.cipher_selection_frame.winfo_children():
            widget.destroy()
        for widget in self.key_input_frame.winfo_children():
            widget.destroy()

        if self.decrypt_mode_var.get() == "manual":
            ctk.CTkLabel(self.cipher_selection_frame, text="Cipher Method:", font=ctk.CTkFont(size=11, weight="bold")).pack(side="left", padx=(0, 10))
            self.decrypt_cipher_var = ctk.StringVar(value="ROT13")
            for cipher in ["ROT13", "Atbash", "Vigenere", "Rail Fence"]:
                ctk.CTkRadioButton(self.cipher_selection_frame, text=cipher, variable=self.decrypt_cipher_var, value=cipher).pack(side="left", padx=5)
            ctk.CTkLabel(self.key_input_frame, text="Key (if needed):", font=ctk.CTkFont(size=11)).pack(side="left", padx=(0, 10))
            self.decrypt_key = ctk.CTkEntry(self.key_input_frame, placeholder_text="e.g., 'SECRET' or '3'", width=200)
            self.decrypt_key.pack(side="left", padx=5)

    def perform_encryption(self):
        text = self.encrypt_input.get("1.0", "end-1c")
        cipher = self.cipher_var.get()
        key = self.encrypt_key.get()
        if not text:
            messagebox.showwarning("Input Error", "Please enter text to encrypt")
            return
        try:
            if cipher == "ROT13":
                result = self.rot13(text)
            elif cipher == "Atbash":
                result = self.atbash(text)
            elif cipher == "Vigenere":
                if not key:
                    messagebox.showwarning("Input Error", "Please enter a key for Vigenere")
                    return
                result = self.vigenere_encrypt(text, key)
            elif cipher == "Rail Fence":
                if not key:
                    messagebox.showwarning("Input Error", "Please enter number of rails")
                    return
                result = self.rail_fence_encrypt(text, int(key))
            self.encrypt_output.delete("1.0", "end")
            self.encrypt_output.insert("1.0", result)
        except Exception as e:
            messagebox.showerror("Error", f"Encryption failed: {str(e)}")

    def perform_decryption(self):
        text = self.decrypt_input.get("1.0", "end-1c")
        if not text:
            messagebox.showwarning("Input Error", "Please enter text to decrypt")
            return
        self.decrypt_output.delete("1.0", "end")
        try:
            if self.decrypt_mode_var.get() == "manual":
                cipher = self.decrypt_cipher_var.get()
                key = self.decrypt_key.get()
                if cipher == "ROT13":
                    result = self.rot13(text)
                elif cipher == "Atbash":
                    result = self.atbash(text)
                elif cipher == "Vigenere":
                    if not key:
                        messagebox.showwarning("Input Error", "Please enter a key")
                        return
                    result = self.vigenere_decrypt(text, key)
                elif cipher == "Rail Fence":
                    if not key:
                        messagebox.showwarning("Input Error", "Please enter number of rails")
                        return
                    result = self.rail_fence_decrypt(text, int(key))
                self.decrypt_output.insert("1.0", result)
            else:
                results = []
                results.append("=== ROT13 ===\n" + self.rot13(text) + "\n\n")
                results.append("=== ATBASH ===\n" + self.atbash(text) + "\n\n")
                results.append("=== VIGENERE (Common keys) ===\n")
                common_keys = ["SECRET", "KEY", "PASSWORD", "PYTHON", "CIPHER", "TEST"]
                for key in common_keys:
                    try:
                        results.append(f"Key '{key}': {self.vigenere_decrypt(text, key)}\n")
                    except:
                        pass
                results.append("\n=== RAIL FENCE (2-5 rails) ===\n")
                for rails in range(2, 6):
                    try:
                        results.append(f"Rails {rails}: {self.rail_fence_decrypt(text, rails)}\n")
                    except:
                        pass
                self.decrypt_output.insert("1.0", "".join(results))
        except Exception as e:
            messagebox.showerror("Error", f"Decryption failed: {str(e)}")

    @staticmethod
    def rot13(text):
        return text.translate(str.maketrans(
            'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ',
            'nopqrstuvwxyzabcdefghijklmNOPQRSTUVWXYZABCDEFGHIJKLM'
        ))

    @staticmethod
    def atbash(text):
        result = []
        for char in text:
            if char.isalpha():
                if char.isupper():
                    result.append(chr(ord('Z') - (ord(char) - ord('A'))))
                else:
                    result.append(chr(ord('z') - (ord(char) - ord('a'))))
            else:
                result.append(char)
        return ''.join(result)

    @staticmethod
    def vigenere_encrypt(text, key):
        result = []
        key = key.upper()
        key_index = 0
        for char in text:
            if char.isalpha():
                shift = ord(key[key_index % len(key)]) - ord('A')
                if char.isupper():
                    result.append(chr((ord(char) - ord('A') + shift) % 26 + ord('A')))
                else:
                    result.append(chr((ord(char) - ord('a') + shift) % 26 + ord('a')))
                key_index += 1
            else:
                result.append(char)
        return ''.join(result)

    @staticmethod
    def vigenere_decrypt(text, key):
        result = []
        key = key.upper()
        key_index = 0
        for char in text:
            if char.isalpha():
                shift = ord(key[key_index % len(key)]) - ord('A')
                if char.isupper():
                    result.append(chr((ord(char) - ord('A') - shift) % 26 + ord('A')))
                else:
                    result.append(chr((ord(char) - ord('a') - shift) % 26 + ord('a')))
                key_index += 1
            else:
                result.append(char)
        return ''.join(result)

    @staticmethod
    def rail_fence_encrypt(text, rails):
        if rails == 1:
            return text
        fence = [[] for _ in range(rails)]
        rail = 0
        direction = 1
        for char in text:
            fence[rail].append(char)
            if rail == 0:
                direction = 1
            elif rail == rails - 1:
                direction = -1
            rail += direction
        return ''.join(''.join(row) for row in fence)

    @staticmethod
    def rail_fence_decrypt(text, rails):
        if rails == 1:
            return text
        fence = [[] for _ in range(rails)]
        rail = 0
        direction = 1
        for _ in text:
            fence[rail].append(None)
            if rail == 0:
                direction = 1
            elif rail == rails - 1:
                direction = -1
            rail += direction
        index = 0
        for i in range(rails):
            for j in range(len(fence[i])):
                fence[i][j] = text[index]
                index += 1
        result = []
        rail = 0
        direction = 1
        for _ in text:
            result.append(fence[rail].pop(0))
            if rail == 0:
                direction = 1
            elif rail == rails - 1:
                direction = -1
            rail += direction
        return ''.join(result)

    def copy_encrypt_output(self):
        output = self.encrypt_output.get("1.0", "end-1c")
        self.clipboard_clear()
        self.clipboard_append(output)
        messagebox.showinfo("Success", "Output copied to clipboard!")

    def copy_decrypt_output(self):
        output = self.decrypt_output.get("1.0", "end-1c")
        self.clipboard_clear()
        self.clipboard_append(output)
        messagebox.showinfo("Success", "Output copied to clipboard!")

# ============================================================================
# MAIN MENU
# ============================================================================
class MenuApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("App Menu Launcher")
        self.geometry("900x650")
        self.resizable(False, False)
        
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        
        self.create_widgets()
    
    def create_widgets(self):
        main_frame = ctk.CTkFrame(self, fg_color="#0a0a0a", corner_radius=0)
        main_frame.grid(row=0, column=0, sticky="nsew")
        main_frame.grid_columnconfigure(0, weight=1)
        main_frame.grid_rowconfigure(1, weight=1)
        
        header_frame = ctk.CTkFrame(main_frame, fg_color="#1e1f29", corner_radius=0)
        header_frame.grid(row=0, column=0, sticky="ew", padx=0, pady=0)
        header_frame.grid_columnconfigure(0, weight=1)
        
        title = ctk.CTkLabel(header_frame, text="🚀 Application Hub",
                            font=ctk.CTkFont(size=32, weight="bold"),
                            text_color="#00D4FF")
        title.pack(pady=20)
        
        subtitle = ctk.CTkLabel(header_frame, text="Select and launch your application",
                               font=ctk.CTkFont(size=14),
                               text_color="#888888")
        subtitle.pack(pady=(0, 15))
        
        content_frame = ctk.CTkFrame(main_frame, fg_color="#0a0a0a")
        content_frame.grid(row=1, column=0, sticky="nsew", padx=20, pady=20)
        content_frame.grid_columnconfigure(0, weight=1)
        content_frame.grid_columnconfigure(1, weight=1)
        
        apps_info = [
            {"name": "📝 To-Do Chatbot", "desc": "Manage tasks with chatbot",
             "icon": "✨", "color": "#7b5bff", "cmd": self.launch_todo},
            {"name": "🧩 Sudoku Solver", "desc": "Generate and solve sudoku",
             "icon": "🎮", "color": "#ff7675", "cmd": self.launch_sudoku},
            {"name": "🔐 Encryption", "desc": "Encrypt/decrypt messages",
             "icon": "🔒", "color": "#00D4FF", "cmd": self.launch_encryption},
            {"name": "🎯 Rock-Paper-Scissors", "desc": "Two-player game",
             "icon": "🎲", "color": "#55efc4", "cmd": self.launch_rps}
        ]
        
        for idx, app in enumerate(apps_info):
            row = idx // 2
            col = idx % 2
            self.create_app_card(content_frame, app, row, col)
    
    def create_app_card(self, parent, app, row, col):
        card = ctk.CTkFrame(parent, fg_color="#2d2f3b", corner_radius=15,
                           border_width=2, border_color=app["color"])
        card.grid(row=row, column=col, sticky="nsew", padx=10, pady=10)
        card.grid_columnconfigure(0, weight=1)
        
        header = ctk.CTkFrame(card, fg_color="#2d2f3b", corner_radius=0)
        header.pack(fill="x", padx=15, pady=(15, 10))
        header.grid_columnconfigure(1, weight=1)
        
        ctk.CTkLabel(header, text=app["icon"], font=ctk.CTkFont(size=28)).grid(row=0, column=0, padx=(0, 10))
        ctk.CTkLabel(header, text=app["name"], font=ctk.CTkFont(size=16, weight="bold"),
                    text_color=app["color"]).grid(row=0, column=1, sticky="w")
        
        ctk.CTkLabel(card, text=app["desc"], font=ctk.CTkFont(size=12),
                    text_color="#aaaaaa", wraplength=250).pack(fill="x", padx=15, pady=(0, 15))
        
        ctk.CTkButton(card, text="Launch →", font=ctk.CTkFont(size=13, weight="bold"),
                     fg_color=app["color"], text_color="black",
                     corner_radius=8, height=40, command=app["cmd"]).pack(fill="x", padx=15, pady=(0, 15))
    
    def launch_todo(self):
        try:
            window = ctk.CTkToplevel(self)
            window.title("To-Do Chatbot")
            window.geometry("600x600")
            TodoChatbot(window)
        except Exception as e:
            messagebox.showerror("Error", f"Failed: {str(e)}")
    
    def launch_sudoku(self):
        try:
            window = ctk.CTkToplevel(self)
            window.title("Sudoku")
            window.geometry("550x650")
            SudokuGame(window)
        except Exception as e:
            messagebox.showerror("Error", f"Failed: {str(e)}")
    
    def launch_encryption(self):
        try:
            app = EncryptionApp()
            app.mainloop()
        except Exception as e:
            messagebox.showerror("Error", f"Failed: {str(e)}")
    
    def launch_rps(self):
        try:
            window = ctk.CTkToplevel(self)
            window.title("Rock-Paper-Scissors")
            RPSGameUI(window)
        except Exception as e:
            messagebox.showerror("Error", f"Failed: {str(e)}")


if __name__ == "__main__":
    app = MenuApp()
    app.mainloop()
