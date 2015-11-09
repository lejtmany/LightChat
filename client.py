import asyncio
import sys
import json

class EchoClientProtocol(asyncio.Protocol):
    def __init__(self, loop, uname,to):
        self.loop = loop
        self.to = to
        self.uname = uname

    def connection_made(self, transport):
        print("Connection Made")
        self.transport = transport
        self.loop.add_reader(sys.stdin, self.write_to_server)
        self.transport.write(json.dumps({'from:':self.uname,'to':'uname_setup', 'message':self.uname}).encode())

    def write_to_server(self):
        message = sys.stdin.readline()
        print("\033[A                             \033[A")
        print('me> {}'.format(message), end='')
        self.transport.write(json.dumps({'to':self.to, 'message': message}).encode())

    def data_received(self, data):
        print('{}'.format(data.decode()))

    def connection_lost(self, exc):
        print('The server closed the connection')
        print('Stop the event lop')
        self.loop.stop()

loop = asyncio.get_event_loop()
uname = input('Enter user name:')
recip = input('Enter recipient:')
coro = loop.create_connection(lambda: EchoClientProtocol(loop, uname,recip),
                              'localhost', 8888)
loop.run_until_complete(coro)
loop.run_forever()
loop.close()
