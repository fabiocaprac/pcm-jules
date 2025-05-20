# backend/app/__init__.py
from flask import Flask
import os
# Ensure this import is correct based on file location
from .config import Config 
from .database import init_app_db 

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    init_app_db(app)

    from .routes import main_bp
    app.register_blueprint(main_bp)
    
    return app
