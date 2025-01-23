import tkinter as tk

WINDOW_TITLE = "Shrimpnator3000"
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
BG_IMAGE_PATH = "assets/bg.png"

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
    """Configures grid layout."""
    window.grid_rowconfigure(0, weight=1)  # Text 'div'
    window.grid_rowconfigure(1, weight=1)  # Spacer
    window.grid_rowconfigure(2, weight=1)  # Buttons 'div'
    window.grid_columnconfigure(0, weight=1)  # Left button
    window.grid_columnconfigure(1, weight=1)  # Right button

def create_widgets(window):
    """Creates and places all widgets."""
    text_label = tk.Label(window, text="Art thou a Shrimp?", font=("Arial", 16, "bold"))
    text_label.place(relx=0.5, rely=0.1, anchor="center")

    button1 = tk.Button(window, text="Aye", command=open_popup, width=10, height=2)
    button1.grid(row=2, column=0, pady=10, padx=(50, 10))

    button2 = tk.Button(window, text="Nay", command=lambda: restart_window(window), width=10, height=2)
    button2.grid(row=2, column=1, pady=10, padx=(10, 50))

def open_popup():
    popup = tk.Toplevel()
    popup.title("GET SHRIMPED !!!!1")
    popup.geometry("1000x700")

def restart_window(window):
    window.destroy()
    main()

def main():
    window = tk.Tk()
    window.title(WINDOW_TITLE)
    center_window(window, WINDOW_WIDTH, WINDOW_HEIGHT)
    window.resizable(False, False)

    bg_image = setup_background(window, BG_IMAGE_PATH)
    setup_layout(window)
    create_widgets(window)

    window.mainloop()

if __name__ == "__main__":
    main()