from flask import request
from flask_restful import Resource
from flask_jwt import jwt_required
from models.get_suggestions_model import SuggestionGenerator


class GetSuggestions(Resource):
    def __init__(self,):
        self.input = input
        self.suggestion_generator = SuggestionGenerator()
    @jwt_required()
    def get(self):
        input = request.args.get('input', default=None, type=str)
        print(input)
        if input is None:
            return {'message': 'no input'}
        else:
            return self.suggestion_generator.get_suggestion(input)

