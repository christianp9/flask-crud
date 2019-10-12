from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, validators, SubmitField

class LoginForm(FlaskForm):
    username = StringField('username user',[validators.DataRequired()])
    password = PasswordField('password user', [validators.DataRequired()])
    submit = SubmitField('Enviar')

class TodoForm(FlaskForm):
    game = StringField('nombre',[validators.DataRequired()])
    description = StringField('descripcion',[validators.DataRequired()])
    price = StringField('precio',[validators.DataRequired()])
    submit = SubmitField('agregar')
