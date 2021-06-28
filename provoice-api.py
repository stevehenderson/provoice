# Sample API
# API to get a provoice response

from flask import Flask, request
from flask_cors import CORS
from models.BasicProvoice import BasicProvoice
from models.TestProvoice import TestProvoice

application = Flask(__name__)
CORS(application, resources={r"/*": {"origins": "*"}})

testProvoiceModel = TestProvoice()
basicProvoiceModel = BasicProvoice()

application = Flask(__name__)

#############################
# WEB API METHODS
#############################

#
#  Given an input, returns a provoice response
#
@application.route('/get_provoice_response', methods=['GET', 'OPTIONS'])
def get_provoice():
    input = request.args.get('input', default = None, type = str)
    model = request.args.get('model', default = 'basic_provoice', type = str)
    sentiment = request.args.get('sentiment', default = None, type = str)

    if input is None:
        result = {}
        result['response'] = "ERROR.  You didn't send an input"
        return result

    if model == "basic_provoice":
        return basicProvoiceModel.get_provoice_response(input)
    if model == "test_provoice":
        return testProvoiceModel.get_provoice_response(input)
    else:
        result = {}
        result['response'] = "ERROR.  Your model {} didn't is not implemented".format(model)
        return result


#
#  Given an input, returns a provoice response
#
@application.route('/', methods=['GET', 'OPTIONS'])
def home():
    return "<h1>Welcome to the Provoice API</h1>"

# run the app.
if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    application.debug = True
    application.run(host='0.0.0.0')