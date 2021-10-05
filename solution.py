from socket import *


def smtp_client(port=1025, mailserver='127.0.0.1'):
   msg = "\r\n My message"
   endmsg = "\r\n.\r\n"

   # Choose a mail server (e.g. Google mail server) if you want to verify the script beyond GradeScope
   mailserver = (mailserver, 1025)  # Fill in start #Fill in end

   # Create socket called clientSocket and establish a TCP connection with mailserver and port
   # Fill in start
   clientSocket = socket(AF_INET, SOCK_STREAM)
   clientSocket.connect(mailserver)
   # Fill in end

   recv = clientSocket.recv(1024).decode()
   # print(recv)
   if recv[:3] != '220':
       print('220 reply not received from server.')

   # Send HELO command and print server response.
   heloCommand = 'HELO Alice\r\n'
   clientSocket.send(heloCommand.encode())
   hello_response = clientSocket.recv(1024).decode()
   # print(hello_response)
   if hello_response[:3] != '250':
       print('250 reply not received from server.')

   # Send MAIL FROM command and print server response.
   # Fill in start
   mailFrom = "MAIL FROM:<ph2303@nyu.edu.com>\r\n"
   clientSocket.send(mailFrom.encode())
   mail_from_response = clientSocket.recv(1024)
   mail_from_response = mail_from_response.decode()
   # print(recv2)
   # Fill in end

   # Send RCPT TO command and print server response.
   # Fill in start
   rcptTo = "RCPT TO:<prestonharms5@gmail.com>\r\n"
   clientSocket.send(rcptTo.encode())
   rcpt_to_response = clientSocket.recv(1024)
   rcpt_to_response = rcpt_to_response.decode()
   # print(rcpt_to_response)
   # Fill in end

   # Send DATA command and print server response.
   # Fill in start
   data = "DATA\r\n"
   clientSocket.send(data.encode())
   data_response = clientSocket.recv(1024)
   data_response = data_response.decode()
   # print(data_response)
   # Fill in end

   # Send message data.
   # Fill in start
   clientSocket.send(msg.encode())
   # Fill in end

   # Message ends with a single period.
   # Fill in start
   clientSocket.send(endmsg.encode())
   msg_response = clientSocket.recv(1024)
   # print(msg_response.decode())
   # Fill in end

   # Send QUIT command and get server response.
   # Fill in start
   quit = "QUIT\r\n"
   clientSocket.send(quit.encode())
   quit_response = clientSocket.recv(1024)
   # print(quit_response.decode())
   clientSocket.close()
   # Fill in end

if __name__ == '__main__':
   smtp_client(1025, '127.0.0.1')