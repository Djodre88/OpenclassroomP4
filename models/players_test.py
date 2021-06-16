from tinydb import TinyDB, Query


class Player :
    def __init__(self, name, age):
        self.name = name
        self.age = age

if __name__ == "__main__":
    players_list = []

    for i in range(0,2):
        name = input("name : ")
        age = input("age : ")
        player = Player(name, age)

        serialized_player = {
            "name": player.name,
            "age": player.age
        }
        players_list.append(serialized_player)

    db = TinyDB("db.json")
    Info = Query()

    # tn_table = db.table("tournament")
    players_table = db.table("players")

    # tn_table.update({"nb_tour" : 8}, Info.nb_tour == 4) # remplacer valeur existante dans le JSON

    # tn_table.truncate()
    players_table.truncate()          #clear the first table
    players_table.insert_multiple(players_list)
    # print(vars(players_table)["_name"])

    ser_players = players_table.all()
    print(ser_players)

    # tn_table.update({"players" : players_list})
    # tn_table.insert_multiple(players_list)


    # rsc = tn_table.search(Info.name == "OC CHESS") # Afficher les infos du JSON existant
    # print(rsc[0])
    