# http://www.xavierdupre.fr/app/teachpyx/helpsphinx/c_gui/tkinter.html
import tkinter as tk

def action():
    message = entree.get()
    sortie.set(coder(message, 3))
    
def coder(f, cle):
    return "".join([chr(ord(l)+cle) for l in list(f)])

root = tk.Tk()
entree = tk.StringVar()
sortie = tk.StringVar()
# Partie de gauche
f1 = tk.Frame()
f1.grid(column=0, row=0)
titre1 = tk.Label(f1, text="Chiffrement")
titre1.grid()
s = tk.Entry(f1, textvariable=entree)
s.grid()
chiffre = tk.Button(f1,command=action, text="Chiffrement")
chiffre.grid()
# Partie de droite
f2 = tk.Frame()
f2.grid(column=1, row=0)
titre2 = tk.Label(f2, text="Déchiffrement")
titre2.grid()
s = tk.Entry(f2, textvariable=sortie)
s.grid()
chiffre = tk.Button(f2,command=action, text="Déchiffrement")
chiffre.grid()

root.mainloop()
