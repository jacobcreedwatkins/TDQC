import socket

# This can also be accomplished by using s = socket.socket() due to AF_INET and SOCK_STREAM being defaults
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ipaddr = '127.0.0.1'
port = 54321

s.connect((ipaddr, port))


# In the above, we are creating a socket with address family = AF_INET (IPv4) and type = SOCK_STREAM (TCP)
# We then define an ip adress amd port pair
# Next we call the socket object 'connect(address)' tied to IPv4 and TCP we mapped to the variable 's'
# This will connect to the remote address and port we provided over IPv4 and TCP
# We will add to this connection by attempting to send a mesage through the connection and waiting for a response
# To send a stringa s a bytes-like object, add the prefix 'b' to the string. \n is used to go to the next line

s.send(b'Hello\n')

# It is recommended that the buffersize used with revvfrom is a power of 2 and not a very large number of bits

response, conn = s.recvfrom(1024)

#In order to revieve a messag ethat is sent a a bytes like object, you must decode into utf-8 (default)

print(response.decode())

s.close(), conn = s.recvfrom(1024)

#In order to revieve a message that is sent as a bytes like object, you must decode into utf-8 (default)

print(response.decode())

s.close()
