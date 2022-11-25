# http://www.xavierdupre.fr/app/teachpyx/helpsphinx/c_gui/tkinter.html
import tkinter as tk
def coder():
    f = entree.get()
    sortie.set("#"+f+"#")
    print(f)
def decoder():
    pass

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
chiffre = tk.Button(f1,command=coder, text="Chiffrement")
chiffre.grid()
# Partie de droite
f2 = tk.Frame()
f2.grid(column=1, row=0)
titre2 = tk.Label(f2, text="Déchiffrement")
titre2.grid()
s = tk.Entry(f2, textvariable=sortie)
s.grid()
chiffre = tk.Button(f2,command=decoder, text="Déchiffrement")
chiffre.grid()

root.mainloop()
