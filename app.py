from flask import Flask, json, Response, render_template

app = Flask(__name__)


###############################################################
#                           Routes                            #
###############################################################


@app.route('/')
def index():
    return render_template('index.html')
