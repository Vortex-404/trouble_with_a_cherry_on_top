from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
CORS(app)

# Corrected the typo in SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///new.db'

# Corrected the typo in SQLALCHEMY_TRACK_MODIFICATIONS
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


