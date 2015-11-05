import asyncio
import sys

class EchoClientProtocol(asyncio.Protocol):
    def __init__(self, loop, to):
        self.loop = loop
        self.to = to

    def connection_made(self, transport):
        print("Connection Made")
        self.transport = transport
        self.loop.add_reader(sys.stdin, self.write_to_server)

    def write_to_server(self):
        self.transport.write(sys.stdin.readline().encode())

    def data_received(self, data):
        print('Data received: {!r}'.format(data.decode()))

    def connection_lost(self, exc):
        print('The server closed the connection')
        print('Stop the event lop')
        self.loop.stop()

loop = asyncio.get_event_loop()
coro = loop.create_connection(lambda: EchoClientProtocol(loop, 'kdog'),
                              'localhost', 8888)
loop.run_until_complete(coro)
loop.run_forever()
loop.close()
