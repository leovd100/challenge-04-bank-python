from ast import arg
from pydoc import cli
from urllib import response
from flask import Flask, jsonify, request, Response
import json

app = Flask(__name__)

#Emprestimo_consignado
#Emprestimo_pessoal
#Empresitmo_garantia




@app.route('/credito', methods = ['GET', 'POST'])
def credito():
    if request.method == 'POST':
        payload_response = json.loads(request.data)
        client_list = []
        for key,value in payload_response.items():
            client_list.append(criandoClient(value))
        return json.dumps(client_list)
    elif request.method == 'GET':
        return 'Online'
    

def verifica(age , uf, renda):
    list_emprestimo = [{'tipo_emprestimo':'Eprestimo_pessoal', 'taxa': 2}]

    if renda >= 5000:
        if age <= 30:
            list_emprestimo.append( {'tipo_emprestimo': 'Credito_consignato','taxa': 2})
            list_emprestimo.append( {'tipo_emprestimo': 'Emprestimo_com_garantia', 'taxa': 2})
        else:
            list_emprestimo.append({'tipo_emprestimo':'Credito_consignato', 'taxa': 2})
    elif renda >= 3000 and uf == 'sp' or (renda < 3000 and age <= 30 and uf == 'sp'):
        list_emprestimo.append({'tipo_emprestimo':'Emprestimo_com_garantia', 'taxa': 2})
   
    
    return list_emprestimo



def criandoClient(value):

    client = {
        "name": "",
        "cpf": "",
        "age": 0,
        "uf": "",
        "renda_mensal": 0,
        "produto_emprestimo" : []
    }

    client['name'] = value['name']
    client['cpf'] = value['cpf']
    client['age'] = value['age']
    client['uf'] = value ['uf']
    client['renda_mensal'] = value['renda_mensal']

    lista_verificada = verifica(value['age'], value['uf'], value['renda_mensal']);
    for valores in lista_verificada:
        client['produto_emprestimo'].append(valores)

   

    return client




if __name__=="__main__":
    app.run(debug=True)