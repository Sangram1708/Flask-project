from market import app
from flask import render_template,url_for
from market .models import Item
@app.route("/")
@app.route("/home")
def home_page():
    return render_template("home.html",title="home")


@app.route("/market")
def market_page():
    items=Item.query.all()
    return render_template("market.html",title="market")