from application import app
from flask import render_template


@app.route("/movie")
def movie():
    return render_template("movie.html")
