from config import db


class User(db.Document):
    user_id = db.Inter
    name = db.StringField()
    email = db.StringField()

    def to_json(self):
        return {
                "user_id":
                "name": self.name,
                "email": self.email
                }