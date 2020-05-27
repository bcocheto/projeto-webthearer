from application import app
from flask.templating import render_template


@app.route("/sub_category")
def sub_category():
    return render_template("sub_category.html")
