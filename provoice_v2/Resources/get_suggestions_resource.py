from flask import Flask, request
from flask_restful import Resource
#import jwt
from Models.get_suggestions_model import SuggestionGenerator
from Models.WikiSearchTwoProvoice import WikiSearchTwoProvoice
from flask_jwt import jwt_required


class GetSuggestions(Resource):
    def __init__(self,):
        self.input = input
        self.suggestion_generator = SuggestionGenerator()

    def get(self):
        input = request.args.get('input', default=None, type=str)
        print(input)
        if input is None:
            return {'message': 'no input'}
        else:
            return self.suggestion_generator.get_suggestion(input)
            #return WikiSearchTwoProvoice.get_provoice_response(input)
