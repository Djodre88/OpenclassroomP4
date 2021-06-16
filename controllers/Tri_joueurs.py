import random

##### Données joueurs
noms = ['AXELROD', 'WAGNER', 'RHOADES', 'MASON', 'ANDOLOV', 'PRINCE', 'RHOADES', 'STERN']
prenoms = ['Bobby', 'Mike', 'Chuck', 'Taylor', 'Grigor', 'Mike', 'Wendy', 'Bill']
dates_naissance = ['Janvier', 'Février', 'Mars', 'Avril', 'Mai', 'Juin', 'Juillet', 'Août']
sexes = ['M', 'M', 'M', 'A', 'M', 'M', 'F', 'M']
classements = []

##### attribution aléatoire de classement
for nom in noms:
    classement_aleatoire = random.randint(1600, 1999)
    if classement_aleatoire in classements:
        classement_aleatoire = random.randint(1600, 1999)
    classements.append(classement_aleatoire)

##### Création d'une liste de joueurs sérialisés
liste_joueurs = []
for nom, prenom, date, sexe, classement in zip (noms, prenoms, dates_naissance, sexes, classements):
    serialized_player = {
        'Nom': nom,
        'Prenom': prenom,
        'Date de naissance': date,
        'Sexe': sexe,
        'Classement': classement
        }
    liste_joueurs.append(serialized_player)

def tri_premier_tour(serialized_list):
    """
    On tri la liste en fonction du classement
    """
    sorted_list = sorted(serialized_list, key=lambda k: k["Classement"], reverse=True)
    return sorted_list

def generer_matchs_premier_tour(une_liste_de_joueurs_triee):
    """
    On génère une liste de paires
    """
    liste_paires = []
    paire = []
    for i in range(0,4):
        paire.append((une_liste_de_joueurs_triee[i]["Nom"], une_liste_de_joueurs_triee[i]["Prenom"]))
        paire.append((une_liste_de_joueurs_triee[i+4]["Nom"], une_liste_de_joueurs_triee[i+4]["Prenom"]))
        # paire.append(une_liste_de_joueurs_triee[i+4]["Nom"])
        liste_paires.append(paire)
        paire =[]    
    """
    On associe un champ resultat à chaque paire
    """
    liste_matchs = []
    # score = [0, 0]
    for lp in liste_paires:
        match =(lp, [0, 0])
        liste_matchs.append(match)               
    return liste_matchs

def verif_score(message):
    valid = False
    while not valid:
        entry = input(message)
        try:
            entry = float(entry)
            if entry in [0, 0.5, 1]:
                if entry==(1 or 0):
                    return round(entry,None)
                else:
                    return entry
                valid = True
            else:
                print("Win : 1, Draw : 0.5, Lose : 0")
        except ValueError:
            print("Veuillez entrer un score")

def saisie_des_scores(matchs):
    liste_scores = []
    for i in range(0,4):        
        score =[]        
        print ("Entrer le résultat du match {} (W : 1, D : 0.5, L : 0)".format(i+1))
        score_joueur1 = verif_score("Score de {} : ".format(matchs[i][0][0]))
        score.append(score_joueur1)        

        if score_joueur1 == 1:
            score_joueur2 = 0
        elif score_joueur1 == 0.5:
            score_joueur2 = 0.5
        else:
            score_joueur2 = 1

        score.append(score_joueur2)        
        score = [score_joueur1, score_joueur2]
        liste_scores.append(score)
    return liste_scores

 

    # return matchs

def update_rounds(matchs, liste_scores):
    rounds = []
    for i in range (0,4):
        new_tuple = (matchs[i][0], liste_scores[i])
        # matchs.pop(i)
        # matchs.insert(i, new_tuple)      
        rounds.append(new_tuple)
    return rounds

def update_classement(liste_matchs, liste_scores):
    joueurs = []
    points = []
    classement = []
    ##### Creation d'une liste de liste associant joueur et nombre de points
    for i in range(0,4):
        matchs[i][1][0] += liste_scores[i][0]
        matchs[i][1][1] += liste_scores[i][1]

        joueurs.append(liste_matchs[i][0][0])   #ajout du joueur1 à la liste pour classement
        joueurs.append(liste_matchs[i][0][1])   #ajout du joueur2 à la liste pour classement
        points.append(liste_matchs[i][1][0])    #ajout du score du joueur1 à la liste pour classement
        points.append(liste_matchs[i][1][1])    #ajout du score du joueur2 à la liste pour classement
    
    for i in range(0,8):
        classement.append([joueurs[i], points[i]])  

    # print(classement,"\n")        
    sorted_classement = sorted(classement, key=lambda s: s[1], reverse=True)    
    # print(sorted_classement,"\n")
    return sorted_classement

def generate_next_round (updated_classement):
    liste_matchs = []
    for i in range (0,4):
        match = ([updated_classement[2*i][0],updated_classement[2*i+1][0]],[updated_classement[2*i][1],updated_classement[2*i+1][1]])
        liste_matchs.append(match)
    # print(liste_matchs)    
    return liste_matchs

liste_joueurs_triee = tri_premier_tour(liste_joueurs)

i=1
print("\n-- Classement avant tournoi : \n")
for l in liste_joueurs_triee:
    print(i,". ",
    liste_joueurs_triee[liste_joueurs_triee.index(l)]["Nom"],
    liste_joueurs_triee[liste_joueurs_triee.index(l)]["Prenom"],
    "| ELO :",
    liste_joueurs_triee[liste_joueurs_triee.index(l)]["Classement"])
    i+=1

for i in range (0,4):
    if i ==0:
        matchs = generer_matchs_premier_tour(liste_joueurs_triee)
        """
        A déplacer dans les views
        """
    else:
        matchs = generate_next_round(updated_classement)

    print("\n-- Matchs Round {} : \n\n".format(i+1), matchs,"\n")
    
    scores = saisie_des_scores(matchs)
    rounds = update_rounds(matchs, scores)

    print("\n-- Resultats Round {} : \n\n".format(i+1))
    for mtch in rounds:
        print(mtch,"\n")    
    
    print("\n-- Classement à l'issue du Round {} : \n\n".format(i+1))
    
    updated_classement = update_classement(matchs, scores)
    for el in updated_classement:
        print(el)

print("\n\n-- FIN DE LA PARTIE --\n\nRetour au Menu Principal...\n\n")