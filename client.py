import socket

s = socket.socket()
host = 'localhost'
ip = socket.gethostbyname(host)
s.connect((ip, 8888))
print('connected to {}'.format(ip) )
s.send("booyah".encode())
reply = s.recv(4096)
print(reply)
s.close()