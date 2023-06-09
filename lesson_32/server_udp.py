import socket

udpsock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

host = '127.0.0.1'
port = 65432
print('starting up on {} port {}'.format(host, port))
udpsock.bind((host, port))

udpsock.listen(1)

while True:
    # Wait for a connection
    print('waiting for a connection')
    connection, client_address = udpsock.accept()
    try:
        print('connection from', client_address)

        # Receive the data in small chunks and retransmit it
        while True:
            data = connection.recv(1024)
            print('received {!r}'.format(data))
            if data:
                print('sending data back to the client')
                connection.sendall(data.upper())
            else:
                print('no data from', client_address)
                break

    finally:
        # Clean up the connection
        connection.close()