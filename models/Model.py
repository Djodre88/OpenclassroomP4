from tinydb import TinyDB, Query


class Model:
    def __init__(self):
        self.db = TinyDB("db.json")
        self.Info = Query()

    def get_db(self):
        return self.db

    def get_info(self):
        return self.Info


if __name__ == "__main__":
    md = Model()
    md.get_db()
    md.get_info()
