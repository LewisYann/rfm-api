from config import db


class Setting(db.Document):
    id=db.ObjectId()
    id_people = db.StringField()
    liste_wifi = db.ListField()
    manette_list = db.ListField()
    authorization = db.IntField()
    def to_json(self):
        return {
            "id": self.id,
            "id_people": self.id_people,
            "list_wifi": self.liste_wifi,
            "manette_list": self.manette_list,
            "authorization": self.authorization,

        }