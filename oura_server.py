# go to https://cloud.ouraring.com/oauth/applications and create an application
# you will be provided with client_id and client_secret put them to config.py
# put "http://localhost:65010/oura_redir" to redirect uri field

import config # get the CLIENT_ID and CLIENT_SECRET from file

REDIRECT_URI = "http://localhost:65010/oura_redir"

import os
os.environ["FLASK_ENV"] = "development"


from flask import Flask, abort, request
app = Flask(__name__)
@app.route('/')
def homepage():
	text = '<a href="%s">Get access token!</a>'
	return text % make_authorization_url()

# Left as an exercise to the reader.
# You may want to store valid states in a database or memcache,
# or perhaps cryptographically sign them and verify upon retrieval.
def save_created_state(state):
	pass
def is_valid_state(state):
	return True

def make_authorization_url():
	# Generate a random string for the state parameter
	# Save it for use later to prevent xsrf attacks
	from uuid import uuid4
	state = str(uuid4())
	save_created_state(state)
	params = {"client_id": config.CLIENT_ID,
			  "response_type": "code",
			  "state": state,
			  "redirect_uri": REDIRECT_URI,
			  "duration": "temporary",
			  "scope": "email personal daily"} # all possible scopes
	import urllib
	url = "https://cloud.ouraring.com/oauth/authorize?" + urllib.parse.urlencode(params)
	return url

# Left as an exercise to the reader.
# You may want to store valid states in a database or memcache,
# or perhaps cryptographically sign them and verify upon retrieval.
def save_created_state(state):
	pass
def is_valid_state(state):
	return True

import requests
import requests.auth
def get_token(code):
	client_auth = requests.auth.HTTPBasicAuth(config.CLIENT_ID, config.CLIENT_SECRET)
	post_data = {"grant_type": "authorization_code",
				 "code": code,
				 "redirect_uri": REDIRECT_URI}
	response = requests.post("https://cloud.ouraring.com/oauth/token",
							 auth=client_auth,
							 data=post_data)
	token_json = response.json()
	return token_json["access_token"]

@app.route('/oura_redir')
def oura_redir():
	error = request.args.get('error', '')
	error = request.args.get('error_description', '')
	if error:
		return "Error: " + error
	state = request.args.get('state', '')
	if not is_valid_state(state):
		# Uh-oh, this request wasn't started by us!
		abort(403)
	code = request.args.get('code')

	return "got an access token! %s" % get_token(code)

if __name__ == '__main__':
	app.run(debug=True, port=65010)
