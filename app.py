# main code will live here, should be almost empty though
from flask import Flask, jsonify
from routes import *

app = Flask(__name__)
app.register_blueprint(routes)

@app.route('/', methods=['GET'])
def hello():
    return jsonify(about='Hello, WP! Welcome to the pipeline.')

if __name__ == '__main__':
    app.run(debug=True, port=5000)