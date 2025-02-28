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

    try:
        itens = request.form.getlist('item[]')
        validades = request.form.getlist('date_validade[]')
        categorias = request.form.getlist('categoria[]')
        lista_itens = [
            {"nome_item": itens[i], "validade_item": validades[i], "categoria_item": categorias[i]}
            for i in range(len(itens))
        ]

        resquestValue = {
            "data_compra": request.form.get("date"),
            "local_compra": request.form.get("local"),
            "valor_compra": request.form.get("valor"),
            "itens": lista_itens
        }

        response = firebase.adicionarItem(resquestValue)
        return f"<p> ItenS Cadastrados com sucesso:</p>"
    except :
        return f"<p> Não foi possivel Cadastrar:</p>"

@app.route("/itens")
def getItens():

    documento_itens = firebase.getDocument("itens")
    
    if not documento_itens:
        documento_itens = {}
    
    return render_template("listaItens.html", documento_itens=documento_itens)

if __name__ == "__main__":
    app.run(debug=True)	
