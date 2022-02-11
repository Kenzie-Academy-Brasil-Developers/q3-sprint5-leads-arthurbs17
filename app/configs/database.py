from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from app.configs import envs


db = SQLAlchemy()

def init_app(app: Flask):

    envs.init_app(app)

    db.init_app(app)
    app.db = db