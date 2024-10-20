import datetime
from flask import Flask, render_template, request, redirect, url_for
from markupsafe import escape
import sqlite3

app = Flask(__name__)

@app.route('/') #this is the web URL for the home page
def hello():
    return render_template('index.html', utc_dt=datetime.datetime.utcnow())

@app.route('/about/') #this is the URL for the about page
def about():
    return render_template('about.html')

@app.route('/comments/') #list that contains 3 items and returns a template file passing a variable called comments
                        #containing the list
def comments():
    comments= ['This is the first comment.',
               'This is the second comment.',
               'This is the third comment.']
    return render_template('comments.html', comments=comments)