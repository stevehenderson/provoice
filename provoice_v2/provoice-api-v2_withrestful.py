from flask import Flask, request
from flask_restful import Resource, Api
from Resources.get_suggestions_resource import GetSuggestions

app = Flask(__name__)
api = Api(app)



#api.add_resource(GetProvoiceResponse, '/')
api.add_resource(GetSuggestions, '/get_suggestions', '/')

if __name__ == '__main__':
    app.run(port=5000, debug=True)