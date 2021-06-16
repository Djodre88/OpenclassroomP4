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
        
        choix = "Y"
        nb_participants = 0
        max_players = 8

        while choix in ["y", "Y"]:
            if nb_participants == max_players:
                print("\n/!\ Désolé, le nombre limite de {} participants a été atteint ! ".format(max_players))
                break

            nom = input("Entrer le NOM de famille du joueur : ")
            nom=nom.upper()
            a_names_list.append(nom)
            
            prenom = input("Entrer le Prénom du joueur : ")
            prenom=prenom.capitalize()
            a_firstnames_list.append(prenom)
            
            date_naissance = input("Entrer la date de naissance du joueur au format JJMMAAAA : ")
            # date = verif_correct_date(date, msg_date) #IMPORTER MODULE VERIF
            a_births_list.append(date_naissance)

            
            sex = input("Entrer le Sexe du joueur (H/F): ")
            #sex = verif_sex(sex, msg_sex)
            a_sexs_list.append(sex)

            
            classement = input("Entrer le Classement du joueur : ")
            # classement = verif_correct_value(classement, msg_classement)
            while int(classement) in a_classements_list:
                print("Deux joueurs ne peuvent avoir le même classement !")
                classement = input("Entrer le Classement du joueur : ")
            a_classements_list.append(int(classement))

            nb_participants += 1

            choix = input("Ajouter un autre joueur ? Y/N : ")
            #choix = verif_yes_no(choix, msg_ajout_joueur)
            while choix not in ["y", "Y", "n", "N"]:
                print("Saisie incorrete...")
                choix = input("Ajouter un autre joueur ? Y/N : ")

        print("\nNombre de participants au tournoi : {}".format(nb_participants),"\n")

        return a_names_list, a_firstnames_list, a_births_list, a_sexs_list, a_classements_list

    def create_player_dict(players_tuple):
        """
        Création d'une liste de dictionnaires de joueurs
        """
        names_list = players_tuple[0]
        firstnames_list = players_tuple[1]
        births_list = players_tuple[2]
        sexs_list = players_tuple[3]
        classements_list = players_tuple[4]
        
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

    def main():
        pl = Player
        players_lists = pl.create_player_list()
        players_dicts = pl.create_player_dict(players_lists)
        print(players_dicts)
        return players_dicts

        # liste_noms=players[0]
        # liste_prenoms=players[1]
        # liste_dates_naissance=players[2]
        # liste_sexes=players[3]
        # liste_classements=players[4]  

        # for player_attributes in players_dicts:
        #     p = Player(**player_attributes)
        #     print(p.Name)

if __name__=="__main__":
    plyr = Player
    joueur = plyr.main()