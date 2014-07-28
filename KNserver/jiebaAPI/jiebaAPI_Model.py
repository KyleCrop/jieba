#Noah Rubin
#07/24/2014
#jiebaAPI_Model.py

from jiebaAPI_processWords import *
from jiebaAPI_updateDictionary import *
from jiebaAPI_authentication import *
from flask import Flask, abort
from flask.ext.restful import Resource, Api, reqparse
#import urllib2

''' pragma mark App configuration and Parser def'''

app = Flask(__name__)
#app.config.from_object(__name__)
#app.config.update(dict(#DATABASE = os.path.join(app.root_path, set database), DEBUG = False))
api = Api(app)

parser = reqparse.RequestParser()
#parser.add_argument('sentence', type=str)
parser.add_argument('city', type=str)
parser.add_argument('category', type=str)

''' pragma mark Error Handlers '''

@app.errorhandler(400)
def bad_request(error):
	"""Error handler for an incorrect request
	Returns: Error code 400 indicating a bad request"""
	return make_response(json.dumps( { 'error': 'Bad request' } ), 400)
 
@app.errorhandler(404)
def not_found(error):
	"""Error handler for failure to locate resource
	Returns: Error code 404 indicating a failure to locate resource"""
	return make_response(json.dumps( { 'error': 'Not found' } ), 404)

''' pragma mark API resource definitions '''

class welcomeScreen(Resource):
	"""Point API user toward API resource end point"""
	def get(self):
		return json.dumps('Please refer to resources at ..../APIresources')

class jiebaAPI(Resource):
	"""Container class for jiebaAPI resources"""
	from codecs import decode, encode

	@requires_auth
	def get(self):
		"""Returns: JSON representation of input cut by jieba method cut_for_search
		Note: output is in UTF-8 encoding
		Precondition (for API users): Input is of type str"""
		output = processWords(request.form['data'])
		return output

	@requires_auth
	def put(self):
		"""Procedure: Changes the operating dictionary
		Note: Returns JSON representation of city and category dict updated to
		Precondition (for API users): Input for city and category are of type str"""
		args = parser.parse_args()
		city = args['city']
		category = args['category']
		updateDictionary(args['city'], args['category'])
		return json.dumps('Dictionary updated to: ' + city + ', ' + category)

''' pragma mark Assign resources to  URL '''

api.add_resource(welcomeScreen, '/')
api.add_resource(jiebaAPI, '/APIresources')

if __name__ == '__main__':
	app.run(host='0.0.0.0', debug=True)