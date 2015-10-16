# coding: utf-8
from flask import Flask, render_template, json, request, redirect, session, jsonify, url_for
from flask.ext.mysql import MySQL 
from werkzeug import generate_password_hash, check_password_hash
from werkzeug.wsgi import LimitedStream
import uuid
import os
import urllib2

app = Flask(__name__)

@app.route("/")
def main():
	return render_template("index.html")


if __name__ == "__main__":
	app.run()