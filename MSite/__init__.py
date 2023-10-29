from flask import Flask
from .constants import SITE_SECRET

def create_app():
    app = Flask(__name__, static_folder="static")

    #CHANGE THIS LATER
    app.config['SECRET_KEY'] = SITE_SECRET
    #CHANGE THIS LATER

    from .views import views

    app.register_blueprint(views, url_prefix='/')

    return app