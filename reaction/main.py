import pyautogui
import win32gui
import win32api
import time
from ctypes import windll
import tkinter as tk
from threading import Thread

# Disable pyautogui's fail-safe feature
pyautogui.FAILSAFE = False

class AutoClickerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Auto Clicker")
        self.root.geometry("300x150")
        
        # Create buttons
        self.start_button = tk.Button(root, text="Start", command=self.start_program)
        self.start_button.pack(pady=20)
        
        self.stop_button = tk.Button(root, text="Stop", command=self.stop_program, state=tk.DISABLED)
        self.stop_button.pack(pady=20)
        
        # Status label
        self.status_label = tk.Label(root, text="Status: Stopped")
        self.status_label.pack(pady=10)
        
        self.running = False
        self.monitor_thread = None

    def start_program(self):
        self.running = True
        self.start_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)
        self.status_label.config(text="Status: Running")
        self.monitor_thread = Thread(target=self.monitor_colors)
        self.monitor_thread.daemon = True
        self.monitor_thread.start()

    def stop_program(self):
        self.running = False
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)
        self.status_label.config(text="Status: Stopped")

    def monitor_colors(self):
        while self.running:
            # Get current cursor position
            x, y = pyautogui.position()
            
            # Get color at cursor position
            current_color = get_pixel_color(x, y)
            
            # Click if green is detected
            if is_green(current_color):
                pyautogui.click()
                print(f"Green detected at position ({x}, {y})! Clicked!")
            
            # Small sleep to prevent high CPU usage
            time.sleep(0.001)

def get_pixel_color(x, y):
    hdc = win32gui.GetDC(0)
    color = win32gui.GetPixel(hdc, x, y)
    win32gui.ReleaseDC(0, hdc)
    return color

def is_green(color):
    # Extract RGB values
    r = color & 0xFF
    g = (color >> 8) & 0xFF
    b = (color >> 16) & 0xFF
    # Check if green component is significantly higher than others
    return g > 200 and r < 50 and b < 50

def main():
    root = tk.Tk()
    app = AutoClickerGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()