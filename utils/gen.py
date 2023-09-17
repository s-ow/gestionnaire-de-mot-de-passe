import secrets
import string
from utils.plugins.reset import resetpage
from utils.plugins.copier import *
from tkinter import *
bg = "#AEDFF7"
gris = "#D3D0CB"
fg = "#1e2f3c"
options = []



def newchoix(option):
    if option in options:
        options.pop(options.index(option))
    else:
        options.append(option)

def gen(len, options):
    if "min" in options:
        chars = string.ascii_lowercase
    if "maj" in options:
        chars += string.ascii_uppercase
    if "spe" in options:
        chars += string.punctuation
    if "num" in options:
        chars += string.digits

    mot_de_passe = ''.join(secrets.choice(chars) for _ in range(len))

    return mot_de_passe

def generateur(window):
    resetpage(window)

    mdp = Label(window, fg=fg, bg=bg)
    mdp.grid(row=0, columnspan=2)

    copy = Button(window, text="Copier", command= lambda:copier(window, mdp["text"], "mot de passe"))
    copy.grid(row=0, column=2, columnspan=2)

    b1 = Checkbutton(window, text='Lettres minuscules', command=lambda:newchoix("min"), fg=fg, bg=bg)
    b1.grid(column=0, row=1)
    b2 = Checkbutton(window, text='Lettres majuscules', command=lambda:newchoix("max"), fg=fg, bg=bg)
    b2.grid(column=1, row=1)
    b3 = Checkbutton(window, text='Caractères spéciaux', command=lambda:newchoix("spe"), fg=fg, bg=bg)
    b3.grid(column=2, row=1)
    b4 = Checkbutton(window, text='Nombres', command=lambda:newchoix("num"), fg=fg, bg=bg)
    b4.grid(column=3, row=1)

    nbr = StringVar()

    nbr = Entry(window, width=20)
    nbr.grid(row=2, columnspan=2)

    def gene(len, options):
        modp = gen(len, options)
        mdp["text"] = modp

    btn = Button(window, text="Générer", command= lambda:gene(int(nbr.get()), options))
    btn.grid(row=2, column=2, columnspan=2)