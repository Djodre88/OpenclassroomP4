from models.Model import Model


class Tournament(Model):

    def __init__(self, name, date, place, desc, time, nb_tour=4) -> None:
        super().__init__()
        self.name = name
        self.date = date
        self.place = place
        self.desc = desc
        self.time = time
        self.nb_tour = nb_tour
        self.players = []
        self.round = []
        self.table_name = "tournament"


    def save_tn(self, reset=True):
        tn_table = super().get_db().table(self.table_name)
        if reset:
            tn_table.truncate()  # clear the table first
        to_ser = self.__dict__
        del to_ser["db"]
        del to_ser["Info"]
        tn_table.insert(to_ser)
        
        return tn_table


    # def save_pl(self, players_list):
        # tn_table = super().get_db().table("tournament")
        # tn_table.update({"players" : players_list})
    def save_pl(self, serialized_players):
        players_table = super().get_db().table("players")
        players_table.truncate()
        players_table.insert_multiple(serialized_players)


if __name__ == "__main__":
    tn = Tournament()
    tn.save_tn()
    liste = ["A", "B"]
    tn.save_pl(liste)