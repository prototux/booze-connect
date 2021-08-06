import socket

class Device:
    def __init__(self, mac_addr):
        self.mac_addr = mac_addr
        self.socket = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)

    def connect(self):
        self.socket.connect((self.mac_addr, 8))
        self.io = self.socket.makefile('rwb')

    def write(self, data):
        self.io.write(data)
        self.io.flush()

    def read(self, length):
        return self.io.read(length)

