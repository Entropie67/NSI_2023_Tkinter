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
chiffre = tk.Button(f1,text="cliquez ici")
chiffre.grid()


root.mainloop()
