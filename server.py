import asyncio
import json


class EchoServerClientProtocol(asyncio.Protocol):
    def __init__(self):
        self.connections = {}

    def connection_made(self, transport):
        peername = transport.get_extra_info('peername')
        print('Connection from {}'.format(peername))
        self.transport = transport

    def data_received(self, data):
        tup = json.loads(data.decode())
        print('Data received from {!r}: {!r}'.format(tup['to'], tup['message']))
        to = tup['to']
        message = tup['message']
        if to == 'uname_setup':
            self.connections[message] = self.transport
        elif to in self.connections.keys():
            self.connections[to].write('{} says: {}'.format(tup['uname'],tup['message']).encode())
        print(self.connections)

loop = asyncio.get_event_loop()
# Each client connection will create a new protocol instance
coro = loop.create_server(EchoServerClientProtocol, 'localhost', 8888)
server = loop.run_until_complete(coro)

# Serve requests until Ctrl+C is pressed
print('Serving on {}'.format(server.sockets[0].getsockname()))
try:
    loop.run_forever()
except KeyboardInterrupt:
    pass

# Close the server
server.close()
loop.run_until_complete(server.wait_closed())
loop.close()