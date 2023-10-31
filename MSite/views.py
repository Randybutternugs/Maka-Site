from flask import Flask, request, Blueprint, render_template, redirect, url_for, abort
import random
import logging
import requests

views = Blueprint('views', __name__)
error_handlers = Blueprint('error_handlers', __name__)

def get_gif_urls():
    return [url_for('static', filename=f'images/gif{i}.gif') for i in range(1, 4)]

@views.route('/')
def home():
    return render_template("homepage.html")

#@views.route('/bday')
#def home():
#    gif_path = random.choice(get_gif_urls())
#    return render_template("makday.html", gif_path=gif_path)


@views.route('/about')
def about():
    return "This is the about page"


# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-  |
#  VIEW FOR TRIGGERING ERRORS FOLLOWED BY ERROR HANDLING ROUTES  |
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- \ /

# Make more as needed

@views.route('/error') #Currently set to trigger a 500 error when I input this route
def trigger_forbidden():
    abort(500)

# 404 error handler for this blueprint
@error_handlers.app_errorhandler(404)
def not_found(e):
    gif_path = random.choice(get_gif_urls())
    return render_template("error.html", gif_path=gif_path, error_code=404), 404

# 500 error handler for this blueprint
@error_handlers.app_errorhandler(500)
def not_found(e):
    gif_path = random.choice(get_gif_urls())
    return render_template("error.html", gif_path=gif_path, error_code=500), 500