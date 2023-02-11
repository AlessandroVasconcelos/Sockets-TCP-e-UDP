# python3 UDPServer.py

# inclui biblioteca de socket com todas as funcoes.
from socket import *

# endereço IP
serverIP = ""

# porta do servidor.
serverPort = 12000

# ('', 12000)
server = (serverIP, serverPort)

# cria socket UDP.
# AF_INET = endereço IPv4, SOCK_DGRAM = UDP.
serverSocket = socket(AF_INET, SOCK_DGRAM)

# atribui um endereço IP e um numero de porta a uma instancia de soquete.
serverSocket.bind(server)

print("\nServidor UDP em execucao...\n")

# laço eterno.
while 1:
    # ler do cliente UDP a mensagem, obtendo endereço do cliente (IP e porta).
    message, clientAddress = serverSocket.recvfrom(2048)
    
    # decodifica uma string codificada em UTF-8.
    message = message.decode("utf-8")
    
    # exibe ip do cliente e a mensagem recebida do cliente.
    print(clientAddress, message)
    
    # mesagem modificada recebe a mensagem do cliente em letras maiusculas.
    modifiedMessage = message.upper()
    # envia string em maiusculas de volta para o cliente de forma codificada.
    serverSocket.sendto(modifiedMessage.encode(), clientAddress)
