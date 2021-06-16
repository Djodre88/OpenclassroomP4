#! /usr/bin/env python3
# coding: utf-8

def CreerListeDictJoueurs(list_noms, list_prenoms, list_dates_naissance, list_sexes, list_classements):
    liste_joueurs = []
    for nom, prenom, date, sexe, classement in zip (list_noms, list_prenoms, list_dates_naissance, list_sexes, list_classements):
        dict_joueur = {
            'Nom': nom,
            'Prénom': prenom,
            'Date de naissance': date,
            'Sexe': sexe,
            'Classement': classement
            }
        liste_joueurs.append(dict_joueur)
    return liste_joueurs