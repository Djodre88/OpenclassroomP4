from models.Model import Model


class Round(Model):
    def __init__(self):
        super().__init__()
        # self.number = number
        self.matchs = []

    def tri_premier_tour(self, serialized_players):
        """
        On tri la liste en fonction du classement
        """
        sorted_list = sorted(serialized_players, key=lambda k: k["elo"], reverse=True)
        return sorted_list

    def generer_matchs_premier_tour(self, une_liste_de_joueurs_triee):
        """
        On génère une liste de paires
        """
        liste_paires = []
        paire = []
        for i in range(0, 4):
            paire.append((une_liste_de_joueurs_triee[i]["name"], une_liste_de_joueurs_triee[i]["firstname"]))
            paire.append((une_liste_de_joueurs_triee[i+4]["name"], une_liste_de_joueurs_triee[i+4]["firstname"]))
            # paire.append(une_liste_de_joueurs_triee[i+4]["Nom"])
            liste_paires.append(paire)
            paire = []
        """
        On associe un champ resultat à chaque paire
        """
        liste_matchs = []
        # score = [0, 0]
        for lp in liste_paires:
            match = (lp, [0, 0])
            liste_matchs.append(match)
        return liste_matchs

    def update_rounds(self, matchs, liste_scores):
        rounds = []
        for i in range(0, 4):
            new_tuple = (matchs[i][0], liste_scores[i])
            rounds.append(new_tuple)
        return rounds

    def update_classement(self, liste_matchs, liste_scores):
        joueurs = []
        points = []
        classement = []
        # Creation d'une liste de liste associant joueur et nombre de points
        for i in range(0, 4):
            liste_matchs[i][1][0] += liste_scores[i][0]
            liste_matchs[i][1][1] += liste_scores[i][1]

            joueurs.append(liste_matchs[i][0][0])   # ajout du joueur1 à la liste pour classement
            joueurs.append(liste_matchs[i][0][1])   # ajout du joueur2 à la liste pour classement
            points.append(liste_matchs[i][1][0])    # ajout du score du joueur1 à la liste pour classement
            points.append(liste_matchs[i][1][1])    # ajout du score du joueur2 à la liste pour classement

        for i in range(0, 8):
            classement.append([joueurs[i], points[i]])

        sorted_classement = sorted(classement, key=lambda s: s[1], reverse=True)
        return sorted_classement

    def generate_next_round(self, updated_classement):
        liste_matchs = []
        for i in range(0, 4):
            match = ([updated_classement[2*i][0], updated_classement[2*i+1][0]], [updated_classement[2*i][1], updated_classement[2*i+1][1]])
            liste_matchs.append(match)
        return liste_matchs
