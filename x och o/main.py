import tkinter as tk
from tkinter import messagebox
import random

class TicTacToe:
    def __init__(self, mode="pvp"):
        self.window = tk.Tk()
        self.window.title("Tic Tac Toe")
        self.window.configure(bg="#0A0A0A")
        
        # Center the window
        window_width = 500
        window_height = 600
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        center_x = int(screen_width/2 - window_width/2)
        center_y = int(screen_height/2 - window_height/2)
        self.window.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
        
        # Colors
        self.COLORS = {
            'bg_dark': '#0A0A0A',
            'bg_light': '#1A1A1A',
            'red': '#FF0F4F',
            'blue': '#0066FF',
            'white': '#FFFFFF',
            'gray': '#333333'
        }
        
        # Game state
        self.current_player = "X"
        self.board = [""] * 9
        self.buttons = []
        self.mode = mode
        
        # Create main container
        main_frame = tk.Frame(self.window, bg=self.COLORS['bg_dark'])
        main_frame.pack(padx=40, pady=40)
        
        # Create title
        title = tk.Label(
            main_frame,
            text="TIC TAC TOE",
            font=("Arial Black", 36, "bold"),
            bg=self.COLORS['bg_dark'],
            fg=self.COLORS['white']
        )
        title.pack(pady=(0, 20))
        
        # Create mode label
        mode_text = "PLAYER VS PLAYER" if mode == "pvp" else "PLAYER VS COMPUTER"
        mode_label = tk.Label(
            main_frame,
            text=mode_text,
            font=("Arial", 14, "bold"),
            bg=self.COLORS['bg_dark'],
            fg=self.COLORS['blue']
        )
        mode_label.pack(pady=(0, 30))
        
        # Create game board with modern styling
        board_frame = tk.Frame(main_frame, bg=self.COLORS['bg_dark'])
        board_frame.pack()
        
        # Button styling
        self.BUTTON_STYLE = {
            "font": ("Arial Black", 32, "bold"),
            "width": 3,
            "height": 1,
            "bd": 0,
            "relief": "flat",
            "cursor": "hand2"
        }
        
        # Create game grid
        for i in range(3):
            for j in range(3):
                button = tk.Button(
                    board_frame,
                    **self.BUTTON_STYLE,
                    command=lambda row=i, col=j: self.button_click(row, col)
                )
                button.configure(
                    bg=self.COLORS['bg_light'],
                    activebackground=self.COLORS['bg_light']
                )
                button.grid(row=i, column=j, padx=5, pady=5)
                self.buttons.append(button)
                
                # Add hover effect
                button.bind("<Enter>", lambda e, b=button: self.on_hover(e, b))
                button.bind("<Leave>", lambda e, b=button: self.on_leave(e, b))
        
        # Control buttons frame
        control_frame = tk.Frame(main_frame, bg=self.COLORS['bg_dark'])
        control_frame.pack(pady=30)
        
        # Control button style
        control_style = {
            "font": ("Arial", 12, "bold"),
            "width": 15,
            "height": 2,
            "bd": 0,
            "cursor": "hand2"
        }
        
        # Create control buttons
        reset_button = tk.Button(
            control_frame,
            text="NEW GAME",
            command=self.reset_game,
            bg=self.COLORS['red'],
            fg=self.COLORS['white'],
            activebackground=self.COLORS['blue'],
            activeforeground=self.COLORS['white'],
            **control_style
        )
        reset_button.pack(side=tk.LEFT, padx=5)
        
        lobby_button = tk.Button(
            control_frame,
            text="RETURN TO LOBBY",
            command=self.return_to_lobby,
            bg=self.COLORS['blue'],
            fg=self.COLORS['white'],
            activebackground=self.COLORS['red'],
            activeforeground=self.COLORS['white'],
            **control_style
        )
        lobby_button.pack(side=tk.LEFT, padx=5)
        
        # Add hover effects to control buttons
        for button in [reset_button, lobby_button]:
            button.bind("<Enter>", lambda e, b=button: self.on_hover(e, b))
            button.bind("<Leave>", lambda e, b=button: self.on_leave(e, b))

    def button_click(self, row, col):
        index = row * 3 + col
        if self.board[index] == "":
            self.board[index] = self.current_player
            self.buttons[index].configure(
                text=self.current_player,
                fg=self.COLORS['red'] if self.current_player == "X" else self.COLORS['blue']
            )
            
            if self.check_winner():
                messagebox.showinfo("Game Over", f"Player {self.current_player} wins!")
                self.reset_game()
            elif "" not in self.board:
                messagebox.showinfo("Game Over", "It's a tie!")
                self.reset_game()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"
                if self.mode == "pvc" and self.current_player == "O":
                    self.window.after(500, self.computer_move)

    def computer_move(self):
        empty_cells = [i for i, cell in enumerate(self.board) if cell == ""]
        if empty_cells:
            index = random.choice(empty_cells)
            row, col = index // 3, index % 3
            self.button_click(row, col)

    def check_winner(self):
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
            button.configure(
                text="",
                fg=self.COLORS['white'],
                bg=self.COLORS['bg_light']
            )

    def on_hover(self, event, button):
        if button['bg'] == self.COLORS['red']:
            button.configure(bg=self.COLORS['blue'])
        elif button['bg'] == self.COLORS['blue']:
            button.configure(bg=self.COLORS['red'])
        elif button['bg'] == self.COLORS['bg_light']:
            button.configure(bg=self.COLORS['gray'])

    def on_leave(self, event, button):
        if button['bg'] == self.COLORS['blue']:
            button.configure(bg=self.COLORS['red'])
        elif button['bg'] == self.COLORS['red']:
            button.configure(bg=self.COLORS['blue'])
        elif button['bg'] == self.COLORS['gray']:
            button.configure(bg=self.COLORS['bg_light'])

    def return_to_lobby(self):
        self.window.destroy()
        # Import here to avoid circular imports
        import lobby
        game_lobby = lobby.GameLobby()
        game_lobby.run()

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    # Import here to avoid circular imports
    import lobby
    game_lobby = lobby.GameLobby()
    game_lobby.run()