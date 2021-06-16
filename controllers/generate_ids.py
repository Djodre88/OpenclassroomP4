import os

os.system("cls")

"""
Creation d'un ID unique pour chaque match
"""
def verif_correct_date(entry, message):
    valid = False
    while not valid:
        entry = input(message)
        try:
            entry = int(entry)
            if len(str(entry))==8:
                entry = str(entry)
                if 1984 <= int(entry[0:4]) <= 2021:
                    if 1 <= int(entry[4:6]) <= 12:
                        if 1 <= int(entry[6:]) <= 31:
                            return entry
                        else:
                            print("Jour incorrect. Veuillez renouveller votre saisie..")
                    else:
                        print("Mois incorrect. Veuillez renouveller votre saisie..")
                else:
                    print("Année incorrecte. Veuillez renouveller votre saisie..")    

            else :
                print("Le format AAAAMMJJ n'est pas respecté. Veuillez à nouveau saisir la date :")        
        except ValueError:
            print("Veuillez saisir des nombres uniquement.")

def verif_correct_value (entry, message):
    valid = False
    while not valid:
        entry = input(message)
        try:
            entry = int(entry)
            if 1 <= entry <= 9:
                entry = "0" + str(entry)
                return entry
                valid = True
            elif entry > 9:
                entry = str(entry)
                return entry
            else :
                print("Vous devez entrer une valeur entière positive.")    
        except ValueError:
            print("Vous devez entrer une valeur entière positive.")

date = -1
tournoi = -1
tour = -1
match = -1

msg_date = "\nsaisir la date au format AAAAMMJJ : "
msg_tournoi = "numéro du tournoi : "
msg_tour = "numéro du tour : "
msg_match = "numéro du match : "

date = verif_correct_date(date, msg_date)
year = date[0:4]
month = date[4:6]
day = date[6:]

nom1 = input("nom du participant1 : ")
nom2 = input("nom du participant2 : ")

tournoi = verif_correct_value(tournoi, msg_tournoi)

tour = verif_correct_value(tour, msg_tour)

match = verif_correct_value(match, msg_match)

ref5 = (year  + month + day  + tournoi  + tour  + match  + "/" + nom1[0:3] + "-" + nom2[0:3])
ref6 = (year + "." + month + "." + day + "/" + tournoi + "." + tour + "." + match + "/" + nom1[0:3] + "-" + nom2[0:3])

print ("\nLa référence du match est : {}\n".format(ref5))
print("ou bien ")
print ("\nLa référence du match est : {}\n".format(ref6))

# ref = (year  + month + day  + tournoi  + tour  + match  + nom1[0:3]  + nom2[0:3])
# ref2 = (year + "-" + month+ "-" + day + "-" + tournoi + "-" + tour + "-" + match + "-" + nom1[0:3] + "-" + nom2[0:3])
# ref3 = (year + "/" + month+ "/" + day + "/" + tournoi + "/" + tour + "/" + match + "/" + nom1[0:3] + "/" + nom2[0:3])
# ref4 = (year + "." + month+ "." + day + "." + tournoi + "." + tour + "." + match + "." + nom1[0:3] + "." + nom2[0:3])

# print ("\nLa référence du match est : {}\n".format(ref))
# print ("\nLa référence du match est : {}\n".format(ref2))
# print ("\nLa référence du match est : {}\n".format(ref3))
# print ("\nLa référence du match est : {}\n".format(ref4))