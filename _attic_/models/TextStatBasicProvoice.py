'''

  First model that selects important keyword from user input.

'''

import json
from textstat.textstat import textstat


class TextStatBasicProvoice():

    # Constructor
    def __init__(self):
        self.id = "text_stat_basic_provoice"
        self.description = "A basic model that selects important keyword from user input..."

    # Helper method to make this class serializable
    def toJson(self):
        response = {}
        response['id'] = self.id
        response['description'] = self.description
        return response

    # The main function of the class.  Works with the API to return a response
    def get_provoice_response(self, input):
        result = {}
        result['input'] = input
        result['model'] = self.toJson()

        responses = []

        #Replace any commas with spaces, so we only have one delimeter character
        input = input.replace(",", " ")

        #Replace any other punctuation  (TODO: There are better ways to do this..)
        input = input.replace("?", " ")
        input = input.replace(".", " ")


        #break up each word in the input
        all_words = input.split(" ")

        for w in all_words:
            wlower = w.lower()
            hi_score = 0
            wordscore = textstat.difficult_words(wlower)
            if wordscore > hi_score:
                hi_score = wordscore # TODO why does this say 'local variable is not used'?
                highest_word = wlower

        responses.append(highest_word)

        result['response'] = responses
        return result

