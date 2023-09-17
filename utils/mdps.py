from tkinter import *
from utils.settings.librairies import *
from utils.plugins.checkkey import *
from utils.plugins.reset import *
from utils.plugins.copier import *
import json
bg = "#AEDFF7"
gris = "#D3D0CB"
fg = "#1e2f3c"

def mdps(window):
    resetpage(window)
    try:
        with open("mdps.txt", "r") as fichier:
            mdps = fichier.read()

        mdps = json.loads(mdps)
    except FileNotFoundError:
        a = Label(window, text="Tu n'as aucun mot de passe enregistré.")
        a.grid()

    if mdps == "":
        a = Label(window, text="Tu n'as aucun mot de passe enregistré.")
        a.grid()

    else:
        a = 1

        label = Label(window, text="Site", width=50, fg=fg, bg=bg)
        label.grid(row=0, column=0, sticky="w")
        label = Label(window, text="Nom d'utilisateur/email\nMot de passe", width=50, fg=fg, bg=bg)
        label.grid(row=0, column=1, sticky="w")

        for i in list(mdps.keys()):
            site = i
            user = decode(mdps[i][0].encode())
            mdp = decode(mdps[i][1].encode())

            mdpliste = Label(window, text=f"{site}", fg=fg, bg=bg)
            mdpliste.grid(row=a, column=0)

            mdpliste = Label(window, text=f"{user}", fg=fg, bg=bg)
            mdpliste.grid(row=a, column=1)
            bcopy = Button(window, text=f"Copier le nom d'utilisateur de {site}", command=lambda:copier(window, user, "nom d'utilisateur"))
            bcopy.grid(row=a, column=2)

            a += 1

            mdpliste = Label(window, text=f"{mdp}", fg=fg, bg=bg)
            mdpliste.grid(row=a, column=1)
            bcopy = Button(window, text=f"Copier le mot de passe de {site}", command=lambda:copier(window, mdp, "mot de passe"))
            bcopy.grid(row=a, column=2)

            a += 1