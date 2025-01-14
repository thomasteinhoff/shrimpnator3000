import tkinter as tk

window = tk.Tk()
window.title("Shrimpnator3000")

windowW, windowH = 800, 600
screenW, screenH = window.winfo_screenwidth(), window.winfo_screenheight()
x = (screenW - windowW) // 2
y = (screenH - windowH) // 2
window.geometry(f"{windowW}x{windowH}+{x}+{y}")
window.resizable(False, False)

label = tk.Label(window, text="Art thou a Shrimp?", font=("Arial", 16, "bold"))
label.pack()

window.mainloop()