from flask import Flask, render_template, request, redirect, url_for
from flask.ext.navigation import Navigation
import flask_login
import sys

application = Flask(__name__)
nav = Navigation(application)

# Template file paths
template404 = '404.html'
templateLayout = 'layout.html'
templateIndex = 'index.html'
templateBlog = 'blog.html'
templateResearch = 'research.html'
templateProjects = 'projects.html'
templateService = 'service.html'
templatePhotos = 'photos.html'
templateVideos = 'videos.html'

# Navigation bar
def set_navbar():
    nav.Bar('top',
            [nav.Item('Home', 'index'),
                nav.Item('Research', 'research'),
                nav.Item('Projects','projects'),
                nav.Item('Service','service'),
                nav.Item('Photography', 'photos'),
                nav.Item('Videos', 'videos')])


#======| ROUTES |=============================================================#
# Handles Error 404
@application.errorhandler(404)
def page_not_found(e):
    return render_template(template404)

# Handles Route /
@application.route('/', methods=['GET', 'POST'])
def index():
    return render_template(templateIndex, layoutfp=templateLayout)

# Handles Route /research
@application.route('/research/', methods=['GET'])
def research():
    projs = [
            {'name':'REU @ Temple University - Summer 2018','proj':'Ravel','desc':'Working on Ravel, a database-defined controller for software-defined networks.', 'img':'/static/img/temple.png'},
            {'name':'Johns Hopkins Medicine CCHR - Spring 2017', 'proj':'Called to Care','desc':'Worked on Called to Care, a project that seeks to decrease caregiver burden by evaluating their knowledge of community resources and connecting them with these resources.'}
            ]
    return render_template(templateResearch, projects=projs, layoutfp=templateLayout)

# Handles Route /projects
@application.route('/projects/', methods=['GET'])
def projects():
    projs = [
            {'name':'AppMinutes - Spring 2018','desc':'Android application that allows users to track mobile application usage.'},
            {'name':'AF Comorbidity - Spring 2018','desc':'Flask application that prototypes Atrial Fibrillation prediction using demographic and comorbidity information from the MIMIC dataset.'},
            {'name':'Logify - Spring 2018','desc':'Android application that allows users to design simple and professional logos.'}
            ]
    return render_template(templateProjects, projects=projs, layoutfp=templateLayout)

# Handles Route /service
@application.route('/service/', methods=['GET'])
def service():
    projs = [
            {'name':'AIDS Alliance','desc':'2016-Current. AIDS Alliance promotes safe sex on campus on campus by handing out condoms. It also partners with Moveable Feast to cook nutritionally tailored meals for patients with AIDS and other chronic conditions. Something unique about Moveable Feast is that it also addresses unemployment through a program that teaches community members to cook.'},
            {'name':'Charm City Science League','desc':'2016-Current. CCSL aims to foster interest in STEM among inner city students. Mentors prepare middle school students to compete in Science Olympiad. CCSL is engaging and fun because students get to choose what they want to learn, so they are personally invested in the topic.'},
            {'name':'Migrant Farm Workers Clinics','desc':'2015-2017. MFWC brings mobile clinics directly to farms in Connecticut to provide health services for migrant farmers, regardless of documentation. Originally, the clinics visited tobacco farms, but now it goes to a variety of farms. General volunteers assist with patient registration, undergraduates perform vitals, and medical students and doctors perform check-ups. Pharmacy students prescribe medicine that companies have donated.'}
            ]
    return render_template(templateService, projects=projs, layoutfp=templateLayout)

# Handles Route /photos
@application.route('/photos/', methods=['GET'])
def photos():
    return render_template(templatePhotos, layoutfp=templateLayout)

# Handles Route /videos
@application.route('/videos/', methods=['GET'])
def videos():
    return render_template(templateVideos, layoutfp=templateLayout)

#=============================================================================#

if __name__ == "__main__":
    application.debug = True
    nav.init_app(application)
    set_navbar()
    application.run()
