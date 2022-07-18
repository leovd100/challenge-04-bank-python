from cliente import Client
from verifica_cliente import verifica
def mostrar_dados(value):
    clientCriado = Client(value)
    lista_verificada = verifica(value)   
    for item in lista_verificada:
        clientCriado.popula_produto(item)
    return clientCriado
