from config import db


class Missions(db.Document):
    id=db.ObjectId()
    id_people = db.StringField()
    name = db.StringField()
    description = db.StringField()
    model = db.db.StringField()
    parcour =db.StringField()
    surface = db.StringField()

    def to_json(self):
        return {
            "id": self.id,
            "id_people": self.id_people,
            "name": self.name,
            "description": self.description,
            "model": self.model,
            "parcour": self.parcour,
            "surface": self.surface

        }