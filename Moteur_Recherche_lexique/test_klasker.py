# coding=utf-8
#Le commentaire précédent permet d'éviter les erreurs d'affichage.

# Description et commentaires :
#   Ce script a pour but de faire des recherches de termes dans le lexique des termes mathématiques tirés du dictionnaire Geriadur ar Matematikoù de Jean Marot.
#   Il permet de trouver toutes les occurences d'un terme en Breton ou Français.
#   Il est sensible à la case (n'utilisez pas de majsucules) et les accents sont pris en compte.
#   La lettre ñ doit être écrite, elle ne peut pas être remplacée par n.
#   Attention, la lettre c’h ne doit pas s'écrire avec l'apostrophe (touche 4 de la ligne alphanumérique) mais avec une cote droite inclinée à gauche  ʼ .
#   L'utilisation de la disposition de clavier C’hwerty est donc très fortement recommandée.
#   Elle est disponible sur le site d'An Drouizig :
#
#   https://drouizig.org/outils-et-ressources/clavier-chwerty/ 
#
#   Il est possible d'effectuer une recherche seulement sur une partie du terme voulu. Ex : trian au lieu de triangle.
# Fin de la description et des commentaires.

#Pour convertir le fichier CSV en dictionnaire
import csv 

#Défini le chemin où se trouve le fichier CSV (fonctionne seulement s'il est dans le même dossier que ce script.
from inspect import getsourcefile
  
import os

def to_raw(string):
    return fr"{string}"
    
#initialisation du dictionnaire et création à partir du fichier CSV
dico = {}

path_CSV = to_raw(os.path.dirname(getsourcefile(lambda:0))+ r"\Geriaoueg_Jean_Marot_source.csv")

with open(path_CSV, mode="r", encoding="ANSI") as entrée:
    lecture = csv.reader(entrée)
    dico = {colonne[0]: colonne[1] for colonne in lecture}

#Recherche dans le lexique
print("Ne pas écrire de majuscules et respecter les accents, le ñ, lire les commentaires au début de ce script.")

continuer = "1"
while (continuer == "1"):
    j = 0
    print("Entrez un terme à chercher : ") 
    terme = input()
    print(f"Voici la liste des entrées dans lesquelles ont été trouvé \"{terme}\" : ")
    for i in dico :
        if (list(dico.keys())[j].__contains__(terme)):
            print("· "+ i + " : " + dico[i])
        elif (dico[i].__contains__(terme)) :
            print("· "+ dico[i] + " : " + i)
        j = j+1
    continuer = input("Voulez-vous faire une nouvelle recherche ? 0 : Non ; 1 : Oui ")