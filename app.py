from flask import Flask, request, render_template, Response
from datetime import datetime

from flask.json import JSONEncoder

from sun import Sun

app = Flask(__name__, template_folder='./docs')

VALID_API_KEYS = {'B3rDwaXJ24As6Q6o5BEN64VFgemKMRJG',
                  'DmvvPxZoZSi2SpgmGC4KH2akTeEouk9x'}


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
    if (request.args.get('key') in VALID_API_KEYS):
        date = datetime.strptime(request.args.get('date'), '%Y-%m-%d').date()
        longitude = float(request.args.get('lon'))
        latitude = float(request.args.get('lat'))
        sunset = Sun().sunset(longitude, latitude, date)
        return {'datetime': str(sunset.isoformat('T')), 'location': {'longitude': longitude, 'latitude': latitude}}
    else:
        error = {'error': 'invallid key',
                 'used-key': str(request.args.get('key'))}
        return Response(JSONEncoder().encode(error), status=403, mimetype='application/json')


@app.route('/sunrise', methods=['GET'])
def get_sunrise():
    if (request.args.get('key') in VALID_API_KEYS):
        date = datetime.strptime(request.args.get('date'), '%Y-%m-%d').date()
        longitude = float(request.args.get('lon'))
        latitude = float(request.args.get('lat'))
        sunrise = Sun().sunrise(longitude, latitude, date)
        return {'datetime': str(sunrise.isoformat('T')), 'location': {'longitude': longitude, 'latitude': latitude}}
    else:
        error = {'error': 'invallid key',
                 'used-key': str(request.args.get('key'))}
        return Response(JSONEncoder().encode(error), status=403, mimetype='application/json')
