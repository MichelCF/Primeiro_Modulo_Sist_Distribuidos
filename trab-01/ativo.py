# Exemplo basico socket (lado ativo)

import socket
import json

HOST = 'localhost' 
PORT = 5000


sock = socket.socket() 


sock.connect((HOST, PORT))

while True:
    print('Digite a Operação ou Sair para sair')
    chave = input()
    if chave =='Sair': break

    print('Digite o primeiro número')
    valor1 = int(input())
    print('Digite o segundo número')
    valor2 = int(input())

    operacao =json.dumps({chave : [valor1,valor2]})
    sock.send(operacao.encode())
    dados = sock.recv(1024)


    print(dados.decode('UTF-8'))


sock.close() 
