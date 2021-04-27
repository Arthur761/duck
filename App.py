# duck
import tkinter as tk
import random
from tkinter import *

app = tk.Tk()

windowWidth = app.winfo_screenwidth()
windowHeight = app.winfo_screenheight()

width = windowWidth
height = windowHeight

def getRandomInt(begin, final):
    return random.randint(begin, final)

def moveDuck():
    canvas.coords(duck, random.randint(0, width), random.randint(0, height))
    app.after(getRandomInt(1, 5000), moveDuck)

app.geometry(f"{width}x{height}")
app.wm_attributes("-transparentcolor", "white")
app.lift()
app.wm_attributes("-topmost", True)
app.wm_attributes("-disabled", True)
#app.overrideredirect(1)

canvas = Canvas(app, bg="white", height=height, width=width, bd=0, relief='ridge')
canvas.pack()

duckImg = PhotoImage(file='duck.png')
duck = canvas.create_image(width / 2, height / 2, image=duckImg)

app.after(getRandomInt(1, 5000), moveDuck)
app.mainloop()
