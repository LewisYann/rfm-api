from config import db


class User(db.Document):
    login = db.StringField()
    password = db.StringField()
    idUser = db.StringField()
    people = db.ListField()
    is_active = db.BooleanField()
    authorization = db.IntField()
    token = db.StringField()
    refresh_token = db.StringField()
    def to_json(self):
        return {
            "login": self.login,
            "password": self.password,
            "idUser": self.idUser,
            "people": self.people,
            "is_active": self.is_active,
            "authorization": self.authorization,
            "token": self.token,
            "refresh_token": self.refresh_token,
        }