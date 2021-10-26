from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from _attic_.provoice_v2.Resources import GetSuggestions



app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})
api = Api(app)





api.add_resource(GetSuggestions, '/get_suggestions', '/')



if __name__ == '__main__':
    app.run(port=5000, debug=True)

    #TODO consolidate data folder? Commented out line 43 and 44 in dictionary model, add college reading selection to dict?
    #TODO figure out path for data/dict


