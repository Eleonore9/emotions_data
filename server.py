#!/usr/local/bin/python
# -*- coding=UTF-8 -*-
import os, sys
from flask import Flask, render_template, redirect, request, session 
import model
#import requests
import json

app= Flask(__name__)
app.config.update(
        DEBUG = True,
)

@app.teardown_request
def teardown_request(exc):
	model.session.close()

#----For now simple homepage that directly
#----links to the 'emotions' page, no user session
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/emotions')
def emotions():
    elements = model.Element.get_all()
    #elements = model.Element.get_all_emotion("sad")
    return render_template('emotions.html', elements=elements)

#@app.route('/emotions/music')
#def get_music():
    #url = "http://ws.audioscrobbler.com/2.0/?method=tag.getTopTags&api_key=de7fb3597dd8746a57b068228cb9f986&format=json"
    #r = requests.get(url)
    #return json.dumps(r.json())

#----User login to implement later
@app.route("/authenticate", methods=['POST'])
def authenticate():
	email = request.form['email']
	password = request.form['password']
	user_auth = model.User.authenticate(email, password)
	if user_auth is not None:
		session['user_id'] = user_auth.id
		flash('You were logged in successfully!')
		return redirect(url_for("enter_text"))
	return redirect(url_for("index"))

@app.route("/sign_up")
def sign_up():
    return render_template("signup.html")

@app.route("/logout")
def logout():
	session.pop('user_id', None)
	flash('You were logged out.')
	return redirect(url_for('index'))

app.secret_key = 'this_a_non_secret_key'

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
