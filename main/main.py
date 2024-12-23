import tkinter as tk
from tkinter import messagebox
import random

class TicTacToe:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Tic Tac Toe")
        self.window.configure(bg="#2C3E50")
        
        # Game state
        self.current_player = "X"
        self.board = [""] * 9
        self.buttons = []
        
        # Styling
        self.BUTTON_STYLE = {
            "font": ("Helvetica", 24, "bold"),
            "width": 5,
            "height": 2,
            "bg": "#34495E",
            "fg": "white",
            "activebackground": "#2980B9"
        }
        
        # Create title
        title = tk.Label(
            self.window,
            text="Tic Tac Toe",
            font=("Helvetica", 24, "bold"),
            bg="#2C3E50",
            fg="white"
        )
        title.pack(pady=10)
        
        # Create game board
        board_frame = tk.Frame(self.window, bg="#2C3E50")
        board_frame.pack()
        
        # Create buttons
        for i in range(3):
            for j in range(3):
                button = tk.Button(
                    board_frame,
                    **self.BUTTON_STYLE,
                    command=lambda row=i, col=j: self.button_click(row, col)
                )
                button.grid(row=i, column=j, padx=5, pady=5)
                self.buttons.append(button)
        
        # Create reset button
        reset_button = tk.Button(
            self.window,
            text="New Game",
            font=("Helvetica", 12),
            command=self.reset_game,
            bg="#E74C3C",
            fg="white",
            activebackground="#C0392B"
        )
        reset_button.pack(pady=20)

    def button_click(self, row, col):
        index = row * 3 + col
        if self.board[index] == "":
            self.board[index] = self.current_player
            self.buttons[index].configure(
                text=self.current_player,
                fg="#3498DB" if self.current_player == "X" else "#E74C3C"
            )
            
            if self.check_winner():
                messagebox.showinfo("Game Over", f"Player {self.current_player} wins!")
                self.reset_game()
            elif "" not in self.board:
                messagebox.showinfo("Game Over", "It's a tie!")
                self.reset_game()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"

    def check_winner(self):
        # Winning combinations
        lines = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
            [0, 4, 8], [2, 4, 6]              # Diagonals
        ]
        
        for line in lines:
            if (self.board[line[0]] == self.board[line[1]] == 
                self.board[line[2]] != ""):
                return True
        return False

    def reset_game(self):
        self.board = [""] * 9
        self.current_player = "X"
        for button in self.buttons:
            button.configure(text="", fg="white")

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    game = TicTacToe()
    game.run()
