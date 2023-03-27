import socket
import datetime

def convert_sec_to_date_from_1900(sec):
    return (datetime.datetime(1900, 1, 1) + datetime.timedelta(seconds=sec)).strftime("%Y-%m-%d %H:%M:%S")

def client_program():
    host = socket.gethostname() # Replace with server IP!
    port = 37  # socket server port number

    client_socket = socket.socket(type=socket.SOCK_STREAM)  # instantiate TCP socket
    print("Created socket")

    # U1: Connect to port 37
    client_socket.connect((host, port))  # connect to the server
    print(f"Connected to server at host: {host}, port: {port}")

    # U2: Recieve the time
    print("Waiting to reieve time from server")
    data = client_socket.recv(1024).decode()  # receive response
    print('Time received from server: ' + data)  # show in terminal
    print('Time received from server: ' + convert_sec_to_date_from_1900(int(data,2)))  # show in terminal

    # U3: Close the connection
    client_socket.close()  # close the connection


if __name__ == '__main__':
    client_program()