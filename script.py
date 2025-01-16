import tkinter as tk

window = tk.Tk()
window.title("Shrimpnator3000")

windowW, windowH = 800, 600
screenW, screenH = window.winfo_screenwidth(), window.winfo_screenheight()
window.geometry(f"{windowW}x{windowH}+{(screenW - windowW) // 2}+{(screenH - windowH) // 2}")
window.resizable(False, False)

bg_image = tk.PhotoImage(file="assets/bg.png")
background_label = tk.Label(window, image=bg_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

window.grid_rowconfigure(0, weight=1)  # Text 'div'
window.grid_rowconfigure(1, weight=1)  # Spacer
window.grid_rowconfigure(2, weight=1)  # Buttons 'div'
window.grid_columnconfigure(0, weight=1)  # Left button
window.grid_columnconfigure(1, weight=1)  # Right button

text_label = tk.Label(window, text="Art thou a Shrimp?", font=("Arial", 16, "bold"))
text_label.place(relx=0.5, rely=0.1, anchor="center")

button1 = tk.Button(window, text="Aye", width=10, height=2)
button1.grid(row=2, column=0, pady=10, padx=(50, 10))

button2 = tk.Button(window, text="Nay", width=10, height=2)
button2.grid(row=2, column=1, pady=10, padx=(10, 50))

window.mainloop()