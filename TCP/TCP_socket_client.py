import socket
import datetime
import sys

def convert_sec_from_1900_to_date(sec):
    return (datetime.datetime(1900, 1, 1) + datetime.timedelta(seconds=sec)).strftime("%Y-%m-%d %H:%M:%S")

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
    data = client_socket.recv(1024).decode()  # receive response
    
    # ---- User feedback ----
    print('Received message from server')
    print('Time received from server: ' + data)  # show in terminal
    print('Time received from server: ' + convert_sec_from_1900_to_date(int(data, 2)))  # show in terminal
    # -----------------------
    
    # U3: Close the connection
    client_socket.close()  # close the connection

    # ---- User feedback ----
    print('Connection closed')
    # -----------------------

if __name__ == '__main__':
    client_program()