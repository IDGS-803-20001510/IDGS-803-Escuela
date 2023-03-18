
from flask import Flask, redirect, render_template
import forms

from flask import jsonify
from config import DevelopmentConfig
from flask_wtf.csrf import CSRFProtect
from models import db
from models import Alumnos

from Alumnos.routes import alumnos
from Maestros.routes import maestros

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
csrf = CSRFProtect()

@app.route("/", methods=['GET'])
def home():
    return render_template('index.html')

app.register_blueprint(alumnos)
app.register_blueprint(maestros)

if __name__ == '__main__':
    csrf.init_app(app)
    db.init_app(app)
    with app.app_context():
        db.create_all()
    app.run(port=3000)