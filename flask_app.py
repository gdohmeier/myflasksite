
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, render_template

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route('/hello')
def hello_world():
    return '.... Hello from Flask!'

@app.route('/foo')
def page_foo():
    return 'Hello, this is the foo page.'

@app.route("/")
def index():
    return render_template("main_page.html")
