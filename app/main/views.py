from flask import render_template,request,redirect,url_for


@main.route('/userprofile')
def userprofile():
    
    return render_template('profile.html')
