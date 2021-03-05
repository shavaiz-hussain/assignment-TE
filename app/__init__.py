""" Top level module

This module:

- Contains create_app()
- Registers extensions
"""

from flask import Flask

# Import config
from config import config_by_name

# Import extensions
from .libraries import bcrypt, cors, db, jwt, ma


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])
    register_libraries(app)
    with app.app_context():
        db.create_all()

    # Register blueprints
    from .auth import auth_bp

    app.register_blueprint(auth_bp)

    from .api import api_bp

    app.register_blueprint(api_bp, url_prefix="/api")

    return app


def register_libraries(app):
    # Registers flask extensions
    db.init_app(app)
    ma.init_app(app)
    jwt.init_app(app)
    bcrypt.init_app(app)
    cors.init_app(app)
