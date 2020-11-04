from flask import Flask 
from config import config_options
from flask_login import LoginManager
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_mail import Mail

db = SQLAlchemy()
bootstap = Bootstrap()
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'
mail = Mail()
bootstrap = Bootstrap()

login_manager = LoginManager()

def create_app(config_name):
    '''
    This function loads the correct configurations from config.py and instance/config.py
    also it creates a db object
    '''
    app = Flask(__name__)


    # Creating the app configurations
    from flask_bootstrap import Bootstrap
    app.config.from_object(config_options[config_name])
    

    db.init_app(app)
    bootstrap.init_app(app)
    mail.init_app(app)

    login_manager.init_app(app)
    login_manager.login_message = "You must be logged in to access this page."
    # login_manager.login_view = "auth.login"

    
    # Register Home Blueprint
    from app import models
    
    from .home import home as home_blueprint
    app.register_blueprint(home_blueprint)

    from .admin import admin as admin_blueprint
    app.register_blueprint(admin_blueprint, url_prefix='/admin')  ##dashboard

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)




        
    return app

