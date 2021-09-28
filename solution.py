# import socket module
from socket import *
# In order to terminate the program
import sys


def webServer(port=13331):
    serverSocket = socket(AF_INET, SOCK_STREAM)
    # Prepare a server socket
    serverSocket.bind(("", port))
    # Fill in start
    serverSocket.listen(1)
    # Fill in end
    while True:
        # Establish the connection
        # print('Ready to serve...')
        connectionSocket, addr = serverSocket.accept()
        try:
            try:
                message =  connectionSocket.recv(80).decode()
                filename = message.split()[1]
                f = open(filename[1:])
                outputdata =  f.read()
                # Send one HTTP header line into socket.
                # Fill in start
                # Fill in end
                response_header = "HTTP/1.1 200 OK\n"
                connectionSocket.send(response_header.encode())
                # Send the content of the requested file to the client
                for i in range(0, len(outputdata)):
                    connectionSocket.send(outputdata[i].encode())
                connectionSocket.send("\r\n".encode())
                connectionSocket.close()
            except IOError:
                # Send response message for file not found (404)
                # Fill in start
                # Fill in end
                not_found_header = "HTTP/1.1 404 Not Found\n"
                connectionSocket.send(not_found_header.encode())
                print(error)
            # Close client socket
            # Fill in start
            # Fill in end
            connectionSocket.close()
        except (ConnectionResetError, BrokenPipeError):
            pass
    serverSocket.close()
    sys.exit()  # Terminate the program after sending the corresponding data


if __name__ == "__main__":
    webServer(13331)