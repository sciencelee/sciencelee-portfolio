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
                                id="index",
                                blog=helper.blog_posts[0],
                                project=helper.projects[0]
                                )


@app.route('/portfolio', methods=['POST', 'GET'])
def portfolio():
    # get the title content for the portfolio page
    title_text = helper.messages['portfolio']
    title = helper.titles['portfolio']

    return render_template('/portfolio.html',
                            title_text=title_text,
                            title=title,
                            id="portfolio",
                            projects=helper.projects,)


@app.route('/about', methods=['POST', 'GET'])
def about():
    # default language if user enters about without language preference in url
    title_text = helper.messages['about']
    title = helper.titles['about']
    skills = helper.skills

    return render_template('/about.html',
                            title_text=title_text,
                            skills=skills,
                            title=title,
                            id="about")



@app.route("/robots.txt")
def robots():
    '''
    Add robots.txt file to avoid google indexing
    '''
    return send_from_directory(app.static_folder, request.path[1:])


if __name__ == '__main__':
    app.run()