import socket

udpsock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

host = '127.0.0.1'
port = 65432
print('starting up on {} port {}'.format(host, port))
udpsock.bind((host, port))

while True:
    # Wait for a connection
    print('waiting for a connection')
    try:
        while True:
            data, client_address = udpsock.recvfrom(1024)
            print('connection from', client_address)
            print('received {!r}'.format(data))
            if data:
                print('sending data back to the client')
                udpsock.sendto(data.upper(), client_address)
            else:
                print('no data from', client_address)
                break

    finally:
        udpsock.close()