from socket import *

serverName = 'localhost'
serverPort = 13331
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
file = 'helloworld.html'
clientSocket.send(file.encode())
modifiedMessage, serverAddress = clientSocket.recvfrom(4096)
print('From Server: ', modifiedMessage.decode())
# clientSocket.close()