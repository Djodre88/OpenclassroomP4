#! /usr/bin/env python3
# coding: utf-8

def CreerListeJoueurs ():
    choix = "o"
    nb_participants = 0
    # datas = []
    liste_noms = []
    liste_prenoms = []
    liste_dates_naissance = []
    liste_sexes = []
    liste_classements = []

    while (choix == "o"):

        
        nom = input("Entrer le NOM de famille du joueur : ")
        liste_noms.append(nom)
        nom=nom.upper()
        # datas.append(liste_noms)

        
        prenom = input("Entrer le Prénom du joueur : ")
        prenom=prenom.capitalize()
        liste_prenoms.append(prenom)
        # datas.append(liste_prenoms)

        
        date_naissance = input("Entrer la date de naissance du joueur au format JJMMAAAA : ")
        liste_dates_naissance.append(date_naissance)
        # datas.append(liste_dates_naissance)

        
        sexe = input("Entrer le Sexe du joueur (H/F): ")
        liste_sexes.append(sexe)
        # datas.append(liste_sexes)

        
        classement = input("Entrer le Classement du joueur : ")
        while (classement in liste_classements):
            print("Deux joueurs ne peuvent avoir le même classement !")
            classement = input("Entrer le Classement du joueur : ")
        liste_classements.append(classement)
        # datas.append(liste_classements)

        nb_participants += 1

        choix = input("Ajouter un autre joueur ? o/n : ")

        while choix != "o" and choix != "n"):
            print("Réponse invalide...")
            choix = input("Ajouter un autre joueur ? o/n : ")

    print("Nombre de participants au tournoi : {}".format(nb_participants),"\n")
    print(liste_noms)
    print(liste_prenoms)
    print(liste_dates_naissance)
    print(liste_sexes)
    print(liste_classements)

    return liste_noms, liste_prenoms, liste_dates_naissance, liste_sexes, liste_classements