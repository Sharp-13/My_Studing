import socket
import pickle

HOST = '127.0.0.1'
PORT = 65435

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    text = input('Write text for sending: ')
    key = input('Enter key for encription: ')
    data = pickle.dumps((text, key))
    s.sendall(data)
    result = pickle.loads(s.recv(1024))

print('Received', repr(result))
