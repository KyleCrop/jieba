#Noah Rubin
#07/24/2014
#jiebaAPI_authentication.py

from functools import wraps
from flask import request, Response

def check_auth(username, secret_key):
	"""Private helper function
	Checks if username and password are correct"""
	return username == 'Baixing_JiebaAPI' and secret_key == 'Tu5kG7rq8PWpyqr'

def authenticate():
	"""Sends a 401 response that enables basic auth"""
	return Response(
	'Could not verify your access level for that URL.\n'
	'You have to login with proper credentials', 401,
	{'WWW-Authenticate': 'Basic realm="Login Required"'})

def requires_auth(f):
	"""Wrapper function requiring authentication"""
	@wraps(f)
	def decorated(*args, **kwargs):
		auth = request.authorization
		if not auth or not check_auth(auth.username, auth.password):
			return authenticate()
		return f(*args, **kwargs)
	return decorated


