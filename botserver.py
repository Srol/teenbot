#!/usr/bin/env python -tt
 
import os
import pickle
import random
from flask import Flask, make_response, request, current_app
from datetime import timedelta
from functools import update_wrapper
from cobe.brain import Brain

app = Flask(__name__)

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
            h['Access-Control-Allow-Credentials'] = 'true'
            h['Access-Control-Allow-Headers'] = \
                "Origin, X-Requested-With, Content-Type, Accept, Authorization"
            if headers is not None:
                h['Access-Control-Allow-Headers'] = headers
            return resp

        f.provide_automatic_options = False
        return update_wrapper(wrapped_function, f)
    return decorator
 
chain = pickle.load(open("chain.p", "rb"))
 
new_review = []
sword1 = "BEGIN"
sword2 = "NOW"
paragraph = []
new_review = []
final = ""

def generateText():
	new_review = []
	sword1 = "BEGIN"
	sword2 = "NOW"
	paragraph = []
	new_review = []
	final = ""
	while True:
		sword1, sword2 = sword2, random.choice(chain[(sword1, sword2)])
		if sword2 == "END":
			break
		new_review.append(sword2)
	if len(' '.join(new_review)) < 20:
		paragraph.append(' '.join(new_review))
		new_review = []
		sword1 = "BEGIN"
		sword2 = "NOW"
		while True:
			sword1, sword2 = sword2, random.choice(chain[(sword1, sword2)])
			if sword2 == "END":
				break
			new_review.append(sword2)
		paragraph.append(' '.join(new_review))
		final = ' '.join(paragraph)
		return final
	else:
		final = ' '.join(new_review)
		return final

def responderText(textQuery):
	b = Brain("cobe.brain")
	return b.reply(textQuery)

@app.route('/teenbot', methods=['GET', 'OPTIONS'])
@crossdomain(origin='*')
def teenBot():
    return generateText()

@app.route('/altbot')
@crossdomain(origin='*')
def altbot():
	textQuery = request.args.get('text')
	return responderText(textQuery)