from flask import Flask, Blueprint
from .constants import SITE_SECRET

def create_app():
    app = Flask(__name__, static_folder="static")
    # Import the error handlers blueprint and views blueprint
    from .views import error_handlers
    from .views import views
 
    #CHANGE THIS LATER
    app.config['SECRET_KEY'] = SITE_SECRET
    #CHANGE THIS LATER

    # Register blueprints
    app.register_blueprint(error_handlers)
    app.register_blueprint(views, url_prefix='/')
    
    return app