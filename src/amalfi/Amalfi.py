import socketserver
import socket
import sys

def start(server, host='localhost', port=9999):
    server = socketserver.TCPServer((host, port), server)
    server.serve_forever()

class AmalfiServer(socketserver.BaseRequestHandler):
    """Class that runs Amalfi Server."""

    # def start(self, host='localhost', port=9999):
    #     self.server = socketserver.TCPServer((host, port), self.__class__)
    #     self.server.serve_forever()

    def get_port(self):
        pass

    def handle(self):
        # self.request is the TCP socket connected to the client
        self.data = self.request.recv(1024).strip()
        print("{} wrote:".format(self.client_address[0]))
        print(self.data)
        # just send back the same data, but upper-cased
        self.request.sendall(self.data)


class AmalfiContext():
    """Context manager for Amalfi."""

    def __init__(self, host='localhost', port=9999):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = host
        self.port = port

    def connect(self, host, port):
        if self.host == None and self.port == None:
            self.host = host
            self.port = port
            self.sock.connect((self.host, self.port))
        else:
            raise Exception('Already connected to {}:{}'.format(self.host, self.port))

    def close(self):
        self.sock.close()
        self.host = None
        self.port = None

    def emit(self, variable):
        self.sock.sendall(bytes(str(variable) + "\n", "utf-8"))

    def get(self, variable):
        pass

    def list_all_objects(self):
        pass