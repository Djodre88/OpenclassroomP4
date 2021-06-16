from models.Model import Model
from views.Views import Views
from models.Tournament import Tournament
from models.Players import Player
from models.Round import Round
# from models.Matchs import Matchs



class Controller(Model):
    def __init__(self):
        super().__init__()
        self.round_nb = 0
        self.nb_round_max = 4      

    def main_menu(self):
        main_view = Views()
        rnd = Round()
        self.all_rounds = []
        self.user_choice = main_view.display_main_menu()
        if self.user_choice == 1:
            """
            Create tournament
            """
            print("\n-- Tournament creation --\n")
            # reset_choice = main_view.reset_tn()    # Clear players list
            # if reset_choice == ("y" or "Y"):
            #     reset = True
            # else:
            #     reset = False

            tn_info = main_view.entry_tn_info()
            self.tn = self.create_tournament(tn_info, reset = True)
            main_view.press_to_continue
            self.main_menu()

        elif self.user_choice == 2:
            print("\nLoad tournament...")
            self.serialized_players = self.load_players()
            self.tn = self.load_tournament()
            main_view.press_to_continue()
            self.main_menu()

        elif self.user_choice == 3:
            """
            Register Player
            """
            self.serialized_players = self.serialize_players()
            players_table = self.save_players(self.serialized_players)

            ser_players = players_table.all()
            print(ser_players)

            self.add_players_to_tn(self.serialized_players)
            self.main_menu()

        elif self.user_choice == 4:
            """
            Generate matchs
            """
            disp = print("\nGenerate matchs...")
            self.round_nb += 1
            if self.round_nb == 1:
                disp
                sorted_players = rnd.tri_premier_tour(self.serialized_players)
                self.matchs = rnd.generer_matchs_premier_tour(sorted_players)
            elif self.round_nb > self.nb_round_max:
                print("\nNombre de rounds atteint ! \n\n-- FIN DE LA PARTIE --\n\nRetour au Menu Principal...\n")
                self.main_menu()                
            else:
                disp
                self.matchs = rnd.generate_next_round(self.updated_classement)

            main_view.display_matchs(self.matchs, self.round_nb)
            main_view.press_to_continue()
            self.main_menu()

        elif self.user_choice == 5:
            """
            Score updating
            """
            if self.round_nb > self.nb_round_max:
                print("\nNombre de rounds atteint !\nClassement final : \n")

            else:
                print("Score updating...\n")
                self.scores = main_view.entry_scores(self.matchs, self.nb_round_max)
                self.rounds = rnd.update_rounds(self.matchs, self.scores)
                self.all_rounds.append(self.rounds)
                self.add_rounds_to_tn(self.all_rounds)
                self.save_round(self.rounds)
                self.updated_classement = rnd.update_classement(self.matchs, self.scores)
                print("\nClassement à l'issue du round {} : \n".format(self.round_nb))
            main_view.display_classement(self.updated_classement)
            main_view.press_to_continue()
            self.main_menu()

        elif self.user_choice == 6:
            """
            Stats
            """
            info_choice = input("\n1. Afficher les infos du tournoi\n2. Afficher les infos de joueurs\n\nChoix : ")
            info_choice = int(info_choice)
            if info_choice == 1:
                try:
                    print("\n-- Tournament info --\n")
                    # aa = self.tn
                    # print(vars(aa)["name"])
                    tn_table = super().get_db().table("tournament")
                    to_find = input("Nom du tournoi recherché : ")
                    rsc = tn_table.search(super().get_info().name == to_find) # Afficher les infos du JSON existant
                    print("\n", rsc, "\n")                    
                except AttributeError:
                    print("\nAucun tournoi enregistré..\n\n")
                main_view.press_to_continue()
                self.main_menu()

            elif info_choice == 2:
                try:
                    print("\n-- Players info --\n")
                    pl_table = super().get_db().table("players")
                    to_find = input("Nom du Joueur recherché : ")
                    rsc = pl_table.search(super().get_info().name == to_find) # Afficher les infos du JSON existant
                    print("\n", rsc, "\n")
                    back = input("Appuyez sur une touche pour revenir au menu principal >>>\n")
                except AttributeError:
                    print("Aucun joueur enregistré..\n\n")
                    back = input("Appuyez sur une touche pour revenir au menu principal >>>")
                self.main_menu()

        elif self.user_choice == 7:
            """
            Exit
            """
            print("\nFin du programme...\n")

    def create_tournament(self, tn_info, reset):
        tn = Tournament(
            tn_info["name"],
            tn_info["date"],
            tn_info["place"],
            tn_info["desc"],
            tn_info["time"],
        )
        tn.save_tn(reset)
        return tn

    def create_player(self):       
        main_view = Views()     
        pl_infos = main_view.entry_player_info()
        name = pl_infos[0]
        firstname = pl_infos[1]
        age = pl_infos[2]
        sex = pl_infos[3]
        elo = pl_infos[4]
        player = Player(name, firstname, age, sex, elo)
        return player
  
    def serialize_players(self, nb_pl_max = 8):
        serialized_players = []
        i=0
        for i in range (0, nb_pl_max):
            player = self.create_player()        
            serialized_player = {
                "name": player.name,
                "firstname": player.firstname,
                "age": player.age,
                "sex": player.sex,
                "elo": player.elo
                }
            if i == 0:
                print("\n 1 joueur enregistré\n")
            else:
                print("\n{} joueurs enregistrés\n".format(i+1))
            serialized_players.append(serialized_player)
            i+=1
        return serialized_players
        
    def save_players(self, serialized_players):    
        players_table = super().get_db().table("players")
        players_table.truncate()          #clear the first table
        players_table.insert_multiple(serialized_players)
        return players_table        

    def add_players_to_tn(self, serialized_players):
        tn_table = super().get_db().table("tournament")
        tn_table.update({"players" : serialized_players})
            
    def save_round(self, rounds):
        round_table = super().get_db().table("rounds")
        round_table.insert({"rounds" : rounds})

    def add_rounds_to_tn(self, rounds):
        tn_table = super().get_db().table("tournament")
        tn_table.update({"rounds" : rounds})

    
    def load_players(self):
        players_table = super().get_db().table("players")
        serialized_players = players_table.all()
        return serialized_players

    def load_tournament(self):
        tn_table = super().get_db().table("tournament")
        tn = tn_table.all()
        return tn

if __name__ == "__main__":
    ctrl = Controller()
    ctrl.main_menu()
