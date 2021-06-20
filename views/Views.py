from other_functions.Validation import Validation


class Views:
    def __init__(self):
        pass

    def display_main_menu(self):
        user_choice = -1
        while (user_choice) not in ['1', '2', '3', '4', '5', '6', '7']:
            print("\n##### OC Chess Tournament #####\n")
            print("1. Create tournament")
            print("2. Load tournament")
            print("3. Register player")
            print("4. Generate matchs")
            print("5. Score updating")
            print("6. Stats")
            print("7. Exit")
            user_choice = input("Enter your choice : ")

        user_choice = int(user_choice)
        # self.user_choice = user_choice

        return user_choice

    def entry_tn_info(self):
        vld = Validation()
        tn_info = {}
        tn_info["name"] = input("Tournament name : ")
        # tn_info["date"] = input("Date (format DDMMYYYY) : ")
        tn_info["date"] = vld.verif_correct_date("Date (format DDMMYYYY) : ")
        tn_info["place"] = input("Location : ")
        tn_info["time"] = input("Time control [Bullet/Blitz/Coup rapide] : ")
        tn_info["desc"] = input("Description : ")

        return tn_info

    def entry_player_info(self):
        name = input("Enter Player NAME : ")
        firstname = input("Enter Player firstname : ")
        age = input("Enter Player age : ")
        sex = input("Enter Player sex : ")
        elo = input("Enter Player ELO : ")

        return name, firstname, age, sex, elo

    def continue_reg(self, event):
        choice = input("Add another {} ? (Y/N) :".format(event))

        while choice not in ["y", "Y", "n", "N"]:
            print("Choix incorrect. Y = Yes / N = No")
            choice = input("Add another {} ? (Y/N) :".format(event))
        self.choice = choice
        return self.choice

    def reset_players(self):
        reset = input("Erase existant players ? (Y/N) :")

        while reset not in ["y", "Y", "n", "N"]:
            print("Choix incorrect. Y = Yes / N = No")
            reset = input("Erase existant playrs ? (Y/N) :")
        self.reset = reset
        return self.reset

    def reset_tn(self):
        reset = input("Erase existant tournament ? (Y/N) :")

        while reset not in ["y", "Y", "n", "N"]:
            print("Choix incorrect. Y = Yes / N = No")
            reset = input("Erase existant tournament ? (Y/N) :")
        self.reset = reset
        return self.reset

    def entry_scores(self, matchs_list, nb_round_max):
        scores_list = []
        vld = Validation()
        print("\nWin : 1, Draw : 0.5, Lose : 0")
        for i in range(0, nb_round_max):
            score = []
            print("\nEntrer le résultat du match {} : {}".format(i+1, matchs_list[i][0]))
            message = "\nScore de {} : ".format(matchs_list[i][0][0])
            score_joueur1 = vld.verif_score(message)
            score.append(score_joueur1)

            if score_joueur1 == 1:
                score_joueur2 = 0
            elif score_joueur1 == 0.5:
                score_joueur2 = 0.5
            else:
                score_joueur2 = 1

            score.append(score_joueur2)
            score = [score_joueur1, score_joueur2]
            scores_list.append(score)
        return scores_list

    def display_tn_info(self, tn_table, pl_table):
        i = 1
        print("Liste des tournois disponibles : \n")
        for tn in tn_table:
            print(". {}".format(tn["name"]))
        # print("\n")
        rsc = input("\nTournoi recherhé : ")
        for tn in tn_table:
            if rsc in tn["name"]:
                print("\nNom du tournoi : {}".format(tn["name"]))
                print("Date : {}".format(tn["date"]))
                print("Lieu : {}".format(tn["place"]))
                print("Time control : {}".format(tn["time"]))
                print("Nombre de tours : {}\n".format(tn["nb_tour"]))
                ser_players = pl_table.all()
                ser_players = sorted(ser_players, key=lambda s: s["name"])
                print("Liste des participants par ordre alphabétique : \n")
                print("NOM \t\tPrénom \t\tAge \t\tSexe \t\tELO\n--- \t\t------ \t\t--- \t\t---- \t\t---")
                for ser_pl in ser_players:
                    if len(ser_pl["name"]) > 6:
                        print("{} \t{} \t\t{} \t\t{} \t\t{}".format(ser_pl["name"], ser_pl["firstname"], ser_pl["age"], ser_pl["sex"], ser_pl["elo"]))
                    else:
                        print("{} \t\t{} \t\t{} \t\t{} \t\t{}".format(ser_pl["name"], ser_pl["firstname"], ser_pl["age"], ser_pl["sex"], ser_pl["elo"]))              
                
            else:
                print("\nTournoi non trouvé...")

    def display_classement(self, updated_classement):
        i = 0
        for player in updated_classement:
            i += 1
            print("{}. {}".format(i, player))

    def display_matchs(self, matchs, round_nb):
        print("\n-- Matchs Round {} : \n".format(round_nb))
        i = 0
        for match in matchs:
            i += 1
            print("{}. {} vs {} | pts before match : {}".format(i, match[0][0], match[0][1], match[1]))

    def press_to_continue(self):
        input("\nAppuyez sur une touche pour revneir au menu précédent... >>>")


if __name__ == "__main__":
    views = Views()
    views.display_main_menu()
    tn_info = views.entry_tn_info()
    print(tn_info)
