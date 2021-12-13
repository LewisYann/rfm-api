from config import db


class Mission(db.Document):
    id_people = db.StringField()
    id_mission = db.StringField()
    name = db.StringField()
    description = db.StringField()
    model =  db.StringField()
    parcour =db.StringField()
    surface = db.StringField()
    heurs_vol=db.IntField()

    def to_json(self):
        return {
            "id_people": self.id_people,
            "id_mission": self.id_mission,
            "name": self.name,
            "description": self.description,
            "model": self.model,
            "parcour": self.parcour,
            "surface": self.surface,
            "heurs_vol": self.heurs_vol

        }