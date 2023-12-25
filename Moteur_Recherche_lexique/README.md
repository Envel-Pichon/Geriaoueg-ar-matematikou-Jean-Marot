Nécessite l'installation de Python 3

# Description et commentaires :
## Descrition

Ce script a pour but de faire des recherches de termes dans le lexique des termes mathématiques tirés du dictionnaire Geriadur ar Matematikoù de Jean Marot.
Il permet de trouver toutes les occurences d'un terme en Breton ou Français.

## Commentaires
- les accents sont pris en compte ;
- la lettre ñ doit être écrite, elle ne peut pas être remplacée par n ;
- attention, la lettre c’h ne doit pas s'écrire avec l'apostrophe (touche 4 de la ligne alphanumérique) mais avec une cote droite inclinée à gauche  ʼ ;
	- c’h est ainsi reconnu mais pas c'h
- l'utilisation de la disposition de clavier C’hwerty est donc très fortement recommandée :
	- elle est disponible sur le site d'[An Drouizig](https://drouizig.org/outils-et-ressources/clavier-chwerty/).
- il est possible d'effectuer une recherche seulement sur une partie du terme voulu :
	- Ex : trian au lieu de triangle (mais renvoie toutes les entrées contenant trian).
- il est possible de créer un raccourci que l'on pourra épingler à la barre des tâches dans Windows 10 :
	- en créant d'abord un raccourci de l'invite de commandes Windows cmd.exe ;
	- puis en ajoutant dans le champ Cible, à la suite de %windir%\system32\cmd.exe :
		- /c "chemin du répertoire où se trouve répertoire\Geriaoueg_ar_matematikou_Jean-Marot\Moteur_Recherche_lexique\klask.py"
		- attention, /c doit être précédé d'un espace
		- Ex : "%windir%\system32\cmd.exe /c "C:\Users\MonNom\Documents\Geriaoueg_ar_matematikou_Jean-Marot\Moteur_Recherche_lexique\klask.py"
	- il est possible enfin de changer l'icône en utilisant celle fournie dans le dossier du script.