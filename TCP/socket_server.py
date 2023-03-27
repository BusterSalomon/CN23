import socket
import datetime


def get_time_since_1900_bin ():
    try:
        # Create a datetime object for January 1st, 1900 at midnight
        start_date = datetime.datetime(1900, 1, 1, 0, 0, 0)

        # Get the current datetime object
        current_date = datetime.datetime.now()

        # Calculate the time difference between the two datetime objects
        time_difference = current_date - start_date

        # Convert the time difference to seconds
        time_in_seconds = time_difference.total_seconds()

        # Convert to binary
        time_in_bin = bin(int(time_in_seconds)).replace('0b', '')

        return time_in_bin
    
    except:
        return 'error'

def server_program():
    # get the hostname
    host = socket.gethostname() # Replace with server IP!
    port = 37  # initiate port no above 1024

    server_socket = socket.socket(type=socket.SOCK_STREAM)  #instantiate TCP socket
    # look closely. The bind() function takes tuple as argument
    server_socket.bind((host, port))  # bind host address and port together

    
    # S1: Listen on port 37
    server_socket.listen(1) # arg: configure how many client the server can listen simultaneously
    conn, address = server_socket.accept()  # accept new connection
    print("Connection from: " + str(address)) 
    
    # S2: Send the time as a 32 bit binary number.
    data = get_time_since_1900_bin()
    
    # Close connection if unable to get time on site
    # Else send time
    if data != -1:
        conn.send(data.encode())  # send data to the client
        
        # S3: Close the connection
        # Wait for client to close connection first
        while True:
            # Check if client have disconnected
            data = conn.recv(1024).decode()
            if not data:
                break

    conn.close()  # close the connection


if __name__ == '__main__':
    server_program()
    