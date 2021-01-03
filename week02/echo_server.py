import socket

HOST = 'localhost'
POST = 10000


def echo_server():

    ''' Echo server Server '''
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    s.bind((HOST, POST))

    s.listen()
    while True:

        connection, address = s.accept()

        print(f'Connected by {address}')

        request = b''
        buffer_size = 1024

        while True:
            r = connection.recv(buffer_size)
            request += r
            if len(r) < buffer_size:
                break
        with open('index.html', 'r') as f:
                    text = f.read()
                    print(f'text : {text}')
                    response = text.encode()
                    print(f'text : {type(response)}')
                    connection.sendall(response)
        conn.close()
    s.close()

if __name__ == "__main__":
    echo_server()
