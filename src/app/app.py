from flask import Flask
# from src.app.config import Config
from flask_sqlalchemy import SQLAlchemy

application = Flask(
    import_name=__name__,
    template_folder='../templates',
    static_folder='../static',
)
application.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mapData.db'
application.config['SECRET_KEY'] = '126059605bb3b26263f9a46e'
db = SQLAlchemy(application)
# application.config.from_object(Config)
# db = SQLAlchemy(application)
