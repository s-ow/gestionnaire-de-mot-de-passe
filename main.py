from utils.settings.librairies import *
bg = "#AEDFF7"
gris = "#D3D0CB"
fg = "#1e2f3c"

createmdpfile()
if checkkey() == False:
    createkey()

# Initialisation + infos de la fenêtre==================================
window = Tk()
window.title("Gestionnaire de mots de passe")
window.configure(bg=bg)
window.geometry("1120x300")
window.minsize(width=1120, height=200)
window.iconbitmap('utils/settings/icon.ico')

# Menu en haut de la fenêtre============================================
menu_principal = Menu(window)

menu = Menu(menu_principal, tearoff=0)
menu.add_command(label="Mes mots de passe", command=lambda:mdps(window), background=gris)
menu.add_command(label="Enregistrer un mot de passe", command=lambda:newmdp(window), background=gris)
menu.add_command(label="Générer un mot de passe", command= lambda:generateur(window), background=gris)
menu.add_separator()
menu.add_command(label="Quitter", command=window.quit, background=gris)

menu_principal.add_cascade(label="Options", menu=menu)

window.config(menu=menu_principal)

titre = Label(window, text="Gestionnaire de mots de passe", font=20, fg=fg, bg=bg)
titre.grid(row=0, columnspan=3, pady=10)

a = Button(window, text="Mes mots de passe", command= lambda:mdps(window))
a.grid(row=1, column=0, padx=5)
b = Button(window, text="Enregistrer un mot de passe", command= lambda:newmdp(window))
b.grid(row=1, column=1, padx=5)
c = Button(window, text="Générer un mot de passe", command= lambda:generateur(window))
c.grid(row=1, column=2, pady=10, padx=5)

desc = Label(window, text=f"Tu as actuellement {countmdps()} mots de passe enregistrés sur ce gestionnaire !", fg=fg, bg=bg)
desc.grid(row=2, columnspan=3, pady=10)

guid = Label(window, text="Comment utiliser ce gestionnaire ?", fg=fg, bg=bg)
guid.grid(row=3, columnspan=2)

guide = Label(window, text="Créer un mot de passe : ", fg=fg, bg=bg)
guide.grid(row=4, column=0, sticky="w")
guide = Label(window, text="Rendez vous dans la catégorie d'enregistrement et suivez les instructions !", fg=fg, bg=bg)
guide.grid(row=4, column=1, sticky="w")

guide = Label(window, text="Modifier un mot de passe : ", fg=fg, bg=bg)
guide.grid(row=5, column=0, sticky="w")
guide = Label(window, text="Rendez vous dans la catégorie d'enregistrement et rentrez le nom du site que vous voulez modifier dans \"site\", puis mettez votre nouveau mot de passe !", fg=fg, bg=bg)
guide.grid(row=5, column=1, sticky="w")

window.mainloop()