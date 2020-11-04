<<<<<<< HEAD
        ## Networking: Write a Web Browser ##
    # An HTTP Request in Python #

import socket
mysock = socket. socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect ( ('data.pr4e.org', 80) )
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\n\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if (len(data) < 1):
        break
    print(data.decode())
mysock.close()

=======
        ## Networking: Write a Web Browser ##
    # An HTTP Request in Python #

import socket
mysock = socket. socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect ( ('data.pr4e.org', 80) )
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\n\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if (len(data) < 1):
        break
    print(data.decode())
mysock.close()

>>>>>>> 1cbe16609e7369aced3579647b9cafd732cd7546
#------------------------------------------------------------------------------------#