import sqlite3
from flask import Flask, request , session, g, redirect, abort, render_template, flash

# configuração 
DATABASE = "blog.db"
SECRET_KEY = 'gamer'

app = Flask(__name__)
app.config.from_object(__name__)

def conect_bd():
    return sqlite3.connect(app.config['DATABASE'])


@app.before_request
def antes_requisicao():
    g.bd = conect_bd()


@app.teardown_request
def depois_request(exc):
    g.bd.close()        

@app.route('/')
@app.route('/entradas')
def exibir_entradas():
    return render_template('entradas.html')

@app.route('/hello')
def pagina_inicial():
    return "Hello, pessoas"
