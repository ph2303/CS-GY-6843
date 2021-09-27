from socket import *

serverPort = 12000
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print('Server is Listening')
while True:
    connectedSocket, addr = serverSocket.accept()
    sentence = connectedSocket.recv(1024).decode()
    capitalizedSentence = sentence.upper()
    connectedSocket.send(capitalizedSentence.encode())
    connectedSocket.close()
