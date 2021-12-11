from config import db


class Mission(db.Document):
    id=db.ObjectId()
    id_people = db.StringField()
    name = db.StringField()
    description = db.StringField()
    model = db.db.StringField()
    parcour =db.StringField()
    surface = db.StringField()
    heurs_vol=db.IntField()

    def to_json(self):
        return {
            "id": self.id,
            "id_people": self.id_people,
            "name": self.name,
            "description": self.description,
            "model": self.model,
            "parcour": self.parcour,
            "surface": self.surface,
            "heurs_vol": self.heurs_vol

        }