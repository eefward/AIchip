from flask import Flask, redirect, render_template, request, session
from flask_session import Session
import sqlite3

app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

con = sqlite3.connect("downlaod.db", check_same_thread=False)
cur = con.cursor()

@app.route("/", methods=["GET", "POST"])
def home():
  if request.method == "POST":
    ...
  return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)