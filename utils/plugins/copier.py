import tkinter.messagebox as messagebox

def copier(window, text, type):
    if text:
        window.clipboard_clear()
        window.clipboard_append(text)
        window.update()
        messagebox.showinfo("Copie réussie", f"Le {type} a été copié dans le presse-papiers.")
    else:
        messagebox.showwarning("Aucun texte", "Aucun {type} à copier")