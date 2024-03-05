# import
import tkinter as tk
from tkinter import Text

# ana pencere
window = tk.Tk()
window.title('Tkinter Temelleri - Text')
window.geometry('600x400')

# Text Widget  (Text Area)
txt = Text(window, height=2, width=40)


# yerleştir
txt.pack()

# mainloop
window.mainloop()