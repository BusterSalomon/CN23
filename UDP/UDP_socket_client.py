import socket


def client_program():
    host = socket.gethostname()  # IP of server
    port = 37  # socket server port number

    client_socket = socket.socket(type=socket.SOCK_DGRAM)  # instantiate TCP socket

    # U1: Send empty datargam
    client_socket.sendto(b'', (host, port))

    # U2: Receive the time datagram
    # - Note that it is a blocking call, it waits for a response
    bytesAddressPair = client_socket.recvfrom(1024)
    time = bytesAddressPair[0]

    print('Time received from server: ' + time)  # show in terminal
   


if __name__ == '__main__':
    client_program()