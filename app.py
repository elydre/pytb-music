from PIL import Image
import requests
from io import BytesIO
from mod.recherche import recherche
from mod.download import start as start_download
from _thread import start_new_thread
from PIL import Image, ImageTk
import pygame

import tkinter as tk

# fenettre

global PLAYLIST, ONGLET
PLAYLIST = []

pygame.mixer.init()
fenettre = tk.Tk()
fenettre.title("pYtb music")
fenettre.geometry("300x390")
fenettre.resizable(width=False, height=False)

def download(video):
    print(video.link)
    start_download(video.link, video.link[-6:])
    video.download = True
    

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
        if video not in PLAYLIST:
            start_new_thread(download, (video,))
            PLAYLIST.append(video)
            print(video.title, "ajouté")
        else:
            print(video.title, "déjà présent")

class Playlist:
    def __init__(self):
        i = 0
        self.resultat_butons = []
        for video in PLAYLIST[:12]:
            self.resultat_butons.append([tk.Button(fenettre, text=video.title), video])
            self.resultat_butons[-1][0].place(x=0, y=i, width=300, height=30)
            i += 30
        self.set_color()

    def set_color(self):
        if len(self.resultat_butons) > 0:
            for buton in self.resultat_butons:
                if buton[1].download:
                    buton[0].configure(bg="green")
                else:
                    buton[0].configure(bg="red")
            self.resultat_butons[0][0].after(1000, self.set_color)


    def destroy(self, full=False):
        for buton in self.resultat_butons:
            buton[0].destroy()
        self.resultat_butons = []

class Lecteur:
    def __init__(self):
        self.lecteur = tk.Label(fenettre, text="chargement")
        self.lecteur.place(x=0, y=0, width=300, height=168)
        self.lecteur.update()
        self.pausse = tk.Button(fenettre, text="pause", command=lambda: pygame.mixer.music.pause())
        self.pausse.place(x=0, y=168, width=300, height=30)
        self.playbt = tk.Button(fenettre, text="play", command=lambda: pygame.mixer.music.unpause())
        self.playbt.place(x=0, y=198, width=300, height=30)
        self.play()

    def play(self):
        for video in PLAYLIST:
            if video.download:
                global photo
                print(video.image)
                photo = ImageTk.PhotoImage(Image.open(BytesIO(requests.get(video.image).content)))
                self.lecteur.configure(image=photo)
                self.lecteur.update()
                pygame.mixer.music.load(f'audio/{video.link[-6:]}.mp3')
                pygame.mixer.music.play()
        

    def destroy(self, full=False):
        self.lecteur.destroy()


def LP(mode):
    global ONGLET
    ONGLET.destroy(True)
    ONGLET = mode()
    

tk.Button(fenettre, text="recherche", command=lambda: LP(Recherche)).place(x=0, y=360, width=100, height=30)
tk.Button(fenettre, text="play-list", command=lambda: LP(Playlist)).place(x=100, y=360, width=100, height=30)
tk.Button(fenettre, text="lecture", command=lambda: LP(Lecteur)).place(x=200, y=360, width=100, height=30)

ONGLET = Recherche()

fenettre.mainloop()