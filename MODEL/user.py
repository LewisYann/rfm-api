from config import db


class User(db.Document):
    id=db.ObjectId()
    login = db.StringField()
    password = db.StringField()
    idUser = db.StringField()
    is_active = db.Boolean()
    is_authorization = db.Integer()
    token = db.StringField()
    refresh_token = db.StringField()
    def to_json(self):
        return {
            "name": self.name,
            "login": self.login,
            "password": self.password,
            "idUser": self.idUser,
            "is_active": self.is_active,
            "is_authorization": self.is_authorization,
            "token": self.token,
            "refresh_token": self.refresh_token,
        }