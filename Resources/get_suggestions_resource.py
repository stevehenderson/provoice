from flask import request
from flask_restful import Resource
from flask_jwt import jwt_required
from models.get_suggestions_model import SuggestionGenerator
from models.BasicGreeterModel import BasicGreetingProvoice
#---
import json
import re
import random


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
            return self.get_basic_greeter(input)

        #else:
        #    return self.suggestion_generator.get_suggestion(input)


    def get_basic_greeter(self, input):

        # Building dictionary of Intents & Keywords
        keywords={}
        keywords_dict={
            'greet_basic': re.compile('hi|hello|howdy|hey|how are you'),
            'doing': re.compile('what are you doing|what are you up to|doing today')

        }

        # Building a dictionary of response

        responses = {
            'greet_basic': ["Hello!", "Hi", "Hey", "Whats Up!",],
            'doing':["Not much", "Just hanging out", "Just working, you?", "No plans! How about you?"],
            'fallback':'ERROR'
        }

        result = {}
        # Takes the user input and converts all characters to lowercase
        user_input = input.lower()
        print(user_input)

        matched_lemma = None
        found_greeting_response = False
        for keys, pattern in keywords_dict.items(): # pattern here is values of keyword_dict
            # Using the regular expression search function to look for keywords in user input
            if re.search(pattern, user_input):
                # if a keyword matches, select the corresponding key from the keywords_dict dictionary
                matched_lemma=keys #keys here is lemma word


        #key='fallback' # default key is fallback response incase there is no response for this chatbot etc... not needed for provoice so much
        if matched_lemma in responses:
            # If a keyword matches, the fallback response key is replaced by the matched_lemma as the key for the responses dictionary
            key = matched_lemma
            # The chatbot prints the response from responses dictionary that matches the key found in both dictionaries, found from searching user input
            found_greeting_response = True

            final_response_list = list(responses[key])
            chosen_response = random.choice(final_response_list)
            result['greeting'] = (chosen_response)

        #if found_greeting_response == True:
            #return result
        result['response'] = self.suggestion_generator.get_suggestion(input)
        return result
