#!/usr/bin/python3
from flask import Blueprint, render_template


app = Blueprint(__name__)
@app.route("/test",methode = ["GET","POST"])
def test():
    return render_template("base.html")