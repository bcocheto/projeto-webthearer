from application import app
from flask.templating import render_template


@app.route("/category")
def category():
    return render_template("category.html")
