import socket
import datetime
import sys


def get_time_since_1900_bin ():
    try:
        # Create a datetime object for January 1st, 1900 at midnight
        start_date = datetime.datetime(1900, 1, 1, 0, 0, 0)

        # Get the current datetime object
        current_date = datetime.datetime.now()

        # Calculate the time difference between the two datetime objects
        time_difference = current_date - start_date

        # Convert the time difference to seconds
        time_in_seconds = int(time_difference.total_seconds())
        
        # Convert to bytes
        time_in_bytes = time_in_seconds.to_bytes(4, 'big')

        # Return
        return time_in_bytes
    
    except:
        return 'error'

def server_program():
    host = socket.gethostname() # Replace with server IP!
    port = int(sys.argv[1])

    # Instantiate UDP socket
    server_socket = socket.socket(type=socket.SOCK_DGRAM)  # instantiate UDP socket
    
      # ---- User feedback -----
    print('Created socket')
    # ------------------------

    # Bind host address and port together
    server_socket.bind((host, port))  
    
    # ---- User feedback -----
    print(f'Host {host} bound to port {port} ')
    # ------------------------

    # S2, S3: Receieve empty datagram and send datagram containing time
    while True:
        # ---- User feedback ----
        print('Waiting to recieve datagram from client')
        # -----------------------
        
        [message, address] = server_socket.recvfrom(1024)
        
        # ---- User feedback ----
        print('Datagram received from client')
        # -----------------------

        # Check if datagram is empty
        if message == b'':
            # Get time & do error check
            data_as_bytes = get_time_since_1900_bin()
            if data_as_bytes != 'error':
                # Encode & send time to client
                server_socket.sendto(data_as_bytes, address)
                
                # ---- User feedback ----
                print('Time literal was send to the client')
                # -----------------------
            else:
                # ---- User feedback ----
                print('Time literal was not send to client, because there was an error in determining the time')
                # -----------------------
        else:
            # ---- User feedback ----
            print('Time literal was not send to client, because datagram was not empty')
            # -----------------------
        
        # Give the user the opertunity to terminate the server
        x = input('Do you want to terminate the server? Y: Yes, N: No \n').lower()
        if x == 'y' or x == 'yes':
            break


if __name__ == '__main__':
    server_program()
    