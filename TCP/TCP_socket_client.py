import socket
import datetime
import sys

def convert_sec_from_1900_to_date (time_in_sec):
    # Create a datetime object for January 1st, 1900 at midnight
    SECONDS_FROM_1900_TO_1970 = 2208988800
    data = time_in_sec - SECONDS_FROM_1900_TO_1970

    # Add the time in seconds to the start date
    time_in_date = datetime.datetime.fromtimestamp(data).strftime('%c')

    return time_in_date

def client_program():
    [serverhost, port] = sys.argv[1:3]
    port = int(port)

    client_socket = socket.socket(type=socket.SOCK_STREAM)  # instantiate TCP socket
    
    # ---- User feedback ----
    print("Created socket")
    # -----------------------

    # U1: Connect to port 37
    client_socket.connect((serverhost, port))  # connect to the server
    
    # ---- User feedback ----
    print(f"Connected to server at host: {serverhost}, port: {port}")
    # -----------------------

    # ---- User feedback ----
    print("Waiting to receive time from server")
    # -----------------------

    # U2: Receive the time
    data_bytes = client_socket.recv(4)  # receive response
    data_int =  int.from_bytes(data_bytes, 'big')
    
    # ---- User feedback ----
    print('Received message from server')
    print('Time received from server: ' + str(data_int))  # show in terminal
    print('Time received from server: ' + str(data_bytes))  # show in terminal
    print('Time received from server: ' + str(convert_sec_from_1900_to_date(data_int)))  # show in terminal
    # -----------------------
    
    # U3: Close the connection
    client_socket.close()  # close the connection

    # ---- User feedback ----
    print('Connection closed')
    # -----------------------

if __name__ == '__main__':
    client_program()