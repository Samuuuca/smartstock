import requests
import dotenv from load_dotenv
import os

load_dotenv()
class Infosimples:

  def __init__(self):
    self.url = 'https://api.infosimples.com/api/v2/consultas'


  def getCuponByChave(self, chave):
    urlConsulta = f'{self.url}/sefaz/sp/cfe'
    args = {
      "chave":   chave,
      "token":   os.getenv('TOKEN_INFOSIMPLES'),
      "timeout": 300
    }

    response = requests.post(urlConsulta, args)
    response_json = response.json()
    response.close()

    if response_json['code'] == 200:
      print("Retorno com sucesso: ", response_json['data'])

    elif response_json['code'] in range(600, 799):

      mensagem = "Resultado sem sucesso. Leia para saber mais: \n"
      mensagem += "Código: {} ({})\n".format(response_json['code'], response_json['code_message'])
      mensagem += "; ".join(response_json['errors'])
      print(mensagem)

    print("Cabeçalho da consulta: ", response_json['header'])
    print("URLs com arquivos de visualização (HTML/PDF): ", response_json['site_receipts'])