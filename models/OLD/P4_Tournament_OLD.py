#import entry_validation*

class Tournament:

    def __init__(self, **tournament_dict):
        for attrs_name, attrs_value in tournament_dict.items():
            setattr(self, attrs_name, attrs_value)
          
    # def create_tournament_list (self):
    #     """
    #     Saisie manuelle du tournoi
    #     """
    #     self.a_tn_name_list = []
    #     self.a_tn_location_list = []
    #     self.a_tn_date_list = []
    #     self.a_tn_rounds_list = []
    #     self.a_tn_time_control_list = []
    #     self.a_tn_description_list = []
    #     self.a_tn_players_list = []

    #     choice = "Y"

    #     while choice in ["y", "Y"]:            
    #         tn_name = input("Nom du tournoi : ")
    #         self.a_tn_name_list.append(tn_name)

    #         tn_location = input("Lieu du tournoi : ")
    #         self.a_tn_location_list.append(tn_location)

    #         tn_date = input("Date du début du tournoi :")
    #         self.a_tn_date_list.append(tn_date)

    #         # int(tn_rounds) = input("Nombre de rounds :")

    #         tn_rounds = input("Nombre de rounds : ")
    #         self.a_tn_rounds_list.append(tn_rounds)

    #         tn_time_control = input("Time control [Bullet/Blitz/Coup Rapide] : ")
    #         tn_time_control = tn_time_control.capitalize()

    #         while tn_time_control not in ["Bullet", "Blitz", "Coup Rapide"]:
    #             print("Saisie incorrecte. Veuillez à nouveau saisir le Time Control en respectant l'orthographe.. ")
    #             tn_time_control = input("Time control [Bullet/Blitz/Coup Rapide] : ")
    #             tn_time_control = tn_time_control.capitalize()
                
    #         self.a_tn_time_control_list.append(tn_time_control)
            
    #         tn_description = input("Description du tournoi : ")
    #         self.a_tn_description_list.append(tn_description)

    #         tn_players = []

    #         choice = input("Voulez-vous créer un autre tournoi ? Y/N :")
    #         while choice not in ["y", "Y", "n", "N"]:
    #             print ("Saisie incorrete")
    #             choice = input("Voulez-vous créer un autre tournoi ? Y/N :")
    #     return self.a_tn_name_list , self.a_tn_location_list , self.a_tn_date_list , self.a_tn_rounds_list , self.a_tn_time_control_list , self.a_tn_description_list ,
    #     self.a_tn_players_list
    
    # def create_tournament_dict (self, tn_tuple):

    #     """
    #     creation d'une liste de dictionnaires de tournois
    #     """
    #     tn_name_list = tn_tuple[0]
    #     tn_date_list = tn_tuple[1]
    #     tn_rnd_list  = tn_tuple[2]
    #     tn_time_ctrl_list = tn_tuple[3]
    #     tn_desc_list = tn_tuple[4]
    #     tn_players_list = tn_tuple[5]
    #     self.tn_dict_list = []
    #     for name, date, rnd, time_ctrl, desc, pl in zip (tn_name_list, tn_date_list, tn_rnd_list, tn_time_ctrl_list, tn_desc_list, tn_players_list):
    #         dict_tn = {
    #             'Name': name,
    #             'Date': date,
    #             'Round_Nb': rnd,
    #             'Time_Control': time_ctrl,
    #             'Description': desc,
    #             'Players': pl
    #         }
    #         self.tn_dict_list.append(dict_tn)
    #     return self.tn_dict_list

    # def main(self):
    #     tn = Tournament()
    #     tn_lists = tn.create_tournament_list()
    #     self.tn_dicts = tn.create_tournament_dict(tn_lists)
    #     print (self.tn_dicts)
    #     return self.tn_dicts

if __name__=="__main__":
    tn = Tournament()
    tn.main()