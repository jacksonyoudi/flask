#!/usr/bin/env python
# coding: utf8

from flask import Flask, url_for

app = Flask(__name__)


@app.route("/user/<username>")
def say_hello(username):
    return "hello,%s" % username


@app.route("/age/<int:id>")
def show_age(id):
    return "age:%d" % id


@app.route("/about")
def about():
    return "about"


@app.route("/project/")
def project():
    return "project"


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
    with app.test_request_context():
        print url_for('say_hello')
        print url_for('say_hello', username="youdi")
        print url_for('about')
        print url_for('project')
