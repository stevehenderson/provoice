from provoice_v2.Models.WikiSearchTwoProvoice import WikiSearchTwoProvoice
from flask import request
from provoice_v2.Models.DictionaryModel import DictionaryModel
from provoice_v2.Models import Suggestion


class SuggestionGenerator():
    def __init__(self):
        self.name = "Suggestion Generator"
        self.model = WikiSearchTwoProvoice()
        self.model2 = DictionaryModel()

    def set_model(self, amodel):
        self.model = amodel


    def get_suggestion(self, input):
        responses = {}

        #return {'responses': []}
        user_input = request.args.get('input', default=None, type=str)
        print("user input is {}".format(user_input))
        text = self.model.get_provoice_response(user_input)
        print("text is {}".format(text))
        text2 = self.model2.get_provoice_response(user_input)
        #return text
        responses['response1'] = text
        responses['response2'] = text2
        print("responses equal {}".format(responses))
        return responses
