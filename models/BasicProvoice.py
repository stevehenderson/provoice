import json

class BasicProvoice():
    def __init__(self):
        self.id = "basic_provoice"
        self.description = "A simple Provoice model with simple responses."

    def toJson(self):
        response = {}
        response['id'] = self.id
        response['description'] = self.description
        return response

    def get_provoice_response(self, input):
        result = {}
        if 'steve' in input.lower():
            result['response'] = "Oooh you mentioned Steve!  He's a good dude!"
        elif 'new york' in input.lower():
            result['response'] = "Oh I love New York!"
        else:
            result['response'] = "I am at a loss for words.."
        result['model'] = self.toJson()
        return result
