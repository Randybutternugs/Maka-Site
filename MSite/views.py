from flask import Flask, request, Blueprint, render_template, redirect, url_for, abort
import random
import logging
import requests

#Declare Blueprints for main app (views) and the error handler I think works(?) (error_handlers)
views = Blueprint('views', __name__)
error_handlers = Blueprint('error_handlers', __name__)

#Function for selecting one of the gifs in static images to serve as a background for any page (used mainly for error pages)
def get_gif_urls():
    return [url_for('static', filename=f'images/gif{i}.gif') for i in range(1, 4)]



# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-  |
#  GENERAL VIEWS                                                 |
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- \ /



#region =-=-=-=- Home Page -=-=-=-=

@views.route('/')
def home():
    return render_template("homepage.html")

#endregion

# -----------------


#region =-=-=-=- About Page -=-=-=-=

@views.route('/about')
def about():
    return "This is the about page"

#endregion



# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-  |
#  VIEW FOR TRIGGERING ERRORS FOLLOWED BY ERROR HANDLING ROUTES  |
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- \ /



####region =-=-=-=- Error Testing Route -=-=-=-=


# USE ROUTE BELOW FOR TESTING ERROR CODES AND MAKING APPROPRIATE MESSAGES
# @views.route('/error') #Currently set to trigger a 500 error when I input this route
# def trigger_forbidden():
#     abort(500)

####endregion 

# -----------------

####region =-=-=-=- 404 Error Handling Route -=-=-=-=


# 404 error handler for this blueprint
@error_handlers.app_errorhandler(404)
def not_found(e):
    gif_path = random.choice(get_gif_urls())

    # List contains the error code, message displayed, and the page text font size.
    code_message_font = [404, "Page Not Found ", "8vh"]


    return render_template("error.html", gif_path=gif_path, code_message_font=code_message_font), 404

####endregion

# -----------------

####region =-=-=-=- 500 Error Handling Route -=-=-=-=

# 500 error handler for this blueprint
@error_handlers.app_errorhandler(500)
def server_error(e):
    gif_path = random.choice(get_gif_urls())

    # List contains the [error code, message displayed, and the page text font size].
    code_message_font = [500, "Unexpected Server-Side Exception ", "5vh"]

    return render_template("error.html", gif_path=gif_path, code_message_font=code_message_font), 500


####endregion

# -----------------
