        ## Networking with Python ##
    # Trasport Control Protocol (TCP) #

# Built on top of IP (Internet Protocol)
# Assumes IP might lose some data
    # stores and retransmits data if it seems to be lost
# Handles "flow control" using a transmit window
# Provides a nice reliable pipe

# In computer networking, an internet socket or networksocket is an endpoint of a bidirectional inter-process 
# communication flow across and Internet Protocol based computer network, such as the internet


#------------------------------------------------------------------------------------#

    # TCP Port Numbers #

# A port is an application-specific or process- specific software communications endpoint
# It allows multiple networked applications to coexist on the same server.
# There is a list of well-known TCP port numbers
    # http://en.wikipedia.org/TCP_and_UDPport
 
 #------------------------------------------------------------------------------------#

     # Sockets in Python #
# Python has built-in support for TCP Sockets

import socket
mysock = socket.socket(socket.AF_INET, socket.sock_STREAM)
mysock.connect( ('data.pr4e.org', 80) )