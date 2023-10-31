from flask import Flask, Blueprint
from .constants import SITE_SECRET

def create_app():
    app = Flask(__name__, static_folder="static")
    from .views import bp as my_blueprint_bp

    #CHANGE THIS LATER
    app.config['SECRET_KEY'] = SITE_SECRET
    #CHANGE THIS LATER

    from .views import views
    app.register_blueprint(my_blueprint_bp)
    app.register_blueprint(views, url_prefix='/')
    
    return app