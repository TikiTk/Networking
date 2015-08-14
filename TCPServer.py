__author__ = 'Tk Mphahlele'
''' 14-Aug-2015
    CSC311
    2:18 AM
    '''
''' TCP server that can be accessed from client(web browser)
    Since all browsers look for favicon.ico in the root directory of the server
    include the favicon.ico so that when the browser sends out a second request the program
    doesn't bomb out
    '''

from socket import *
serverPort = 5005
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(("localhost", serverPort))

serverSocket.listen(1)
print("The server is ready to receive")
while 1:
    connectionSocket, addr = serverSocket.accept()
    sentence = connectionSocket.recv(1024)


    try:
        newWord = sentence.split()[1]
        connectionSocket.send(bytes('HTTP/1.1 200 OK \r\n\r\n'.encode('utf-8')))
        with open(newWord[1:], 'rb') as f: #open entire file as bytes to enable writing to socket(socket only takes in bytes
            connectionSocket.send(f.read())  #tentire file is sent through socket as bytes
        connectionSocket.close()


    except IOError:
        connectionSocket.send('HTTP/1.1 404 Not found: The requested document does not exist on this server.'.encode('utf-8'))
        serverSocket.close()



