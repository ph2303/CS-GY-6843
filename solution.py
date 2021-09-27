# import socket module
from socket import *
# In order to terminate the program
import sys
import time


def webServer(port=13331):
    serverSocket = socket(AF_INET, SOCK_STREAM)
    # Prepare a server socket
    serverSocket.bind(('', port))
    serverSocket.listen(1)
    while True:
        # Establish the connection
        print('Ready to serve...')
        connectionSocket, addr = serverSocket.accept()
        print('Address:')
        print(addr)
        try:
            try:
                message = connectionSocket.recv(1024).decode()
                print('Message Received: ' + message)
                filename = message
                f = open(filename)
                outputdata = f.read()
                # Send one HTTP header line into socket.
                response_header = "200 OK"
                connectionSocket.send(response_header.encode())
                connectionSocket.send("\r\n".encode())
                # Send the content of the requested file to the client
                for i in range(0, len(outputdata)):
                    connectionSocket.send(outputdata[i].encode())
                f.close()
                connectionSocket.send("\r\n".encode())
            except IOError as error:
                print("File not found. Serving 404 page.")
                print(error)
                not_found_header = "404 Not Found"
                connectionSocket.send(not_found_header.encode())
            connectionSocket.close()
        except (ConnectionResetError, BrokenPipeError):
            pass
    serverSocket.close()
    sys.exit()  # Terminate the program after sending the corresponding data


if __name__ == "__main__":
    webServer(13331)
