from flask import Flask
from app.controller import posts_controller

def create_app():
    app = Flask(__name__)

    posts_controller.init_app(app)

    return app

