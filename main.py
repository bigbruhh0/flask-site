import sys
from flask import Flask, render_template, Response, request, render_template_string,url_for,redirect
users=[]
#save_users(users)
app = Flask(__name__)
@app.route('/')
def index():
	icons = ['static/icon1.png', 'static/icon2.png', 'static/icon3.gif']
	backgrounds = ['static/background1.jpg', 'static/background2.jpg']
	print(123123)
	return render_template('index.html',icons=icons,backgrounds=backgrounds)

if __name__ == '__main__':
    # run app in debug mode on port 5000
    app.run(debug=True, port=5000)

