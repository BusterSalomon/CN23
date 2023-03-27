import socket
import datetime


def get_time_since_1970_sec ():
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
    host = socket.gethostname()
    port = 37  # initiate port no above 1024

    server_socket = socket.socket(type=socket.SOCK_DGRAM)  # instantiate UDP socket
    # look closely. The bind() function takes tuple as argument
    server_socket.bind((host, port))  # bind host address and port together

    # S1: Listen on port 37
    
    # S2, S3: Receieve empty datagram and send datagram containing time
    bytesAddressPair = server_socket.recvfrom(1024)
    message = bytesAddressPair[0]
    address = bytesAddressPair[1]

    if format(message) == b'':
        data = convert_sec_to_bin(get_time_since_1970_sec())
        server_socket.sendto(data, address)


if __name__ == '__main__':
    server_program()
    