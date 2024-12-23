import tkinter as tk
from PIL import Image, ImageTk

class ChessGame:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Chess Game")
        
        # Board setup
        self.board_size = 8
        self.square_size = 60
        self.current_player = "white"
        
        # Initialize the board
        self.board = {}
        self.selected_piece = None
        self.setup_board()
        
        # Create the canvas
        self.canvas = tk.Canvas(
            self.window, 
            width=self.board_size * self.square_size,
            height=self.board_size * self.square_size
        )
        self.canvas.pack()
        
        # Load piece images
        self.pieces_images = {}
        self.load_pieces()
        
        # Draw initial board
        self.draw_board()
        self.place_pieces()
        
        # Bind click event
        self.canvas.bind("<Button-1>", self.handle_click)
        
    def setup_board(self):
        # Initialize piece positions
        piece_order = ['rook', 'knight', 'bishop', 'queen', 'king', 'bishop', 'knight', 'rook']
        
        # Set up white pieces
        for i in range(8):
            self.board[(i, 1)] = ('white', 'pawn')
            self.board[(i, 0)] = ('white', piece_order[i])
            
        # Set up black pieces
        for i in range(8):
            self.board[(i, 6)] = ('black', 'pawn')
            self.board[(i, 7)] = ('black', piece_order[i])
    
    def load_pieces(self):
        pieces = ['king', 'queen', 'bishop', 'knight', 'rook', 'pawn']
        colors = ['white', 'black']
        
        for piece in pieces:
            for color in colors:
                try:
                    image = Image.open(f"chess_pieces/{color}_{piece}.png")
                    image = image.resize((self.square_size, self.square_size))
                    self.pieces_images[f"{color}_{piece}"] = ImageTk.PhotoImage(image)
                except:
                    print(f"Warning: Could not load image for {color} {piece}")
    
    def draw_board(self):
        for row in range(self.board_size):
            for col in range(self.board_size):
                x1 = col * self.square_size
                y1 = row * self.square_size
                x2 = x1 + self.square_size
                y2 = y1 + self.square_size
                
                color = "#ffffff" if (row + col) % 2 == 0 else "#769656"
                self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="")
    
    def place_pieces(self):
        for pos, piece in self.board.items():
            color, piece_type = piece
            x = pos[0] * self.square_size
            y = pos[1] * self.square_size
            
            try:
                image = self.pieces_images[f"{color}_{piece_type}"]
                self.canvas.create_image(x, y, image=image, anchor="nw", tags="piece")
            except:
                print(f"Warning: Could not place {color} {piece_type}")
    
    def get_square_from_coords(self, x, y):
        return (x // self.square_size, y // self.square_size)
    
    def is_valid_move(self, start, end):
        # Basic move validation (can be expanded for proper chess rules)
        if end not in self.board:
            return True
        return self.board[end][0] != self.board[start][0]
    
    def handle_click(self, event):
        clicked_square = self.get_square_from_coords(event.x, event.y)
        
        if self.selected_piece:
            if self.is_valid_move(self.selected_piece, clicked_square):
                # Move piece
                self.board[clicked_square] = self.board[self.selected_piece]
                del self.board[self.selected_piece]
                
                # Switch turns
                self.current_player = "black" if self.current_player == "white" else "white"
                
                # Redraw board
                self.canvas.delete("piece")
                self.place_pieces()
            
            self.selected_piece = None
            self.canvas.delete("highlight")
        
        elif clicked_square in self.board:
            piece = self.board[clicked_square]
            if piece[0] == self.current_player:
                self.selected_piece = clicked_square
                # Highlight selected square
                x1 = clicked_square[0] * self.square_size
                y1 = clicked_square[1] * self.square_size
                self.canvas.create_rectangle(
                    x1, y1, 
                    x1 + self.square_size, 
                    y1 + self.square_size,
                    outline="yellow", width=2, tags="highlight"
                )
    
    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    game = ChessGame()
    game.run()