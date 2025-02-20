from flask import Flask, request,render_template,render_template_string
from Model.Firebase import Firebase
import os
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

firebase = Firebase()

@app.route("/")
def hello_world():
    return render_template('index.html') 

@app.route("/cadastrarItem")
def cadastrarItem():
    
    return render_template('cadastroItem.html')

@app.route("/processarItem", methods=["POST"])
def processarItem():
    item = request.form.get("item")
    requestItens = {
        "nome_item": item,
        "data_compra": request.form.get("date"),
        "categoria_item": request.form.get("categoria"),    
    }

    
    firebase.adicionarItem(requestItens)
    
    return f"<p>Item cadastrado: {item}</p>"

@app.route("/itens")
def getItens():

    documento_itens = firebase.getDocument("itens")
    
    if not documento_itens:
        documento_itens = {}
    
    return render_template_string('''
    <!DOCTYPE html>
    <html lang="pt-BR">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Lista de Itens</title>
        <style>
            table {
                width: 100%;
                border-collapse: collapse;
            }
            th, td {
                border: 1px solid black;
                padding: 8px;
                text-align: left;
            }
            th {
                background-color: #f2f2f2;
            }
        </style>
    </head>
    <body>
        <h2>Lista de Itens</h2>
        <table>
            <thead>
                <tr>
                    <th>ID</th>
                    <th>Nome</th>
                    <th>Data da Compra</th>
                    <th>Categoria</th>
                </tr>
            </thead>
            <tbody>
                {% for id, dados in documento_itens.items() %}
                <tr>
                    <td>{{ id }}</td>
                    <td>{{ dados['nome_item'] }}</td>
                    <td>{{ dados['data_compra'] }}</td>
                    <td>{{ dados['categoria_item'] }}</td>
                </tr>
                {% endfor %}
            </tbody>
        </table>
    </body>
    </html>
    ''', documento_itens=documento_itens)

if __name__ == "__main__":
    app.run(debug=True)	
