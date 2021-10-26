from flask import Flask, request, jsonify


app = Flask(__name__)



@app.route('/get_suggestions', methods=['GET'])
def get_suggestions():
    input = request.args.get('input', default=None, type=str)
    if input is None:
        return jsonify({'message': 'no input, please enter some text'})
    else:
        return {'responses': ["response1", "response2"]}


if __name__ == '__main__':
    app.run(port=5000, debug=True)
