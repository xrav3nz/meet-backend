import os
import logging.handlers

from flask import Flask, render_template

from config import config
from .extensions import db, admin
from .admin import admin_bp
from .api import api_bp


def create_app(config_name):

    app = Flask(__name__)

    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    configure_blueprints(app)
    configure_extensions(app)
    configure_errorhandlers(app)
    configure_logging(app)
    configure_signals(app)

    return app

def configure_extensions(app):

    # Flask-SQLAlchemy
    db.init_app(app)

    # Flask-Admin
    admin.init_app(app)

def configure_blueprints(app):
    app.register_blueprint(admin_bp)
    app.register_blueprint(api_bp)

def configure_errorhandlers(app):
    pass

def configure_logging(app):

    logs_folder = os.path.join(app.root_path, os.pardir, "logs")
    formatter = logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s '
        '[in %(pathname)s:%(lineno)d]')

    info_log = os.path.join(logs_folder, app.config['INFO_LOG'])

    info_file_handler = logging.handlers.RotatingFileHandler(
        info_log,
        maxBytes=100000,
        backupCount=10
    )

    info_file_handler.setLevel(logging.INFO)
    info_file_handler.setFormatter(formatter)
    app.logger.addHandler(info_file_handler)

    error_log = os.path.join(logs_folder, app.config['ERROR_LOG'])

    error_file_handler = logging.handlers.RotatingFileHandler(
        error_log,
        maxBytes=100000,
        backupCount=10
    )

    error_file_handler.setLevel(logging.ERROR)
    error_file_handler.setFormatter(formatter)
    app.logger.addHandler(error_file_handler)

def configure_signals(app):
    pass