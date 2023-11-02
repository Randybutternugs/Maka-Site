from flask import Flask, Blueprint, render_template, redirect, url_for
import random

auth = Blueprint('auth', __name__)

#def get_gif_urls():
#    return [url_for('static/images', filename=f'gif{i}.gif') for i in range(1, 4)]

@auth.route('/login')
def login():
    return "<p>Login</p>"

@auth.route('/logout')
def logout():
    return "<p>logout<p>"

@auth.route('/sign-up')
def sign_up():
    return "<p> Sign Up</p>"

#@auth.errorhandler(404)
#def page_not_found(e):
#    gif_path = random.choice(get_gif_urls())
#    # note that we set the 404 status explicitly
#    return render_template("404.html", gif_path=gif_path), 404