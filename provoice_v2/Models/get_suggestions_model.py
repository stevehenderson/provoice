from Models.WikiSearchTwoProvoice import WikiSearchTwoProvoice
from flask import request
from Models import DictionaryModel
from Models import Suggestion


class SuggestionGenerator():
    def __init__(self):
        self.name = "Suggestion Generator"
        self.model = WikiSearchTwoProvoice()

    def set_model(self, amodel):
        self.model = amodel


    def get_suggestion(self, input):
        #return {'responses': []}
        user_input = request.args.get('input', default=None, type=str)

        text = self.model.get_provoice_response(user_input)
        new_suggestion = Suggestion(text)
        return new_suggestion
