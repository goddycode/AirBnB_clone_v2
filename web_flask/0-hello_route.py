#!/usr/bin/python3
"""
starts a Flask web application
"""
from flask import Flask

app = Flask(__name__)

"""The route decorator defines the URL path and the function to handle requests
"""
@app.route('/airbnb-onepage/')
def hello_HBNB():
    return 'Hello HBNB!'

"""Run the Flask development server on port 5000"""
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
