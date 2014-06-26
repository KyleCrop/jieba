from flask_wtf import Form
from wtforms import TextField, BooleanField
from wtforms.validators import DataRequired

'''
class LoginForm(Form):
    username = TextField('username', validators=[DataRequired()] )
    password = TextField('password', validators=[DataRequired()] )
    
class CreateTaskForm(Form):
    title = TextField('title', validators=[DataRequired()] )
    description = TextField('description', validators=[DataRequired()] )
    done = BooleanField('done', default = False)
'''

class JiebaForm(Form):
	enterText = TextField('Enter text', validators=[DataRequired()] )
	
    
