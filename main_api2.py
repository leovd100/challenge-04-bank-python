import imp
from flask import Flask, request, Response
import json
from mostrar_dados import mostrar_dados


app = Flask(__name__)


@app.route('/credito', methods = ['GET', 'POST'])
def credito():
    if request.method == 'POST':
        payload_response = json.loads(request.data)
        client_list = []
        for key,value in payload_response.items():
            client_list.append(mostrar_dados(value).__dict__)
        return json.dumps(client_list)
    elif request.method == 'GET':
        return 'Online'
  


if __name__=='__main__':
    app.run(debug=True)