from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_mongoengine import MongoEngine

app = Flask(__name__)
app.config['CORS_HEADERS'] = 'Content-Type'
app.config['SECRET_KEY'] = 'test'
CORS(app, resources={
    r'/*': {
        'origins': '*'
    }
})
app.config['MONGODB_SETTINGS'] = {
    'db': 'your_database',
    'host': 'localhost',
    'port': 27017
}
db = MongoEngine()
db.init_app(app)



# create the DB on demand
@app.before_first_request
def create_tables():
    db.create_all()