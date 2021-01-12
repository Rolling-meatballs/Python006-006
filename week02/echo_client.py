import socket

HOST = 'localhost'
PORT = 10000

def echo_client():
    ''' Echo server 的 Client 端 '''

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))

    while True:

        data = input('input > ')

        if data == 'exit':
            break

        s.sendall(data.encode())

        data = s.recv(1024)
        if not data:
            break
        else:
            print(data.decode('utf-8'))

    s.close()

if __name__ == "__main__":
    echo_client()
