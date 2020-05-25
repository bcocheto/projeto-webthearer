from flask import Flask
import os

app = Flask(__name__, static_folder=os.path.abspath("app/view/static"),
            template_folder=os.path.abspath("app/view/templates"))
