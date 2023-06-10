import socket

class socket_client:
    def socket_send(self, msg):
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect(('127.0.0.1', 114))
        client.send(msg.encode())
        from_server = client.recv(4096)
        # client.close()
        print (from_server.decode())