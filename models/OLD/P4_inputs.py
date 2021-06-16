class Player:

    def __init__(self, **players_dict):
        for attrs_name, attrs_value in players_dict.items():
            setattr(self, attrs_name, attrs_value)

    def create_player_list ():
        """
        Saisie manuelle des joueurs
        """
        a_names_list=[]
        a_firstnames_list=[]
        a_births_list=[]
        a_sexs_list=[]
        a_classements_list=[]
        
        choix = "o"
        nb_participants = 0
        max_players = 8

        while choix == "o":
            if nb_participants==8:
                print("\n Désolé, le nombre limite de {} participants a été atteint ! ".format(max_players))
                break

            nom = input("Entrer le NOM de famille du joueur : ")
            nom=nom.upper()
            a_names_list.append(nom)
            
            prenom = input("Entrer le Prénom du joueur : ")
            prenom=prenom.capitalize()
            a_firstnames_list.append(prenom)
            
            date_naissance = input("Entrer la date de naissance du joueur au format JJMMAAAA : ")
            a_births_list.append(date_naissance)
            
            sex = input("Entrer le Sexe du joueur (H/F): ")
            a_sexs_list.append(sex)
            
            classement = input("Entrer le Classement du joueur : ")
            while int(classement) in a_classements_list:
                print("Deux joueurs ne peuvent avoir le même classement !")
                classement = input("Entrer le Classement du joueur : ")
            a_classements_list.append(int(classement))

            nb_participants += 1

            choix = input("Ajouter un autre joueur ? o/n : ")

            while choix != "o" and choix != "n":
                print("Réponse invalide...")
                choix = input("Ajouter un autre joueur ? o/n : ")

        print("\n Nombre de participants au tournoi : {}".format(nb_participants),"\n")

        return a_names_list, a_firstnames_list, a_births_list, a_sexs_list, a_classements_list

    def create_player_dict(names_list, firstnames_list, births_list, sexs_list, classements_list):
        """
        Création d'une liste de dictionnaires de joueurs
        """
        players_list = []
        for name, firstname, birth, sex, classement in zip (names_list, firstnames_list, births_list, sexs_list, classements_list):
            dict_joueur = {
                'Name': name,
                'Firstname': firstname,
                'Date_of_birth': birth,
                'Sex': sex,
                'Classement': classement
                }
            players_list.append(dict_joueur)
        return players_list

p = Player
players = p.create_player_list()

liste_noms=players[0]
liste_prenoms=players[1]
liste_dates_naissance=players[2]
liste_sexes=players[3]
liste_classements=players[4]

players_dict = p.create_player_dict(liste_noms, liste_prenoms, liste_dates_naissance, liste_sexes, liste_classements)

def main():
    for player_attributes in players_dict:
        p = Player(**player_attributes)
        # print(p.Name)
        print(players_dict)

main()