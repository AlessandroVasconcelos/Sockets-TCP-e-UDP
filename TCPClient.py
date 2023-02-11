# python3 TCPClient.py

# inclui biblioteca de socket com todas as funcoes.
from socket import *

# endereço IP, 127.0.0.1.
serverIP = "127.0.0.1"

# porta do servidor.
serverPort = 12000

# cria socket TCP no cliente.
# AF_INET = endereco IPv4, SOCK_STREAM = TCP.
clientSocket = socket (AF_INET, SOCK_STREAM)

print("\nCliente TCP em execucao...\nObs: para sair use CTRL+X\n")

# cria conexao TCP para servidor, porta remota 12000.
clientSocket.connect((serverIP, serverPort))

# obtem entrada do teclado do usuario.
message = input("=== Digite caracteres minusculos:\n")

# enquanto a mesagem for diferente de CTRL+X.
while message != "\x18":
    # no TCP nao eh necessario anexar IP e porta para o envio da mensagem ao servidor TCP.
    clientSocket.send(message.encode())

    # recebe dados do servidor TCP, em um tamanho de buffer de 1024 bytes por vez .    
    modifiedMessage = clientSocket.recv(1024)
    
    print("=== Resposta do servidor:")
    print(modifiedMessage.decode("utf-8"),"\n")
    
    message = input("=== Digite caracteres minusculos:\n")

# fecha o socket TCP.
clientSocket.close()
