from flask import Flask, redirect, render_template, request, session
from flask_session import Session
import sqlite3

from functions import create_db

app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

con = sqlite3.connect("downlaod.db", check_same_thread=False)
cur = con.cursor()
create_db()

@app.route("/", methods=["GET", "POST"])
def home():
  data = cur.execute("SELECT * FROM downloads")
  if request.method == "POST":
    name = request.form.get("name")
    desc = request.form.get("desc")

    cur.execute("INSERT INTO downloads (name, description) VALUES (?, ?)", (name, desc))
    con.commit()
  return render_template("index.html", data=data)

if __name__ == '__main__':
    app.run(debug=True)