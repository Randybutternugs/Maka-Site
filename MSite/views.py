from flask import Flask, Blueprint, render_template, redirect, url_for
import random

views = Blueprint('views', __name__)


def get_gif_urls():
    return [url_for('MSite/static/images', filename=f'gif{i}.gif') for i in range(1, 4)]

@views.route('/')
def home():
    return render_template("homepage.html")

#@views.route('/bday')
#def home():
#    gif_path = random.choice(get_gif_urls())
#    return render_template("makday.html", gif_path=gif_path)

@views.errorhandler(404)
def not_found(e):
    gif_path = random.choice(get_gif_urls())
    # note that we set the 404 status explicitly
    return render_template("404.html", gif_path=gif_path), 404

@views.route('/about')
def about():
    return "This is the about page"