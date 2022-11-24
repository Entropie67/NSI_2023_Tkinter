import tkinter as tk


# Fonction
def decoder():
    print("decode")
    v =sortie.get()
    print(v)
    text.set(chiffrement(v, -2))

def coder():
    print("code")
    v = text.get()
    print(v)
    sortie.set(chiffrement(v, 2))

chiffrement = lambda message, cle: "".join([chr(ord(e)+cle) for e in list(message)])

root = tk.Tk()

text = tk.StringVar()
text.set("")
sortie = tk.StringVar()
sortie.set("")

# Partie message clair.
message_clair = tk.Frame()
message_clair.grid(column=0, row=0, columnspan=6, rowspan=6)
titre = tk.Label(message_clair, text="Message en clair")
titre.grid(column=0, row=0, columnspan=3)
saisie = tk.Entry(message_clair, textvariable=text)
saisie.grid(column=0, row=1, columnspan=3)
bouton = tk.Button(message_clair, text="Chiffrer", command=coder)
bouton.grid(column=0, row=4, columnspan=6)




# Partie message chiffré.
message_chiffre = tk.Frame()
message_chiffre.grid(column=7, row=0, columnspan=6, rowspan=6)
titre = tk.Label(message_chiffre, text="Message chiffré")
titre.grid(column=0, row=0, columnspan=3)
saisie2 = tk.Entry(message_chiffre, textvariable=sortie)
saisie2.grid(column=0, row=1, columnspan=3)
bouton2 = tk.Button(message_chiffre, text="Déchiffrer", command=decoder)
bouton2.grid(column=0, row=4, columnspan=6)






root.mainloop()