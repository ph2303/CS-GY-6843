from socket import *

serverName = 'localhost'
serverPort = 13331
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
file = 'GET /helloworld.html'
clientSocket.send(file.encode())
modifiedMessage, serverAddress = clientSocket.recvfrom(1024)
print('From Server: ', modifiedMessage.decode())
# clientSocket.close()