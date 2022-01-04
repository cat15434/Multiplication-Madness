from tkinter import *
from pathlib import Path


print((Path(__file__).parent / "highscore.txt").resolve())


gui = Tk(className='Multiplication madness')
# set window size
gui.geometry("800x400")

gui.mainloop()

