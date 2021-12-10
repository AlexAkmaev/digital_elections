import json
import socket
# from Storage import *


class ClientError(Exception):
    pass


class Client:
    def __init__(self, host='127.0.0.1', port=62000, timeout=None, buffer_size=1024):
        self.host = host
        self.port = port
        self.timeout = timeout
        self.buffer_size = buffer_size
        try:
            self.connection = socket.create_connection((host, port), timeout)
        except socket.error as err:
            raise ClientError("[Client]: Cannot create connection", err)

    def _send(self, data):
        try:
            self.connection.sendall(data)
        except socket.error as err:
            raise ClientError("Error sending data to server", err)

    def _read(self):
        try:
            data = self.connection.recv(self.buffer_size)
        except socket.error as err:
            raise ClientError("Error reading data from socket", err)
        return data

    def send_msg(self, fio, pub_key):
        data = {"fio": fio, "public_key": pub_key}
        self._send(json.dumps(data).encode('utf-8'))
        print("send_msg")
        response = self._read().decode()
        if not response.startswith('OK'):
            print('Incorrect response!')
        return response
