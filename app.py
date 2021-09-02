from flask import Flask, render_template , request
import pyshorteners

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def home():
	return render_template('index.html')

@app.route('/url',methods=['GET','POST'])
def result():
	key = request.form.get('text')
	shortener = pyshorteners.Shortener()
	x = shortener.tinyurl.short(key)
	return render_template('index.html',result=x)


if __name__ == '__main__':
	app.run()
