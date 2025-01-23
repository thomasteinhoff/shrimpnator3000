import tkinter as tk
from dataclasses import dataclass

@dataclass
class Config:
    WINDOW_TITLE: str = "Shrimpnator3000"
    WINDOW_WIDTH: int = 800
    WINDOW_HEIGHT: int = 600
    BG_IMAGE_PATH: str = "assets/bg.png"
    POPUP_TITLE: str = "GET SHRIMPED !!!!1"
    POPUP_WIDTH: int = 1000
    POPUP_HEIGHT: int = 700
    POPUP_IMAGE_PATH: str = "assets/getlobstered.png"

def setup_window(window, title, width, height, resizable=False):
    window.title(title)
    center_window(window, width, height)
    window.resizable(resizable, resizable)

def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    window.geometry(f"{width}x{height}+{x}+{y}")

def setup_background(window, image_path):
    bg_image = tk.PhotoImage(file=image_path)
    background_label = tk.Label(window, image=bg_image)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    window.bg_image = bg_image  # Keep a reference to avoid garbage collection

def setup_layout(window):
    configure_grid(window, 3, 2)
def configure_grid(window, rows, columns):
    for i in range(rows):
        window.grid_rowconfigure(i, weight=1)
    for j in range(columns):
        window.grid_columnconfigure(j, weight=1)

def create_widgets(window):
    text_label = tk.Label(window, text="Art thou a Shrimp?", font=("Arial", 16, "bold"))
    text_label.place(relx=0.5, rely=0.1, anchor="center")

    button1 = tk.Button(window, text="Aye", command=open_popup, width=10, height=2)
    button1.grid(row=2, column=0, pady=10, padx=(50, 10))

    button2 = tk.Button(window, text="Nay", command=lambda: restart_window(window), width=10, height=2)
    button2.grid(row=2, column=1, pady=10, padx=(10, 50))

def open_popup():
    popup = tk.Toplevel()
    setup_window(popup, Config.POPUP_TITLE, Config.POPUP_WIDTH, Config.POPUP_HEIGHT, resizable=False)
    setup_background(popup, Config.POPUP_IMAGE_PATH)

def restart_window(window):
    window.destroy()
    main()

def main():
    window = tk.Tk()
    setup_window(window, Config.WINDOW_TITLE, Config.WINDOW_WIDTH, Config.WINDOW_HEIGHT)
    setup_background(window, Config.BG_IMAGE_PATH)
    setup_layout(window)
    create_widgets(window)
    window.mainloop()

if __name__ == "__main__":
    main()