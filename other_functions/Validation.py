class Validation:
    """
    Ensemble des fonctions permettant la vérification des différentes saisies
    """
    def __init__(self):
        pass

    def verif_correct_date(self, message):
        """
        Saisie de la Date au format AAAAMMJJ
        """
        valid = False
        while not valid:
            entry = input(message)
            try:
                entry = int(entry)
                if len(str(entry)) == 7:
                    entry = '0'+str(entry)
                    valid = True
                elif len(str(entry)) == 8:
                    entry = str(entry)
                    valid = True
                else:
                    print("Le format DDMMYYYY n'est pas respecté. Veuillez à nouveau saisir la date :")                    
                if valid == True:
                    if 1984 <= int(entry[4:]) <= 2021:
                        if 1 <= int(entry[2:4]) <= 12:
                            if 1 <= int(entry[0:2]) <= 31:
                                valid = True
                                return entry
                            else:
                                print("Jour incorrect. Veuillez renouveller votre saisie..")
                        else:
                            print("Mois incorrect. Veuillez renouveller votre saisie..")
                    else:
                        print("Année incorrecte. Veuillez renouveller votre saisie..")
            except ValueError:
                print("Veuillez saisir des nombres uniquement.")

    def verif_correct_value(self, message):
        """
        Saisie des numéros de tournoi, tour et matchs
        """
        valid = False
        while not valid:
            entry = input(message)
            try:
                entry = int(entry)
                if 1 <= entry <= 9:
                    entry = "0" + str(entry)
                    valid = True
                    return entry
                elif entry > 9:
                    entry = str(entry)
                    return entry
                else:
                    print("Vous devez entrer une valeur entière positive.")
            except ValueError:
                print("Vous devez entrer une valeur entière positive.")

    def verif_sex(self, message):
        entry = input(message)
        while entry not in ["h", "H", "f", "F"]:
            print("Invalid sex. ")
            entry = input(message)
        return entry

    def verif_yes_no(self, message):
        entry = input(message)
        while entry not in ["y", "Y", "n", "N"]:
            print("Incorrect choice. Please answer by Yes(Y) or No(N)..")

    def verif_score(self, message):
        valid = False
        while not valid:
            entry = input(message)
            if entry in ["0", "1"]:
                entry = int(entry)
                valid = True
                return entry
            elif entry == "0.5":
                entry = float(entry)
                valid = True
                return entry
            else:
                try:
                    entry = float(entry)
                    print("\nRappel :\nWin : 1, Draw : 0.5, Lose : 0")
                except ValueError:
                    print("\nVeuillez entrer un score valide")
