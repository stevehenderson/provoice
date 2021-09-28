import json

'''

A simple test model to test API integration.

'''
class TestProvoice():
    def __init__(self):
        self.id = "test_provoice"
        self.description = "A test model for ProVoice to test API integration."

    def toJson(self):
        response = {}
        response['id'] = self.id
        response['description'] = self.description
        return response

    def get_provoice_response(self, input):
        result = {}
        result['response'] = "I AM A TEST MODEL AND THIS IS MY ONLY RESPONSE :)"
        result['model'] = self.toJson()
        return result