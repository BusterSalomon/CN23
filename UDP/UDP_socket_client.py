import socket
import datetime

def convert_sec_from_1900_to_date (time_in_sec):
    # Create a datetime object for January 1st, 1900 at midnight
    start_date = datetime.datetime(1900, 1, 1, 0, 0, 0)

    # Add the time in seconds to the start date
    time_in_date = start_date + datetime.timedelta(seconds=time_in_sec)

    return time_in_date

def client_program():
    print('Created host + port')
    host = socket.gethostname() # Replace with server IP!
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

    time_as_date = convert_sec_from_1900_to_date(time_secs)
    
    print('Time received from server in bits: ' + time_bits)  # show in terminal
    print('Time received from server in secs : ' + str(time_secs))  # show in terminal
    print('Time received from server in date : ' + str(time_as_date))  # show in terminal



if __name__ == '__main__':
    client_program()