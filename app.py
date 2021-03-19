from flask import Flask, render_template

# Configure application
app = Flask(__name__)

@app.route('/index', methods=['POST', 'GET'])
@app.route('/', methods=['POST', 'GET'])
def index():

    greeting = 'Welcome to My Data Science Portfolio Website'

    return render_template('/index.html',
                            title = "Data Science Portfolio",
                            id = "index",
                            greeting=greeting)


@app.route('/projects', methods=['POST', 'GET'])
@app.route('/', methods=['POST', 'GET'])
def projects():
    greeting = 'Welcome to My Data Science Projects Page'
    return render_template('/projects.html',
                            greeting=greeting)


@app.route('/about', methods=['POST', 'GET'])
@app.route('/', methods=['POST', 'GET'])
def about():
    greeting = 'Welcome to My Data Science About Me Page'
    return render_template('/about.html',
                            greeting=greeting)


@app.route('/blog', methods=['POST', 'GET'])
@app.route('/', methods=['POST', 'GET'])
def blog():
    return render_template('/blog.html')