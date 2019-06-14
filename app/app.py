#!/usr/bin/env python3
from flask import Flask, render_template, request, redirect, url_for
import os

application = Flask(__name__, static_url_path='/static')

templateLayout = 'layout.html'
templateIndex = 'index.html'
templateTech = 'tech.html'
templateClubs = 'clubs.html'

#=============================================================================#
# Handles Route /
@application.route('/', methods=['GET', 'POST'])
def index():
    return render_template(templateIndex, layoutfp=templateLayout)

@application.route('/tech', methods=['GET', 'POST'])
def tech():
    return render_template(templateTech, layoutfp=templateLayout)

@application.route('/clubs', methods=['GET', 'POST'])
def clubs():
    return render_template(templateClubs, layoutfp=templateLayout)

#=============================================================================#
# https://stackoverflow.com/questions/21714653/flask-css-not-updating
@application.context_processor
def override_url_for():
    return dict(url_for=dated_url_for)

def dated_url_for(endpoint, **values):
    if endpoint == 'static':
        filename = values.get('filename', None)
        if filename:
            file_path = os.path.join(application.root_path,
                                 endpoint, filename)
            values['q'] = int(os.stat(file_path).st_mtime)
    return url_for(endpoint, **values)

#=============================================================================#

if __name__ == "__main__":
    application.debug = True
    application.run()
