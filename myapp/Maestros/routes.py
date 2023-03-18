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

maestros=Blueprint("maestros",__name__)
csrf = CSRFProtect()

@maestros.route("/getMaestros",methods=["GET","POST"])
def getMaestros():
    creat_form=forms.MaestroForm(request.form)
    maestro = ""
    try:
        connection = get_connection()
        with connection.cursor() as cursor:
            cursor.execute('call consulta_maestros()')
            resulset=cursor.fetchall()
            maestro = resulset
    except Exception as ex:
        print(ex)

    return render_template("ABCompletoMaestros.html",form=creat_form,maestro=maestro)

@maestros.route("/insertarMaes", methods=["GET","POST"])
def index():
    create_form=forms.MaestroForm(request.form)
    if request.method=="POST":
        nombre=create_form.nombre.data
        apellidos=create_form.apellidos.data
        email=create_form.email.data
        materia=create_form.materia.data

        try:
            connection=get_connection()
            with connection.cursor() as cursor:
                cursor.execute('CALL agrega_maestro(%s, %s, %s, %s)', (nombre, apellidos, email, materia))
            connection.commit()
            connection.close()
        except Exception as ex:
            print(ex)
            
        return redirect(url_for("maestros.getMaestros"))
    return render_template("agregarMaestro.html",form=create_form)

@maestros.route("/modificarMaes",methods=["GET","POST"])
def modificar():
    create_form=forms.MaestroForm(request.form)
    idM = 0
    nombre = ""
    apellidos = ""
    email = ""
    materia = ""
    fecha = "";
    
    if request.method=="GET":
        id=request.args.get("id")
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute('call consultar_maestro(%s)',(id))
                resulset=cursor.fetchall()
                for row in resulset:
                    print(row)
        except Exception as ex:
            print(ex)

        idM, nombre, apellidos, email, materia, fecha = row
        

        create_form.id.data=idM
        create_form.nombre.data=nombre
        create_form.apellidos.data=apellidos
        create_form.email.data=email
        create_form.materia.data=materia

    if request.method=="POST":
        id=create_form.id.data
        nombre=create_form.nombre.data
        apellidos=create_form.apellidos.data
        email=create_form.email.data
        materia=create_form.materia.data

        try:
            connection=get_connection()
            with connection.cursor() as cursor:
                cursor.execute('call modificar_maestro(%s, %s, %s, %s, %s)',(id, nombre, apellidos, email, materia))
            connection.commit()
            connection.close()
        except Exception as ex:
            print(ex)
        
        return redirect(url_for("maestros.getMaestros"))
    return render_template("modificarMaestros.html",form=create_form)

@maestros.route("/eliminarMaes",methods=["GET","POST"])
def eliminar():
    create_form=forms.MaestroForm(request.form)
    if request.method=="GET":
        id=request.args.get("id")
        id=request.args.get("id")
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute('call consultar_maestro(%s)',(id))
                resulset=cursor.fetchall()
                for row in resulset:
                    print(row)
        except Exception as ex:
            print(ex)

        idM, nombre, apellidos, email, materia, fecha = row
        

        create_form.id.data=idM
        create_form.nombre.data=nombre
        create_form.apellidos.data=apellidos
        create_form.email.data=email
        create_form.materia.data=materia
    if request.method=="POST":
        id=create_form.id.data
        try:
            connection=get_connection()
            with connection.cursor() as cursor:
                cursor.execute('call eliminar_maestro(%s)',(id))
            connection.commit()
            connection.close()
        except Exception as ex:
            print(ex)
        
        return redirect(url_for("maestros.getMaestros"))
    return render_template("eliminarMaestros.html",form=create_form)