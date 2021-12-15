from flask import Flask, request, render_template
from datetime import datetime

from sun import Sun

app = Flask(__name__, template_folder='./docs')


###############################################################
#                         Web Routes                         #
###############################################################


@app.route('/')
def index():
    return render_template('index.html')


###############################################################
#                         Api Routes                         #
###############################################################

@app.route('/sunset', methods=['GET'])
def get_sunset():
    date = datetime.strptime(request.args.get('date'), '%Y-%m-%d').date()
    longitude = float(request.args.get('lon'))
    latitude = float(request.args.get('lat'))
    sunset = Sun().sunset(longitude, latitude, date)
    return {'datetime': str(sunset.isoformat('T')), 'location': {'longitude': longitude, 'latitude': latitude}}


@app.route('/sunrise', methods=['GET'])
def get_sunrise():
    date = datetime.strptime(request.args.get('date'), '%Y-%m-%d').date()
    longitude = float(request.args.get('lon'))
    latitude = float(request.args.get('lat'))
    sunrise = Sun().sunrise(longitude, latitude, date)
    return {'datetime': str(sunrise.isoformat('T')), 'location': {'longitude': longitude, 'latitude': latitude}}
