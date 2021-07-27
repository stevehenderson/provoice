# Sample API
# API to get a provoice response

from flask import Flask, request
from flask_cors import CORS
from models.BasicProvoice import BasicProvoice
from models.TestProvoice import TestProvoice

application = Flask(__name__)
CORS(application, resources={r"/*": {"origins": "*"}})

#  Add models, contained in classes, here...
testProvoiceModel = TestProvoice()
basicProvoiceModel = BasicProvoice()

application = Flask(__name__)
 
#############################
# WEB API METHODS
#############################

#
#  Given an input, returns a provoice response.
#  If no model is specified, the BasicProvoice model is invoked.
#
@application.route('/get_provoice_response', methods=['GET', 'OPTIONS'])
def get_provoice():
    input = request.args.get('input', default = None, type = str)
    model = request.args.get('model', default = 'basic_provoice', type = str)
    sentiment = request.args.get('sentiment', default = None, type = str)
    result = {}
    if input is None:
        result['response'] = "ERROR.  You didn't send an input"
        return result
    # Check the input parameter for the selected model
    if model == "basic_provoice":
        result = basicProvoiceModel.get_provoice_response(input)
    elif model == "test_provoice":
        result = testProvoiceModel.get_provoice_response(input)
    else:
        result['response'] = "ERROR.  Your desired model {} is not implemented".format(model)
    result['input'] = input
    return result

#
#  Given an input, returns a provoice response
#
@application.route('/', methods=['GET', 'OPTIONS'])
def home():
    return "<h1>Welcome to the Provoice API</h1>"

#
#  Given an input, returns a provoice response
#
@application.route('/oregon', methods=['GET', 'OPTIONS'])
def oregon():
    return "<h2>Welcome to the Oregon</h2>"

# run the app.
if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    application.debug = True
    application.run(host='0.0.0.0')