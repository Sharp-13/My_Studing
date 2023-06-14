import socket
import pickle

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('localhost', 65435)
print('starting up on {} port {}'.format(*server_address))
sock.bind(server_address)

sock.listen(1)

while True:
    print('waiting for a connection')
    connection, client_address = sock.accept()
    try:
        print('connection from', client_address)

        while True:
            data = connection.recv(1024)
            print('received {!r}'.format(data))
            text = pickle.loads(data)[0]
            key = pickle.loads(data)[1]
            if not data:
                print('no data from', client_address)
                break
            elif not isinstance(text, str):
                answer = 'data for encryption is not string'
            elif not key.isnumeric():
                answer = 'key for encription needs to be int'
            else:
                answer = ''.join(map(lambda x: chr(ord(x) + int(key)), list(text)))
            print('sending data back to the client')
            connection.sendall(pickle.dumps(answer))

    finally:
        connection.close()

