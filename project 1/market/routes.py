from market import app
from flask import render_template,url_for,redirect
from market.models import Item,User
from market.forms import RegisterForm
from market import db
@app.route("/")
@app.route("/home")
def home_page():
    return render_template("home.html",title="home")


@app.route("/market")
def market_page():
    items=Item.query.all()
    return render_template("market.html",title="market")

@app.route("/register",methods=["GET","POST"])
def register_page():
    form=RegisterForm()
    if form.validate_on_submit():
        user_profile=User(username=form.username.data, 
                          email_address=form.email.data,
                          password_hash=form.password.data)
        db.session.add(user_profile)
        db.session.commit()
        return redirect(url_for("home_page"))
    return render_template("register.html",title="register",form=form)    