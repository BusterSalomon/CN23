import socket
import datetime
import sys

def convert_sec_from_1900_to_date (time_in_sec):
    # Create a datetime object for January 1st, 1900 at midnight
    start_date = datetime.datetime(1900, 1, 1, 0, 0, 0)

    # Add the time in seconds to the start date
    time_in_date = start_date + datetime.timedelta(seconds=time_in_sec)

    return time_in_date

def client_program():
    [serverhost, port] = sys.argv[1:3]
    port = int(port)
    
    # Instantiate UDP socket
    client_socket = socket.socket(type=socket.SOCK_DGRAM)  
    
    # ---- User feedback -----
    print('Created socket')
    # ------------------------

    # U1: Send empty datagram
    client_socket.sendto(b'', (serverhost, port))
    
    # ---- User feedback -----
    print('Empty datagram was send')
    # ------------------------

    # ---- User feedback -----
    print('Waiting to receive response')
    # ------------------------

    # U2: Receive the time datagram
    time_as_bytes = client_socket.recvfrom(1024)[0]
    
    # ---- User feedback -----
    print('Received reponse')
    # ------------------------

    # Decode & convert
    time_bits = time_as_bytes.decode()
    time_secs = int(time_bits, 2)
    time_as_date = convert_sec_from_1900_to_date(time_secs)
    
    # ---- User feedback -----
    print('Seconds since 01/01/1900 received from server in bits: ' + time_bits)  # show in terminal
    print('Seconds since 01/01/1900 received: ' + str(time_secs))  # show in terminal
    print('Seconds since 01/01/1900 converted to date: ' + str(time_as_date))  # show in terminal
    # ------------------------



if __name__ == '__main__':
    client_program()