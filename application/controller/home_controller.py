from application import app
from flask import render_template, current_app
from application.model.dao.category_dao import Category_DAO


@app.route("/")
@app.route("/home")
def home():

    return render_template(
        "home.html", categories=current_app.config["categories"].getListCategory()
    )
