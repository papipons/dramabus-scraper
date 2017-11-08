from flask import Flask, jsonify
from flask_restful import Resource, Api
import requests
import bs4

from constants import *
from models import Drama

app = Flask(__name__)
api = Api(app)

def getSoup(url):
    response = requests.get(url)
    return bs4.BeautifulSoup(response.text)
    
class ApiDrama(Resource):
    def get(self):
        soup = getSoup(DRAMA_URL)
        dramas = Drama.parse(soup)
        return jsonify([drama.__dict__ for drama in dramas])

api.add_resource(ApiDrama, '/drama')

if __name__ == '__main__':
    app.run(debug=True)