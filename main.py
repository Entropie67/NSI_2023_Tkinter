import tkinter as tk

root = tk.Tk()

# Partie message clair.
message_clair = tk.Frame()
message_clair.grid(column=0, row=0, columnspan=6, rowspan=6)
titre = tk.Label(message_clair, text="Message en clair")
titre.grid(column=0, row=0, columnspan=3)
saisie = tk.Text(message_clair)
saisie.grid(column=0, row=1, columnspan=3)
bouton = tk.Button(message_clair, text="Chiffrer")
bouton.grid(column=0, row=4, columnspan=6)

# Partie message chiffré.
message_chiffre = tk.Frame()
message_chiffre.grid(column=7, row=0, columnspan=6, rowspan=6)
titre = tk.Label(message_chiffre, text="Message chiffré")
titre.grid(column=0, row=0, columnspan=3)
saisie2 = tk.Text(message_chiffre)
saisie2.grid(column=0, row=1, columnspan=3)
bouton2 = tk.Button(message_chiffre, text="Déchiffrer")
bouton2.grid(column=0, row=4, columnspan=6)



obj = tk.Label(text="Mon texte")
# Pour modifier le texte
obj.config(text="second texte")


v = tk.IntVar()  # Variable de type Int
case = tk.Checkbutton(text="J'accepte de renoncer à ma liberté", variable=v)
case.select()


u = tk.IntVar()
case1 = tk.Radiobutton(variable=u, value=10)
case2 = tk.Radiobutton(variable=u, value=20)
case3 = tk.Radiobutton(variable=u, value=30)



root.mainloop()