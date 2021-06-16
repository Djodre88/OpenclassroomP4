from models.Model import Model

class Player(Model):
    
    def __init__(self, name, firstname, age, sex, elo) -> None:
        super().__init__()
        self.name = name 
        self.firstname = firstname
        self.age = age
        self.sex = sex
        self.elo = elo
        # self.table_name = "players"

    # def save_players(self, serialized_players):    
    #     players_table = super().get_db().table("players")
    #     players_table.truncate()          #clear the first table
    #     players_table.insert_multiple(serialized_players)
    #     return players_table