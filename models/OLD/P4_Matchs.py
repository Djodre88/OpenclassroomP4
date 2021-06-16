class Matchs:
    def __init__(self):
        pass

    def TriListeJoueurs (une_liste_de_joueurs):
        classements_tri_decroissant = sorted(classements, reverse=True)
        index_tri = []

        for classement in classements_tri_decroissant:
            index = classements.index(classement)
            index_tri.append(index)

        une_liste_joueurs_triee = []    

        for i in index_tri:
            une_liste_joueurs_triee.append(une_liste_de_joueurs[i])
            
        return (une_liste_joueurs_triee)

    def GenererPairesPremierTour (une_liste_de_joueurs_triee):
        moitie_sup = une_liste_de_joueurs_triee[:int(len(une_liste_de_joueurs_triee)/2)]
        moitie_inf = une_liste_de_joueurs_triee[int(len(une_liste_de_joueurs_triee)/2):]
        paires = []
        for msup, minf in zip (moitie_sup, moitie_inf):
            t=(msup, minf)
            paires.append(t)
            # paires.append((msup, minf))            
        return paires

    def main ():
        mtch = Matchs
        liste_joueurs_triee = mtch.TriListeJoueurs(liste_joueurs)
        paires_triees = mtch.GenererPairesPremierTour(liste_joueurs_triee)

        i=1
        for l in liste_joueurs_triee:
            print(i,". ",liste_joueurs_triee[liste_joueurs_triee.index(l)]["Nom"],"| classement :", liste_joueurs_triee[liste_joueurs_triee.index(l)]["Classement"])
            i+=1

        print("\nMatchs Tour n°1 :\n")    
        for pt in paires_triees:
            print((paires_triees)[paires_triees.index(pt)][0]["Nom"],"-",(paires_triees)[paires_triees.index(pt)][1]["Nom"])

if __name__ == "__main__":
    mtch = Matchs
    mtch.main()