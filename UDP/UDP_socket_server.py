import socket
import datetime


def get_time_since_1900_sec ():
    # Create a datetime object for January 1st, 1900 at midnight
    start_date = datetime.datetime(1900, 1, 1, 0, 0, 0)

    # Get the current datetime object
    current_date = datetime.datetime.now()

    # Calculate the time difference between the two datetime objects
    time_difference = current_date - start_date

    # Convert the time difference to seconds
    time_in_seconds = time_difference.total_seconds()

    return int(time_in_seconds)

def convert_sec_to_bin (time_in_sec):
    return bin(time_in_sec).removeprefix("0b")

def server_program():
    # get the hostname
    print('Created host + port')
    host = socket.gethostname()
    port = 37  # initiate port no above 1024

    print('Created socket')
    server_socket = socket.socket(type=socket.SOCK_DGRAM)  # instantiate UDP socket
    
    print('Bind socket to port')
    server_socket.bind((host, port))  # bind host address and port together

    # S2, S3: Receieve empty datagram and send datagram containing time
    print('Waiting to recieve response')
    bytesAddressPair = server_socket.recvfrom(1024)
    message = bytesAddressPair[0]
    address = bytesAddressPair[1]

    print('Recieved response, should be an empty datagram')
    print(message)
    if message == b'':
        print('Message is empty datagram')
        data = convert_sec_to_bin(get_time_since_1900_sec())
        data_as_bytes = str.encode(data)
        server_socket.sendto(data_as_bytes, address)
    else:
        print('Message is not empty!')
    
    print('End program')


if __name__ == '__main__':
    server_program()
    