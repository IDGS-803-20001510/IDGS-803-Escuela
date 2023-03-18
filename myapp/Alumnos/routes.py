from flask import Blueprint
from flask import Flask, redirect, render_template
from flask import request
from flask import url_for
import forms
from db import get_connection

from flask import jsonify
from config import DevelopmentConfig
from flask_wtf.csrf import CSRFProtect
from models import db
from models import Alumnos


alumnos=Blueprint("alumnos",__name__)
csrf = CSRFProtect()

@alumnos.route("/getAlum",methods=["GET","POST"])
def getalum():

    creat_form=forms.UserForm(request.form)
    alumno = ""
    try:
        connection = get_connection()
        with connection.cursor() as cursor:
            cursor.execute('call consulta_alumnos()')
            resulset=cursor.fetchall()
            alumno = resulset
    except Exception as ex:
        print(ex)

    return render_template("ABCompleto.html", form=creat_form, alumno=alumno)

@alumnos.route("/insertarAlum", methods=["GET","POST"])
def index():
    create_form=forms.UserForm(request.form)
    if request.method=="POST":

        nombre=create_form.nombre.data,
        apellidos=create_form.apellidos.data,
        email=create_form.email.data

        try:
            connection=get_connection()
            with connection.cursor() as cursor:
                cursor.execute('call agrega_alumno(%s, %s, %s)',(nombre,apellidos,email))
            connection.commit()
            connection.close()
        except Exception as ex:
            print(ex)
        
        return redirect(url_for("alumnos.getalum"))
    return render_template("agregar.html",form=create_form)

@alumnos.route("/modificarAlum",methods=["GET","POST"])
def modificar():
    create_form=forms.UserForm(request.form)
    idA = 0
    nombre = ""
    apellidos = ""
    email = ""
    fecha = "";
    
    if request.method=="GET":
        id=request.args.get("id")
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute('call consultar_alumno(%s)',(id))
                resulset=cursor.fetchall()
                for row in resulset:
                    idA, nombre, apellidos, email, fecha = row
        except Exception as ex:
            print(ex)
        create_form.id.data=idA
        create_form.nombre.data=nombre
        create_form.apellidos.data=apellidos
        create_form.email.data=email

    if request.method=="POST":
        id=create_form.id.data
        nombre=create_form.nombre.data
        apellidos=create_form.apellidos.data
        email=create_form.email.data

        try:
            connection=get_connection()
            with connection.cursor() as cursor:
                cursor.execute('call modificar_alumno(%s, %s, %s, %s)',(id,nombre,apellidos, email))
            connection.commit()
            connection.close()
        except Exception as ex:
            print(ex)
        
        return redirect(url_for("alumnos.getalum"))
    return render_template("modificar.html",form=create_form)

@alumnos.route("/eliminarAlum",methods=["GET","POST"])
def eliminar():
    create_form=forms.UserForm(request.form)
    idA = 0
    nombre = ""
    apellidos = ""
    email = ""
    fecha = "";
    if request.method=="GET":
        id=request.args.get("id")
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute('call consultar_alumno(%s)',(id))
                resulset=cursor.fetchall()
                for row in resulset:
                    idA, nombre, apellidos, email, fecha = row
        except Exception as ex:
            print(ex)
        create_form.id.data=idA
        create_form.nombre.data=nombre
        create_form.apellidos.data=apellidos
        create_form.email.data=email
    if request.method=="POST":
        id=create_form.id.data
        try:
            connection=get_connection()
            with connection.cursor() as cursor:
                cursor.execute('call eliminar_alumno(%s)',(id))
            connection.commit()
            connection.close()
        except Exception as ex:
            print(ex)

        return redirect(url_for("alumnos.getalum"))
    return render_template("eliminar.html",form=create_form)