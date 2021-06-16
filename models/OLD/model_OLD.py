import random

class Joueur:
    def say_hello(self, first_name):    #méthode
        return "Wesh " + first_name     #initialisation
    def __init__(self, **dict_joueur):
        for attr_name, attr_value in dict_joueur.items():
            setattr(self, attr_name, attr_value)

noms = ['Linpou', 'Herre', 'Resseveur', 'Musse', 'Roux', 'Tritokovich', 'Goncalves', 'Gaultier']
prenoms = ['Amélie',	'Jordan', 'Caroline', 'Maxime', 'Jean-Yves', 'Clément', 'Gaëlle', 'Sylvie']
dates_naissance = ['Janvier', 'Février', 'Mars', 'Avril', 'Mai', 'Juin', 'Juillet', 'Août']
sexes = ['F', 'M', 'F', 'M', 'M', 'M', 'F', 'F']
classements = [2, 4, 5, 1, 6, 7, 8, 3]

joueurs = []

for nom, prenom, date, sexe, classement in zip (noms, prenoms, dates_naissance, sexes, classements):
    dict_joueur = {
        'Nom': nom,
        'Prénom': prenom,
        'Date de naissance': date,
        'Sexe': sexe,
        'Classement': classement
        }
    joueurs.append(dict_joueur)

print[joueur[0]

joueur = Joueur(**dict_joueur)
print (joueur.Classement)





# paire_tour1 = []
# for i in range (0,len(prenom),2):
#     paire_tour1.append([prenom[i],prenom[i+1]])
# # print (sorted(liste))
# print (paire_tour1)
# print (random.choice(paire_tour1))