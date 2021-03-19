from flask import Blueprint, Flask, g, jsonify, render_template, request, Response, redirect, url_for, send_from_directory
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
import helper
import os

app = Flask(__name__)

@app.route('/index', methods=['POST', 'GET'])
@app.route('/', methods=['POST', 'GET'])
def index():
    # main page
    return render_template('index.html',
                                title_text=helper.messages['index'],
                                title=helper.titles['index'],
                                id="index")


@app.route('/portfolio', methods=['POST', 'GET'])
def portfolio():
    # get the title content for the portfolio page
    title_text = helper.titles['portfolio']

    return render_template('/portfolio.html',
                            title_text=title_text,
                            title="PROJECT PORTFOLIO",
                            id="portfolio",
                            projects=helper.projects,)


@app.route('/about', methods=['POST', 'GET'])
def about():
    # default language if user enters about without language preference in url
    title_text = helper.about_title_text

    skills = helper.skills

    return render_template('/about.html',
                            title_text=title_text,
                            skills=skills,
                            title="ABOUT ME",
                            id="about")



@app.route("/robots.txt")
def robots():
    '''
    Add robots.txt file to avoid google indexing
    '''
    return send_from_directory(app.static_folder, request.path[1:])


if __name__ == '__main__':
    app.run()