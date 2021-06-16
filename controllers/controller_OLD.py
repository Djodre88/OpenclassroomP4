from models.Model import Model
from views.Views import Views
from models.Tournament import Tournament
from models.Players import Player
from models.Round import Round
# from models.Matchs import Matchs
from other_functions.entry_validation import *


class Controller(Model):
    def __init__(self):
        super().__init__()
        # nb_players = 0
        pass

    def main_menu(self):
        main_view = Views()
        user_choice = main_view.display_main_menu()
        if user_choice == 1:
            """
            Create tournament
            """
            print("\n-- Tournament creation --\n")
            reset_choice = main_view.reset_tn()    # Clear players list
            if reset_choice == ("y" or "Y"):
                reset = True
            else:
                reset = False

            tn_info = main_view.entry_tn_info()
            self.tn = self.create_tournament(tn_info, reset)
            self.main_menu()

        if user_choice == 2:
            """
            Register Player
            """
            # reset_choice = main_view.reset_players()    # Clear players list
            # if reset_choice == ("y" or "Y"):
            #     reset = True
            # else:
            #     reset = False
            tn_table = super().get_db().table("tournament")
            tn_info = tn_table.search(super().get_info().name == "OC CHESS")
            tn_info = tn_info[0]
            players_list = []

            continue_choice = "y"
            print("\n -- Player registration --\n")

            player_info = main_view.entry_player_info()
            ser_pl = self.register_player(player_info)
            # players_list.append(ser_pl)
            players_list.append(player_info)
            continue_choice = main_view.continue_reg("Player")

            while continue_choice == ("y" or "Y"):
                print("\n -- Player registration --\n")
                player_info = main_view.entry_player_info()
                ser_pl = self.register_player(player_info)
                # players_list.append(ser_pl)
                players_list.append(player_info)
                continue_choice = main_view.continue_reg("Player")

            # self.add_players_to_tn(tn_info, players_list)
            self.add_players_to_tn(tn_info, ser_pl)
            self.main_menu()

        # if user_choice == 3:
        #     """
        #     Link player - tournament
        #     """
        #     print("\n-- Link Player - Tournament --\n")
        #     # def players_to_tn(self, players_dict, tn_dict):

        if user_choice == 3:
            """
            Generate matchs
            """
            print("Generate matchs...\n")
            # def match_generation()

        if user_choice == 4:
            """
            Score updating
            """
            print("Score updating...\n")

        if user_choice == 5:
            """
            Stats
            """
            info_choice = input("\n1. Afficher les infos du tournoi\n2. Afficher les infos de joueurs\n\nChoix : ")
            info_choice = int(info_choice)
            if info_choice == 1:
                try:
                    print("\n-- Tournament info --\n")
                    aa = self.tn
                    print(vars(aa)["name"])
                    back = input("Appuyez sur une touche pour revenir au menu principal >>>")
                    self.main_menu()
                except AttributeError:
                    print("Aucun tournoi enregistré..\n\n")
                    back = input("Appuyez sur une touche pour revenir au menu principal >>>")
                    self.main_menu()
            elif info_choice == 2:
                try:
                    print("\n-- Players info --\n")
                    pl_info = self.player
                    print(vars(pl_info))
                    back = input("Appuyez sur une touche pour revenir au menu principal >>>")
                    self.main_menu()
                except AttributeError:
                    print("Aucun joueur enregistré..\n\n")
                    back = input("Appuyez sur une touche pour revenir au menu principal >>>")
                    self.main_menu()

        elif user_choice == 7:
            """
            Exit
            """
            print("Fin du programme...")

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

    def register_player(self, player_info):
        player = Player(
            player_info["name"],
            player_info["firstname"],
            player_info["age"],
            player_info["sex"],
            player_info["ELO"]
        )
        return player

    def add_players_to_tn(self, tn_info, players_list):
        tn = Tournament(
            tn_info["name"],
            tn_info["date"],
            tn_info["place"],
            tn_info["desc"],
            tn_info["time"],
        )
        tn.save_pl(players_list)
            

        
if __name__ == "__main__":
    ctrl = Controller()
    ctrl.main_menu()
