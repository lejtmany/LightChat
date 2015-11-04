import socket
HOST=''
PORT = 8888
s=socket.socket()
s.bind((HOST,PORT))
print('bound socket')
s.listen(10)
conn, addr = s.accept()
text = conn.recv(2096)
print(text)
conn.sendall('message from server...'.encode())
print('connected successfully with {}{}'.format(addr[0], addr[1]))