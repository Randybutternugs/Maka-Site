from flask import Flask, request, Blueprint, render_template, redirect, url_for, abort
import random
import logging
import requests

views = Blueprint('views', __name__)
error_handlers = Blueprint('error_handlers', __name__)

def get_gif_urls():
    return [url_for('static', filename=f'images/gif{i}.gif') for i in range(1, 4)]

@views.route('/', methods = ['POST', 'GET'])
def home():
    return render_template("homepage.html")

#@views.route('/bday')
#def home():
#    gif_path = random.choice(get_gif_urls())
#    return render_template("makday.html", gif_path=gif_path)


@views.route('/about')
def about():
    return "This is the about page"

# 404 error handler for this blueprint
@error_handlers.app_errorhandler(404)
def not_found(e):
    gif_path = random.choice(get_gif_urls())
    return render_template("404.html", gif_path=gif_path), 404


@views.errorhandler(404)
def page_not_found(e):
    logging.error(f"Internal Server Error: {e}")
    #gif_path = random.choice(get_gif_urls())
    # note that we set the 404 status explicitly
    return render_template("404.html", error=e), 404