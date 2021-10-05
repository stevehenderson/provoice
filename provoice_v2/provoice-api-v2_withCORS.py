# draft CORS api

from flask import Flask, request
from flask_cors import CORS

application = Flask(__name__)
CORS(application, resources={r"/*": {"origins": "*"}})

# TODO insert cross domain need help with this



@application.route('/get_suggestions', methods=['GET', 'OPTIONS'])
def get_suggestions():
    """ This would then go to R002 method to return suggestions?"""
    input = request.args.get('input', default=None, type=str)
    if input is None:
        return {'message': 'no input, please enter some text'}
    else:
        return {'responses': ["response1", "response2"]}


if __name__ == '__main__':
    application.run(port=5000, debug=True)