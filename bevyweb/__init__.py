from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__,instance_relative_config=True)

app.config.from_pyfile('config.py', silent=False)

db = SQLAlchemy(app)

from bevyweb import userroute,adminroute