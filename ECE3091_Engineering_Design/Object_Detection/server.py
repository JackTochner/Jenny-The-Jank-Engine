import socket
# create the socket
# AF_INET == ipv4
# SOCK_STREAM == TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#In the case of the server, you will bind a socket to some port on the server (localhost). 
# In the case of a client, you will connect a socket to that server, on the same port that the server-side code is using.
s.bind((socket.gethostname(),1234))
#listen for incoming connections
s.listen(5)

while True:
    # now our endpoint knows about the OTHER endpoint.
    clientsocket, address = s.accept()
    print(f"Connection from {address} has been established.")