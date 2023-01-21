from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from config.database import Config

app = Flask(__name__)
app.config.from_object(Config)
api = Api(app)

db = SQLAlchemy(app)

from api import routes