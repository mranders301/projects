import tkinter as tk
from tkinter import ttk
import random
import math

class GameLobby:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Tic Tac Toe")
        
        # Center the window
        window_width = 800
        window_height = 600
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        center_x = int(screen_width/2 - window_width/2)
        center_y = int(screen_height/2 - window_height/2)
        self.window.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
        
        self.window.configure(bg="#0A0A0A")
        
        # Colors
        self.COLORS = {
            'bg_dark': '#0A0A0A',
            'bg_light': '#1A1A1A',
            'red': '#FF0F4F',
            'blue': '#0066FF',
            'white': '#FFFFFF',
            'gray': '#333333'
        }
        
        # Create main container
        self.main_frame = tk.Frame(self.window, bg=self.COLORS['bg_dark'])
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Create canvas for decorative elements
        self.canvas = tk.Canvas(
            self.main_frame,
            width=800,
            height=600,
            bg=self.COLORS['bg_dark'],
            highlightthickness=0
        )
        self.canvas.place(x=0, y=0)
        
        # Add decorative elements
        self.draw_decorative_elements()
        
        # Create content frame
        content_frame = tk.Frame(self.main_frame, bg=self.COLORS['bg_dark'])
        content_frame.place(relx=0.5, rely=0.5, anchor="center")
        
        # Create title with glowing effect
        title_frame = tk.Frame(content_frame, bg=self.COLORS['bg_dark'])
        title_frame.pack(pady=(0, 30))
        
        glow = tk.Label(
            title_frame,
            text="TIC TAC TOE",
            font=("Arial Black", 45, "bold"),
            bg=self.COLORS['bg_dark'],
            fg=self.COLORS['red']
        )
        glow.pack()
        
        title = tk.Label(
            title_frame,
            text="TIC TAC TOE",
            font=("Arial Black", 44, "bold"),
            bg=self.COLORS['bg_dark'],
            fg=self.COLORS['white']
        )
        title.place(relx=0.5, rely=0.5, anchor="center")
        
        # Create subtitle with modern styling
        subtitle = tk.Label(
            content_frame,
            text="CHOOSE YOUR GAME MODE",
            font=("Arial", 14, "bold"),
            bg=self.COLORS['bg_dark'],
            fg=self.COLORS['blue']
        )
        subtitle.pack(pady=(0, 40))
        
        # Button styles
        button_style = {
            "font": ("Arial", 14, "bold"),
            "width": 25,
            "height": 2,
            "border": 0,
            "cursor": "hand2"
        }
        
        # Create modern buttons with hover effect
        pvp_button = tk.Button(
            content_frame,
            text="PLAYER VS PLAYER",
            command=self.start_pvp,
            bg=self.COLORS['red'],
            fg=self.COLORS['white'],
            activebackground=self.COLORS['blue'],
            activeforeground=self.COLORS['white'],
            **button_style
        )
        pvp_button.pack(pady=10)
        
        pvc_button = tk.Button(
            content_frame,
            text="PLAYER VS COMPUTER",
            command=self.start_pvc,
            bg=self.COLORS['blue'],
            fg=self.COLORS['white'],
            activebackground=self.COLORS['red'],
            activeforeground=self.COLORS['white'],
            **button_style
        )
        pvc_button.pack(pady=10)
        
        # Add hover effects
        for button in [pvp_button, pvc_button]:
            button.bind("<Enter>", lambda e, b=button: self.on_hover(e, b))
            button.bind("<Leave>", lambda e, b=button: self.on_leave(e, b))
        
        # Create modern footer
        footer_frame = tk.Frame(self.main_frame, bg=self.COLORS['bg_dark'])
        footer_frame.pack(side=tk.BOTTOM, pady=20)
        
        footer = tk.Label(
            footer_frame,
            text="© 2024 | MODERN TIC TAC TOE",
            font=("Arial", 10),
            bg=self.COLORS['bg_dark'],
            fg=self.COLORS['gray']
        )
        footer.pack()

    def draw_decorative_elements(self):
        # Draw animated circles
        for i in range(5):
            x = random.randint(0, 800)
            y = random.randint(0, 600)
            size = random.randint(100, 200)
            color = self.COLORS['red'] if i % 2 == 0 else self.COLORS['blue']
            self.canvas.create_oval(
                x-size/2, y-size/2, 
                x+size/2, y+size/2, 
                fill="", outline=color, width=2
            )
        
        # Draw grid lines
        for i in range(10):
            offset = i * 80
            self.canvas.create_line(
                offset, 0, offset, 600,
                fill=self.COLORS['gray'], width=1
            )
            self.canvas.create_line(
                0, offset, 800, offset,
                fill=self.COLORS['gray'], width=1
            )

    def on_hover(self, event, button):
        if button['bg'] == self.COLORS['red']:
            button.configure(bg=self.COLORS['blue'])
        else:
            button.configure(bg=self.COLORS['red'])

    def on_leave(self, event, button):
        if button['bg'] == self.COLORS['blue']:
            button.configure(bg=self.COLORS['red'])
        else:
            button.configure(bg=self.COLORS['blue'])

    def start_pvp(self):
        self.window.destroy()
        from main import TicTacToe
        game = TicTacToe(mode="pvp")
        game.run()

    def start_pvc(self):
        self.window.destroy()
        from main import TicTacToe
        game = TicTacToe(mode="pvc")
        game.run()

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    lobby = GameLobby()
    lobby.run() 