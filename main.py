import tkinter as tk

root = tk.Tk()

# Partie message clair.
message_clair = tk.Frame()
message_clair.grid(column=0, row=0, columnspan=6, rowspan=6)
titre = tk.Label(message_clair, text="Message en clair")
titre.grid(column=3, row=0, columnspan=3)

message_chiffre = tk.Frame()
message_chiffre.grid(column=7, row=0, columnspan=6, rowspan=6)
titre = tk.Label(message_chiffre, text="Message chiffré")
titre.grid(column=3, row=0, columnspan=3)

saisie = tk.Entry()


bouton = tk.Button(text="zone de texte")

bouton2 = tk.Button(text="truc")


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