import socket

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
    # sock.bind((HOST, PORT))
    sock.sendto(b'Hello, world', (HOST, PORT))
    data = sock.recv(1024)

print('Received', repr(data))