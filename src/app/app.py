from flask import Flask
from flask_sqlalchemy import SQLAlchemy

application = Flask(
    import_name=__name__,
    template_folder='../templates',
    static_folder='../static',
)
# set up the database location
application.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mapData.db'
application.config['SECRET_KEY'] = '126059605bb3b26263f9a46e'
# create an database object based on current application configuration
db = SQLAlchemy(application)
