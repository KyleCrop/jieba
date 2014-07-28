Jieba API Documentation

All API resources can be found at 'http://0.0.0.0:5000/APIresources"

Get()
	Returns: JSON representation of input cut by jieba method cut_for_search
	Note: output is in UTF-8 encoding
	Precondition (for API users): Input is of type str

Put()
	Procedure: Changes the operating dictionary
	Note: Returns JSON representation of city and category dict updated to
	Precondition (for API users): Input for city and category are of type str

Authorization:

	username: Baixing_JiebaAPI
	secret_key: Tu5kG7rq8PWpyqr

Example get request:
	
	request: get('http://0.0.0.0:5000/APIresources', data={'data':'我最喜欢的是您'}, auth=HTTPBasicAuth('Baixing_JiebaAPI','Tu5kG7rq8PWpyqr')).json()
	output: u'"\\u6211 | \\u6700 | \\u559c\\u6b22 | \\u7684 | \\u662f | \\u60a8"'