#!/usr/bin/env python
#coding: utf-8

from asyncore import dispatcher
from asynchat import async_chat
import socket, asyncore

PORT = 5005

class ChatSession(async_chat):
    def __init__(self, sock):
        async_chat.__init__(self, sock)
        self.set_terminator('\r\n')
        self.data = []

    def collect_incoming_data(self, data):
        self.data.append(data)

    def found_terminator(self):
        line = ''.join(self.data)
        self.data = []

        print line


class ChatServer(dispatcher):
    def __init__(self, port):
        dispatcher.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.set_reuse_addr()
        self.bind(('', port))
        self.listen(5)
        self.sessions = []

    def handle_accept(self):
        conn, add = self.accept()
        self.sessions.append(ChatSession(conn))


if __name__ == '__main__':
    s = ChatServer(PORT)
    try:
        
        asyncore.loop()
    except KeyboardInterrupt:
        pass