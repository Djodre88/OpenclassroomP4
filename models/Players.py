from models.Model import Model


class Player(Model):

    def __init__(self, name, firstname, age, sex, elo) -> None:
        super().__init__()
        self.name = name
        self.firstname = firstname
        self.age = age
        self.sex = sex
        self.elo = elo
