# Exemplo basico socket (lado passivo)

import socket
import json
import calculadora

HOST = ''
PORT = 5000

operacoes = calculadora.operacoes()

sock = socket.socket() 

sock.bind((HOST, PORT))

sock.listen(1) 

novoSock, endereco = sock.accept() 
print ('Conectado com: ', endereco)

while True:
	data = json.loads(novoSock.recv(1024).decode('UTF-8'))
	if not data: break
	else:

		operacao = operacoes[[*data.keys()][0]]
		novoSock.send(str(operacao([*data.values()][0][0]
			,[*data.values()][0][1])).encode())
    		


novoSock.close() 


sock.close() 
