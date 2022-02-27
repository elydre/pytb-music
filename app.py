from mod.recherche import recherche
from mod.download import start

import tkinter as tk

# fenettre

fenettre = tk.Tk()
fenettre.title("pYtb music")
fenettre.geometry("300x390")
fenettre.resizable(width=False, height=False)

class Recherche:
    def __init__(self):
        self.resultat_butons = []
        self.barre = tk.Entry(fenettre, width=30)
        self.barre.place(x=0, y=0, width=300, height=30)
        self.barre.bind("<Return>", self.recherche)
        

    def recherche(self, event):
        self.destroy()

        query = self.barre.get()

        self.info = tk.Label(fenettre, text="Recherche en cours...")
        self.info.place(x=0, y=30, width=300, height=30)
        self.info.update()

        self.resultat = recherche(query)

        self.info.destroy()
        self.afficher()

    def afficher(self):
        
        i = 30
        for video in self.resultat[:11]:
            self.resultat_butons.append(tk.Button(fenettre, text=video.title, command=lambda video=video: self.add(video)))
            self.resultat_butons[-1].place(x=0, y=i, width=300, height=30)
            i += 30

    def destroy(self, full=False):
        for buton in self.resultat_butons:
            buton.destroy()
        self.resultat_butons = []
        if full:
            self.barre.destroy()

def LP_recherche():
    Recherche()
    
def LP_play(): ...

def LP_liste(): ...

tk.Button(fenettre, text="recherche", command=LP_recherche).place(x=0, y=360, width=100, height=30)
tk.Button(fenettre, text="play-liste", command=LP_play).place(x=100, y=360, width=100, height=30)
tk.Button(fenettre, text="lecture", command=LP_liste).place(x=200, y=360, width=100, height=30)

fenettre.mainloop()