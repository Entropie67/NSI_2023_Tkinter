# http://www.xavierdupre.fr/app/teachpyx/helpsphinx/c_gui/tkinter.html
import tkinter as tk

root = tk.Tk()
# Partie de gauche
f1 = tk.Frame()
f1.grid(column=0, row=0)
titre1 = tk.Label(f1, text="Chiffrement")
titre1.grid()
s = tk.Entry(f1)
s.grid()
chiffre = tk.Button(f1, text="cliquez ici")
chiffre.grid()
# Partie de droite
f2 = tk.Frame()
f2.grid(column=1, row=0)
titre2 = tk.Label(f2, text="Chiffrement")
titre2.grid()
s = tk.Entry(f2)
s.grid()
chiffre = tk.Button(f2, text="Déchiffrement")
chiffre.grid()

root.mainloop()
