from flask import Flask
import os
from application.controller import home_controller

app = Flask(
    __name__,
    static_folder=os.path.abspath("app/view/static"),
    template_folder=os.path.abspath("app/view/templates"),
)
