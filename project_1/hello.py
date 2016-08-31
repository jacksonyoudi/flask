#!/usr/bin/env python
# coding: utf8

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "hello World!"


if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)