from flask import render_template,request,redirect,url_for
from . import main


@main.route('/')
def index():
    """
    function to redirect to main page
    """
    return render_template('index.html')

@main.route('/userprofile')
def userprofile():
    
    return render_template('profile.html')
