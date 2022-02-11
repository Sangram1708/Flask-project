from turtle import title
from flask import Flask,render_template,url_for

app=Flask(__name__)
@app.route("/")
@app.route("/home")
def home_page():
    return render_template("home.html",title="home")


@app.route("/market")
def market_page():
    return render_template("market.html",title="market")

    
if __name__=="__main__":
    app.run(debug=True)    