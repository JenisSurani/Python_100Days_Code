from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/test', methods=['GET'])
def test_api():
    return jsonify({"message": "Hello, this is a test API!"})

@app.route('/test', methods=['POST'])
def post_data():
    data = request.json  # Accept JSON data
    return jsonify({"received": data}), 201  # Respond with received data

if __name__ == '__main__':
    app.run(debug=True)
