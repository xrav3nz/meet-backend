from flask.ext.sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_restful import Api

db = SQLAlchemy()
admin = Admin()
api = Api()
