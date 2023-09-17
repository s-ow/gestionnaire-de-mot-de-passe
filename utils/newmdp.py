from tkinter import *
from utils.settings.librairies import *
from utils.plugins.checkkey import *
from utils.plugins.reset import resetpage
import tkinter.messagebox as messagebox
import json
bg = "#AEDFF7"
gris = "#D3D0CB"
fg = "#1e2f3c"

def save(site, user, mdp):
    if site != "" and user != "" and mdp != "":
        user = encode(user).decode()
        mdp = encode(mdp).decode()

        with open('mdps.txt', 'r+') as filemdp:
            content = filemdp.read()

            content = json.loads(content)
            content[site] = [user, mdp]

            filemdp.seek(0)
            filemdp.truncate()

            filemdp.write(json.dumps(content))

            messagebox.showinfo("Enregistrement réussi", "Le mot de passe a été enregistré.")

    else:
        messagebox.showinfo("Enregistrement échoué", "Certains champs sont vides.")

def newmdp(window):
    resetpage(window)

    site = StringVar()
    user = StringVar()
    mdp = StringVar()

    site = Label(window, text="🌐 Site", fg=fg, bg=bg)
    site.grid(row=0, column=0, sticky="w", padx=10, pady=10)
    site = Entry(window, width=30)
    site.grid(row=0, column=1, sticky="w", padx=10, pady=10)

    user = Label(window, text="👤 Nom d'utilisateur/email", fg=fg, bg=bg)
    user.grid(row=1, column=0, sticky="w", padx=10, pady=10)
    user = Entry(window, width=30)
    user.grid(row=1, column=1, sticky="w", padx=10, pady=10)

    mdp = Label(window, text="🔒 Mot de passe", fg=fg, bg=bg)
    mdp.grid(row=2, column=0, sticky="w", padx=10, pady=10)
    mdp = Entry(window, width=30)
    mdp.grid(row=2, column=1, sticky="w", padx=10, pady=10)

    bouton = Button(window, text="Enregistrer", command= lambda:[save(site.get(), user.get(), mdp.get()), user.delete(0, "end"), site.delete(0, "end"), user.delete(0, "end")])
    bouton.grid(row=3, columnspan=2, pady=10)