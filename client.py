import asyncio

class EchoClientProtocol(asyncio.Protocol):
    def __init__(self, loop):
        self.loop = loop

    def connection_made(self, transport):
        # transport.write(self.message.encode())
        # print('Data sent: {!r}'.format(self.message))
        print("Connection Made")
        a = self.loop.ensure_future(listen_for_input())
        self.loop.run_until_complete(a)

    async def listen_for_input(self):
        while True:
            await input()

    def data_received(self, data):
        print('Data received: {!r}'.format(data.decode()))

    def connection_lost(self, exc):
        print('The server closed the connection')
        print('Stop the event lop')
        self.loop.stop()

loop = asyncio.get_event_loop()
coro = loop.create_connection(lambda: EchoClientProtocol(loop),
                              'localhost', 8888)
loop.run_until_complete(coro)
loop.run_forever()
loop.close()
