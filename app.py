from mod.recherche import recherche
from mod.download import start

import tkinter as tk

# fenettre

global PLAYLIST, ONGLET
PLAYLIST = []

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

    def add(self, video):
        PLAYLIST.append(video)
        print(video.title, "ajouté")

class Playlist:
    def __init__(self):
        i = 0
        self.resultat_butons = []
        for video in PLAYLIST[:12]:
            self.resultat_butons.append(tk.Button(fenettre, text=video.title, command=lambda video=video: self.add(video)))
            self.resultat_butons[-1].place(x=0, y=i, width=300, height=30)
            i += 30

    def destroy(self, full=False):
        for buton in self.resultat_butons:
            buton.destroy()
        self.resultat_butons = []


class Lecteur: ...

def LP(mode):
    global ONGLET
    ONGLET.destroy(True)
    ONGLET = mode()
    

tk.Button(fenettre, text="recherche", command=lambda: LP(Recherche)).place(x=0, y=360, width=100, height=30)
tk.Button(fenettre, text="play-list", command=lambda: LP(Playlist)).place(x=100, y=360, width=100, height=30)
tk.Button(fenettre, text="lecture", command=lambda: LP(Lecteur)).place(x=200, y=360, width=100, height=30)

ONGLET = Recherche()

fenettre.mainloop()