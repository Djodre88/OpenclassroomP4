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
        self.user_choice = user_choice

        return self.user_choice

    def entry_tn_info(self):
        tn_info = {}
        tn_info["name"] = input("Tournament name : ")
        tn_info["date"] = input("Date (format DDMMYYYY) : ")
        tn_info["place"] = input("Location : ")
        tn_info["time"] = input("Time control [Bullet/Blitz/Coup rapide] : ")
        tn_info["desc"] = input("Description : ")

        return tn_info

    def entry_player_info(self):       
        name = input("Enter Player NAME : ")
        firstname = input("Enter Player firstname : ")
        age = input("Enter Player age : ")
        sex = input("Enter Player sex : ")
        elo  = input("Enter Player ELO : ")

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

    def entry_scores(self, matchs_list):
        scores_list = []
        vld = Validation()
        for i in range(0,4):        
            score =[]        
            print ("Entrer le résultat du match {} : {}".format(i+1, matchs_list[i][0]))
            print("\nW : 1, D : 0.5, L : 0\n")
            message = "Score de {} : ".format(matchs_list[i][0][0])
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

if __name__ == "__main__":
    views = Views()
    views.display_main_menu()
    tn_info = views.entry_tn_info()
    print(tn_info)
