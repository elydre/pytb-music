from mod.recherche import recherche
from mod.download import start


sortie = recherche("jain come")[0]

start([sortie.link])