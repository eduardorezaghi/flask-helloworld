"""
Módulo app.py
App: "Hello World!" com o micro-framework Flask
Baseado em: https://bit.ly/3eD7BkU
https://flask.palletsprojects.com/en/2.0.x/
"""
from flask import Flask
from flask import render_template
from flask import jsonify

app = Flask(__name__)

# Rota raiz "/"


@app.route("/")
def hello():
    """
    View raiz "Hello World"
    """
    return "Olá, mundo!"


# Rota "rota1"
@app.route("/rota1")
def view_rota1():
    """
    View /rota1 que retorna uma representação string
    """
    return "Essa é a view da /rota1"


# Rota personalizada que aceita um parâmetro <nome>
@app.route("/rota2/<nome>")
def view_rota2(nome):
    """
    View /rota2 que retorna uma representação string com variável
    """
    return f"Bem vindo, <b>{nome}</b>! Essa é a view da rota2!"


# Renderização do conteúdo por uma string simples
@app.route("/ola")
def view_str() -> str:
    """
    View que retorna a exibição como string simples
    """
    return "Esse é o conteúdo representado como uma string simples."


# Renderização por template Jinja!
@app.route("/ola/<seu_nome>")
def view_template(seu_nome):
    """
    View que utiliza o Jinja2 para exibir uma página HTML
    """
    return render_template("index.html", nome=seu_nome)


# Rota que retorna um objeto JSON
@app.route("/api")
def view_json():
    """View que retorna um JSON chave=valor

    -- 'mensagem' = chave representando a mensagem a ser encapsulada

    -- 'Bem-vindo a sua primeira API REST!' = valor hardcoded representando a mensagem
    """
    return jsonify(
        {
            'mensagem': 'Bem-vindo a sua primeira API REST!'
        }
    )
