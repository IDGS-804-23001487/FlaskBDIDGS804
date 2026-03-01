from flask import Flask, render_template, request, redirect, url_for, flash
from flask_wtf.csrf import CSRFProtect
from config import DevelopmentConfig
from flask_migrate import Migrate
from maestros.routes import maestros
import forms
from models import db, Alumnos

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
app.register_blueprint(maestros)
db.init_app(app)
migrate = Migrate(app, db) 
csrf = CSRFProtect()
csrf.init_app(app)

@app.route("/alumnos", methods=['GET', 'POST'])
def alumnos():
    create_form = forms.UserForm(request.form)
    if request.method == 'POST' and create_form.validate():
        alum = Alumnos(
            nombre=create_form.nombre.data, 
            apellidos=create_form.apellidos.data, 
            email=create_form.email.data, 
            telefono=create_form.telefono.data
        )
        db.session.add(alum)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template("alumnos.html", form=create_form)

@app.route("/detalles", methods=["GET"])
def detalles():
    id = request.args.get('id')
    alum = Alumnos.query.get(id) 
    
    if not alum:
        flash("Alumno no encontrado")
        return redirect(url_for('index'))
        
    return render_template("detalles.html", id=id, nombre=alum.nombre, apellidos=alum.apellidos, email=alum.email)

@app.route("/modificar", methods=['GET', 'POST'])
def modificar():
    id = request.args.get('id')
    alum = Alumnos.query.get(id)

   
    if not alum:
        flash("El alumno que intentas modificar no existe.")
        return redirect(url_for('index'))

    create_form = forms.UserForm(request.form)

    if request.method == 'GET':
       
        create_form.id.data = alum.id
        create_form.nombre.data = alum.nombre
        create_form.apellidos.data = alum.apellidos
        create_form.email.data = alum.email
        create_form.telefono.data = alum.telefono
        
    if request.method == 'POST':
     
        alum.nombre = create_form.nombre.data
        alum.apellidos = create_form.apellidos.data
        alum.email = create_form.email.data
        alum.telefono = create_form.telefono.data
        
        db.session.add(alum)
        db.session.commit()
        flash("Alumno actualizado correctamente")
        return redirect(url_for('index'))
        
    return render_template("modificar.html", form=create_form)

@app.route("/eliminar", methods=['GET', 'POST'])
def eliminar():
    id = request.args.get('id')
    alum = Alumnos.query.get(id)

    if not alum:
        flash("Registro no encontrado")
        return redirect(url_for('index'))

    create_form = forms.UserForm(request.form)

    if request.method == 'GET':
        create_form.id.data = alum.id
        create_form.nombre.data = alum.nombre
        create_form.apellidos.data = alum.apellidos
        create_form.email.data = alum.email
        
    if request.method == 'POST':
        db.session.delete(alum)
        db.session.commit()
        flash("Registro eliminado")
        return redirect(url_for('index'))
        
    return render_template("eliminar.html", form=create_form)

@app.route("/", methods=['GET', 'POST'])
@app.route("/index")
def index():
    alumno = Alumnos.query.all()
    return render_template("index.html", alumno=alumno)

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

if __name__ == '__main__':
    app.run()