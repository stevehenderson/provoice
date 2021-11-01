from flask import Flask, request
from flask_restful import Resource, Api
from flask_cors import CORS
from flask_jwt import JWT
from Resources.get_suggestions_resource import GetSuggestions

from security import authenticate, identity

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})
app.secret_key = 'douglasfir'
api = Api(app)

jwt = JWT(app, authenticate, identity)



api.add_resource(GetSuggestions, '/get_suggestions', '/')

if __name__ == '__main__':
    app.run(port=5000, debug=True)

    #TODO consolidate data folder? Commented out line 43 and 44 in dictionary model, add college reading selection to dict?
    #TODO figure out path for data/dict


