from mod.recherche import recherche
from mod.download import start

import tkinter as tk

# fenettre

fenettre = tk.Tk()
fenettre.title("pYtb music")
fenettre.geometry("300x400")
fenettre.resizable(width=False, height=False)

class Recherche:
    def __init__(self):
        # barre de recherche
        self.barre = tk.Entry(fenettre, width=30)
        self.barre.pack(side=tk.TOP, fill=tk.X)
        self.barre.bind("<Return>", self.recherche)
    def recherche(self, event):
        query = self.barre.get()
        self.barre.delete(0, tk.END)
        self.barre.insert(0, "recherche en cours...")
        self.barre.update()
        self.resultat = recherche(query)
        self.barre.delete(0, tk.END)
        self.barre.insert(0, "recherche terminée")
        self.barre.update()
        self.afficher()
    def afficher(self):
        self.liste = tk.Listbox(fenettre, width=30)
        self.liste.pack(side=tk.TOP, fill=tk.X)
        for video in self.resultat:
            self.liste.insert(tk.END, video.title)
        self.liste.bind("<Double-Button-1>", self.download)

def LP_recherche():
    Recherche()
    
def LP_play(): ...

def LP_liste(): ...

tk.Button(fenettre, text="recherche", command=LP_recherche).place(x=0, y=370, width=100, height=30)
tk.Button(fenettre, text="play-liste", command=LP_play).place(x=100, y=370, width=100, height=30)
tk.Button(fenettre, text="lecture", command=LP_liste).place(x=200, y=370, width=100, height=30)

fenettre.mainloop()