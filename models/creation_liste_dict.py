#! /usr/bin/env python3
# coding: utf-8

import random

##### Données joueurs
noms = ['Linpou', 'Herre', 'Resseveur', 'Musse', 'Roux', 'Tritokovich', 'Goncalves', 'Gaultier']
prenoms = ['Amélie',	'Jordan', 'Caroline', 'Maxime', 'Jean-Yves', 'Clément', 'Gaëlle', 'Sylvie']
dates_naissance = ['Janvier', 'Février', 'Mars', 'Avril', 'Mai', 'Juin', 'Juillet', 'Août']
sexes = ['F', 'M', 'F', 'M', 'M', 'M', 'F', 'F']
classements = []

##### attribution aléatoire de classement
for nom in noms:
    classement_aleatoire = random.randint(1600, 1999)
    if classement_aleatoire in classements:
        classement_aleatoire = random.randint(1600, 1999)
    classements.append(classement_aleatoire)
print(classements)


#####Création d'une liste de dictionnaires de joueurs
liste_joueurs = []
for nom, prenom, date, sexe, classement in zip (noms, prenoms, dates_naissance, sexes, classements):
    dict_joueur = {
        'Nom': nom,
        'Prénom': prenom,
        'Date de naissance': date,
        'Sexe': sexe,
        'Classement': classement
        }
    liste_joueurs.append(dict_joueur)





##### Paire de joueurs liste_évolutive = liste_joueurs



print("Le match oppose {} à {}".format(liste_joueurs[0]["Prénom"], liste_joueurs[3]["Prénom"]))

# ####### Génération des paires de joueurs 1er tour ####### 
# matchs_tour1=()
#  for m in joueurs:
#      match = random.choice(joueurs)