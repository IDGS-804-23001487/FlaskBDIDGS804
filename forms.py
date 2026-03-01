from wtforms import Form
from flask_wtf import FlaskForm
 
from wtforms import StringField, IntegerField
from wtforms import EmailField
from wtforms import validators
 
class UserForm(Form):
    id = IntegerField('id', [
        validators.number_range(min=1, max=20, message='valor no valido')
    ])
   
    nombre = StringField('nombre', [
        validators.DataRequired(message='El nombre es requerido'),
        validators.length(min=4, max=20, message='requiere min=4 max=20')
    ])
   
    apaterno = StringField('apaterno', [
        validators.DataRequired(message='El apellido es requerido')
    ])
   
    email = EmailField('correo', [
        validators.DataRequired(message='El apellido es requerido'),
        validators.Email(message='Ingrese un correo valido')
    ])
    

class MaestroForm(Form):
    
    matricula = IntegerField('Matricula', [
        validators.NumberRange(min=1, message="Valor no válido")
    ])
    
    nombre = StringField("Nombre", [
        validators.DataRequired(message="El nombre es requerido"),
        validators.Length(min=1, max=50)
    ])
    
    apellidos = StringField("Apellidos", [
        validators.DataRequired(message="Los apellidos son requeridos")
    ])
    
    especialidad = StringField("Especialidad", [
        validators.DataRequired(message="La especialidad es requerida")
    ])
    
    email = EmailField("Email", [
        validators.DataRequired(message="El email es requerido"),
        validators.Email(message="Ingrese un correo válido")
    ])
 
