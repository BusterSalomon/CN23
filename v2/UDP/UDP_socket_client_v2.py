import socket
import datetime
import sys

def convert_sec_from_1900_to_date (time_in_sec):
    # Calculate 
    SECONDS_FROM_1900_TO_1970 = 2208988800
    seconds_since_1970 = time_in_sec - SECONDS_FROM_1900_TO_1970

    # Calculate timestamp
    time_in_date = datetime.datetime.fromtimestamp(seconds_since_1970).strftime('%c')

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
    time_secs = int.from_bytes(time_as_bytes, 'big')
    time_as_date = convert_sec_from_1900_to_date(time_secs)
    
    # ---- User feedback -----
    print('Seconds since 01/01/1900 received: ' + str(time_secs))  # show in terminal
    print('Seconds since 01/01/1900 converted to date: ' + str(time_as_date))  # show in terminal
    # ------------------------



if __name__ == '__main__':
    client_program()