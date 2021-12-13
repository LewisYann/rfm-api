from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_mongoengine import MongoEngine, MongoEngineSessionInterface
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config['CORS_HEADERS'] = 'Content-Type'
app.config['SECRET_KEY'] = 'test'
CORS(app, resources={
    r'/*': {
        'origins': '*'
    }
})
app.config['DEBUG_TB_PANELS'] = ['flask_mongoengine.panels.MongoDebugPanel']
app.config['MONGODB_SETTINGS'] = {
    'db': 'rfm',
    'host': '127.0.0.1',
    'port': 27017
}
db = MongoEngine()
toolbar = DebugToolbarExtension(app)

app.session_interface = MongoEngineSessionInterface(db)


db.init_app(app)

