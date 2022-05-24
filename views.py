from config import app
from flask import render_template , request
import pyshorteners

@app.get('/')
def home_page():
	return render_template('index.html')

@app.post('/url')
def url_shorting():
	key = request.form.get('text')
	shortener = pyshorteners.Shortener()
	shortened_url = shortener.tinyurl.short(key)
	return render_template('index.html',result=shortened_url)
