from tkinter import *

def resetmdp():
    with open("mdps.txt", "w") as filemdp:
        filemdp.seek(0)
        filemdp.truncate()

def resetpage(window):
    for widget in window.winfo_children():
        if widget != window.winfo_children()[0]:
            widget.destroy()