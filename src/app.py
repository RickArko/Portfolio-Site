import json
from datetime import datetime
from email_validator import validate_email
from flask import Flask, render_template, request
from utils import validate_string
from utils import get_last_commit_and_upstream_url
import constants
from google_recaptcha import ReCaptcha
from telegram import Bot

app = Flask(__name__)
recaptcha = ReCaptcha(app)
bot = Bot()

@app.errorhandler(404) 
def not_found(e):
    return render_template("404.html")

@app.route('/')
@app.route('/home/')
def home():
    if request.method == 'GET':
        with open(constants.HOME_PATH) as f:
            home_data = json.load(f)
        return render_template('home.html', context=home_data)


@app.route('/experience/')
def experience():
    if request.method == 'GET':
        with open(constants.EXPERIENCE_PATH) as f:
            experience_data = json.load(f)
        return render_template('experience.html', context=experience_data)


@app.route('/blog/')
def blog():
    if request.method == 'GET':
        return render_template('blog.html')


@app.route('/projects/')
def projects():
    if request.method == 'GET':
        with open(constants.PROJECT_PATH) as f:
            projects_data = json.load(f)
        return render_template('projects.html', context=projects_data)


# @app.context_processor
# def context_variables():
#     now = datetime.now()
#     formatted_today = f'{now.year}/{now.month}/{now.day}'
#     commit, upstream_url = get_last_commit_and_upstream_url('origin', 'main')
    
#     return {
#         'today' : formatted_today,
#         'last_upstream_commit' : commit,
#         'upstream_url' : upstream_url
#     }


application = app

if __name__ == "__main__":
    
    app.run(
        host="0.0.0.0",
        # host="127.0.0.1",
        port=5050,
        debug=True
    )