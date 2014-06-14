#!/usr/local/bin/python
# -*- coding=UTF-8 -*-
import os, sys
from flask import Flask, render_template, redirect, request, session 
import model
#import sqlite3
#from flask import g

#DATABASE = 'emotion_data.db.db'

#def get_db():
#    db = getattr(g, '_database', None)
#    if db is None:
#        db = g._database = sqlite3.connect(DATABASE)
#        return db

#@app.teardown_appcontext
#    def close_connection(exception):
#        db = getattr(g, '_database', None)
#        if db is not None:
#            db.close()

app= Flask(__name__)

@app.teardown_request
def teardown_request(exc):
	model.session.close()

@app.route('/')
def index():
    user = model.User.get(1)
    return 'Hello %s!' %user.username


app.secret_key = 'this_a_non_secret_key'

if __name__ == '__main__':
    app.run(debug=True)
