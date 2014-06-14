#!/usr/local/bin/python
# -*- coding=UTF-8 -*-
import os, sys
from flask import Flask, render_template, redirect, request, session 
import model
import requests
import json

app= Flask(__name__)

@app.teardown_request
def teardown_request(exc):
	model.session.close()

@app.route('/')
def index():
    #user = model.User.get(1)
    #return 'Hello %s!' %user.username
    return render_template('index.html')

@app.route('/emotions')
def emotions():
    elements = model.Element.get_all()
    #imgs = model.Element.get_all_imgs("image")
    #vids = model.Element.get_all_videos("video")
    return render_template('emotions.html', elements=elements)

@app.route('/emotions/music')
def get_music():
    url = "http://ws.audioscrobbler.com/2.0/?method=tag.getTopTags&api_key=de7fb3597dd8746a57b068228cb9f986&format=json"
    r = requests.get(url)
    return json.dumps(r.json())

app.secret_key = 'this_a_non_secret_key'

if __name__ == '__main__':
    app.run(debug=True, port=33507)
