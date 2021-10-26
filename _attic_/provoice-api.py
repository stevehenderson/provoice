# Sample API
# API to get a provoice response

from flask import Flask, request, render_template
from flask_cors import CORS
import json
from models.BasicProvoice import BasicProvoice
from models.BasicKeywordLookupProvoice import BasicKeywordLookupProvoice
from models.DictionaryModel import DictionaryModel
from models.TestProvoice import TestProvoice
from models.OregonDudeProvoice import OregonDudeProvoice
from models.TextStatBasicProvoice import TextStatBasicProvoice
from models.WikiSearchOneProvoice import WikiSearchOneProvoice

application = Flask(__name__)
CORS(application, resources={r"/*": {"origins": "*"}})

from datetime import timedelta
from flask import make_response, request, current_app
from functools import update_wrapper


def crossdomain(origin=None, methods=None, headers=None,
                max_age=21600, attach_to_all=True,
                automatic_options=True):
    if methods is not None:
        methods = ', '.join(sorted(x.upper() for x in methods))
    if headers is not None and not isinstance(headers, basestring):
        headers = ', '.join(x.upper() for x in headers)
    if not isinstance(origin, basestring):
        origin = ', '.join(origin)
    if isinstance(max_age, timedelta):
        max_age = max_age.total_seconds()

    def get_methods():
        if methods is not None:
            return methods

        options_resp = current_app.make_default_options_response()
        return options_resp.headers['allow']

    def decorator(f):
        def wrapped_function(*args, **kwargs):
            if automatic_options and request.method == 'OPTIONS':
                resp = current_app.make_default_options_response()
            else:
                resp = make_response(f(*args, **kwargs))
            if not attach_to_all and request.method != 'OPTIONS':
                return resp

            h = resp.headers

            h['Access-Control-Allow-Origin'] = origin
            h['Access-Control-Allow-Methods'] = get_methods()
            h['Access-Control-Max-Age'] = str(max_age)
            if headers is not None:
                h['Access-Control-Allow-Headers'] = headers
            return resp

        f.provide_automatic_options = False
        return update_wrapper(wrapped_function, f)
    return decorator

#  Add models, contained in classes, here...
basicProvoiceModel = BasicProvoice()
basicKeywordLookupProvoiceModel = BasicKeywordLookupProvoice()
oregonDudeProvoiceModel = OregonDudeProvoice()
testProvoiceModel = TestProvoice()
dictionaryModel = DictionaryModel()
textStatBasicModel = TextStatBasicProvoice()
wikiSearchOneProvoiceModel = WikiSearchOneProvoice()

application = Flask(__name__)
 
#############################
# WEB API METHODS
#############################

# EB looks for an 'application' callable by default.
application = Flask(__name__)


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
    elif model == "oregon_dude_provoice":
        result = oregonDudeProvoiceModel.get_oregon_response(input)
    elif model == "basic_keyword_lookup_provoice":
        result = basicKeywordLookupProvoiceModel.get_provoice_response(input)
    elif model == "dictionary_model":
        result = dictionaryModel.get_provoice_response(input)
    elif model == "text_stat_basic_provoice":
        result = textStatBasicModel.get_provoice_response(input)
    elif model == "wiki_search_one_provoice":
        result = wikiSearchOneProvoiceModel.get_provoice_response(input)
    else:
        result['response'] = "ERROR.  Your desired model {} is not implemented".format(model)
    result['input'] = input
    return result

#
#  Given an input, returns a provoice response
#
@application.route('/', methods=['GET', 'OPTIONS'])
def home():
    return render_template('index.html')

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