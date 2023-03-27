import socket

def client_program():
    print('Created host + port')
    host = socket.gethostname()  # IP of server
    port = 37  # socket server port number

    print('Created socket')
    client_socket = socket.socket(type=socket.SOCK_DGRAM)  # instantiate TCP socket

    print('send empty datagram')
    # U1: Send empty datargam
    client_socket.sendto(b'', (host, port))

    print('Empty datagram was send, waiting to recieve response')
    # U2: Receive the time datagram
    # - Note that it is a blocking call, it waits for a response
    bytesAddressPair = client_socket.recvfrom(1024)
    time_as_bytes = bytesAddressPair[0]
    print('Response recieved')
    time_bits = time_as_bytes.decode()
    time_secs = int(time_bits, 2)
    
    print('Time received from server in bits: ' + time_bits)  # show in terminal
    print('Time received from server in secs : ' + str(time_secs))  # show in terminal



if __name__ == '__main__':
    client_program()