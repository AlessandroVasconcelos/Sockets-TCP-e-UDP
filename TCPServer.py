# python3 TCPServer.py

# inclui biblioteca de socket com todas as funcoes.
from socket import *

# endereço IP
serverIP = ""

# porta do servidor.
serverPort = 12000

# ('', 12000)
server = (serverIP, serverPort)

# cria socket TCP de acolhimento.
# AF_INET = endereço IPv4, SOCK_STREAM = TCP.
serverSocket = socket(AF_INET, SOCK_STREAM)

# atribui o IP e a porta a uma instância de soquete.
serverSocket.bind(server)

# servidor começa a ouvir pedidos TCP que chegam.
serverSocket.listen(1)

print("\nServidor TCP em execucao...\n")

# laço eterno.
while 1:
    # aceita uma solicitação de conexao recebida de um cliente TCP.
    connectionSocket, clientAddress = serverSocket.accept()

    while 1:
        # ler bytes do cliente TCP (mas nao enderecos como no UDP). 
        message = connectionSocket.recv(1024)
        
        if not message: break

        # exibe ip do cliente e a mensagem recebida. 
        print(clientAddress,message.decode("utf-8"))
        
        # modifiedMessage recebe string em letras maiusculas.
        modifiedMessage = message.upper()
        
        # envia string em maiusculas de volta para o cliente.
        connectionSocket.send(modifiedMessage)
  
# fecha conexão a esse cliente(mas não o socket de acolhimento)
connectionSocket.close()
