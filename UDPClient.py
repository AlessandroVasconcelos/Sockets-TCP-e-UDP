# python3 UDPClient.py

# inclui biblioteca de socket com todas as funcoes.
from socket import *

# endereço IP, localhost = 127.0.0.1.
serverIP = "127.0.0.1"

# porta do servidor.
serverPort = 12000

# anexa nome e numero da porta do servidor ('127.0.0.1', 12000)
server = (serverIP, serverPort)

# cria socket UDP no cliente.
# AF_INET = endereço IPv4, SOCK_DGRAM = UDP.
clientSocket = socket(AF_INET, SOCK_DGRAM)

print("\nCliente UDP em execucao... \nObs: para sair use CTRL+X\n")

# obtém entrada do teclado do usuario.
message = input("=== Digite caracteres minusculos:\n")
#modifiedMessage = None

# enquanto a mesagem for diferente de CTRL+X.
while message != "\x18":
    # anexa IP e porta do servidor a mensagem e envia pelo socket ao servidor.
    clientSocket.sendto(message.encode(), server)

    # ler caracteres respondidos do servidor UDP.
    modifiedMessage,serverAddress = clientSocket.recvfrom(2048)
    
    # exibe a mensagem que foi modificada pelo servidor de forma decodificada.
    print("=== Resposta do servidor:")
    print(modifiedMessage.decode("utf-8"),"\n")
    
    message = input("=== Digite caracteres minusculos:\n")

# fecha socket.
clientSocket.close()
