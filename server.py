#!/usr/local/bin/python
# -*- coding=UTF-8 -*-
import os, sys
from flask import Flask, render_template, redirect, request, session 
import model

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
    element = model.Element.get(1)
    return render_template('emotions.html', element=element)


app.secret_key = 'this_a_non_secret_key'

if __name__ == '__main__':
    app.run(debug=True)
