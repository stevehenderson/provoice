# Sample API
# API to get a provoice response

from flask import Flask, request
from datetime import timedelta
from flask_cors import CORS
from pprint import pprint
import time
import datetime
from dateutil import parser as dateparser
import json
import random

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

########################
# INITIALIZE DATE MODEL
########################
#Tweets
tweets = []

data = json.load(open('twitter.json'))

for tweet in data['tweets']:
    newTweet = Tweet(tweet["status"],tweet["loc_string"],tweet["updated"],tweet["screen_name"],tweet["post_title"],tweet["Unix_time"],tweet["n_id"],tweet["ap_id"],tweet["thing"],tweet["score"],tweet["link"],tweet["published"],tweet["lat"],tweet["time_stamp"],tweet["content_hash"],tweet["location_prob"],tweet["lng"],tweet["tags"],tweet["screen_id"])
    tweets.append(newTweet)


# print the model as json
def dump_model(aModel):
    result = "{ \"tweets\": "
    result=result + json.dumps(aModel, cls=MyEncoder)  + "}"
    return result

#############################
# WEB API METHODS
#############################

# EB looks for an 'application' callable by default.
application = Flask(__name__)

@application.route('/get_tweets', methods=['GET', 'OPTIONS'])
@crossdomain(origin='*', headers=['Content-Type','Authorization'])
def get_tweets():

    screen_name = request.args.get('screen_name', default = '*', type = str)
    timestamp_start = request.args.get('startDate', default = '*', type = str)
    timestamp_end = request.args.get('endDate', default = '*', type = str)
    sentiment_score = request.args.get('sentiment', default = '*', type = str)
    search_terms = request.args.get('search', default = '*', type = str)

    if(len(timestamp_start)>5):
        timestamp_start = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(float(timestamp_start)/1000))
        timestamp_end = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(float(timestamp_end)/1000))
    print("startDate:{0}".format(timestamp_start))

    returnModel = tweets

    #################
    #Apply filters
    #################

    # Screenname
    if screen_name != "*":
        returnModel = [x for x in returnModel if x['screen_name'] == screen_name]

    # Sentiment Score
    if sentiment_score != "*":
        returnModel = [x for x in returnModel if x['score'] == sentiment_score]

    # Search Terms
    if search_terms != "*":
        print search_terms
        search_termsList = search_terms.split(" ")
        print search_termsList
        for term in search_termsList:
            returnModel = [x for x in returnModel if term.lower() in x['thing'].lower()]

    # DTG
    if timestamp_start != "*":
        st=dateparser.parse(timestamp_start)
        et=dateparser.parse("1/1/2050")
        if timestamp_end != "*":
            et=dateparser.parse(timestamp_end)
        returnModel = [x for x in returnModel if ((dateparser.parse(x['time_stamp']) >= st) & (dateparser.parse(x['time_stamp']) <= et)) ]


    response = dump_model(returnModel)
    return response


# add a rule for the index page.
application.add_url_rule('/', 'index', (lambda: dump_model()))


# run the app.
if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    application.debug = True
    application.run(host='0.0.0.0')