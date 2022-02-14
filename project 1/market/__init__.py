from flask import Flask,render_template,url_for
from flask_sqlalchemy import SQLAlchemy



app=Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///market.db"
app.config["SECRET_KEY"]="9d06d9361b3ef71696b0ff64"
db=SQLAlchemy(app)

from market import routes