from flask import Flask 
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


#app.config['SQLALCHEMY_DATABASE_URI'] ="sqlite:///data.db"
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:root@34.71.43.237:3306/gym"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "khanx"

db = SQLAlchemy(app)

from application import routes
