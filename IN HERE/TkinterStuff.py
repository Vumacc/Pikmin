import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

window = tk.Tk()
window.geometry('250x250')
window.title('Pikmin')

pikminPath = Image.open('redPikmin.jpeg')
pikmin = ImageTk.PhotoImage(pikminPath)
displayPikmin = ttk.Label(window, image=pikmin)
displayPikmin.image = pikmin

displayPikmin.pack()

window.mainloop()
