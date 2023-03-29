import socket
import datetime
import sys
import time


def get_time_since_1900_bin ():
    try:
        # Convert the time difference to seconds
        time_in_seconds = int(time.time()) + 2208988800

        # Convert to bytes
        time_in_bytes = time_in_seconds.to_bytes(4, 'big')

        # Return
        return time_in_bytes
    
    except:
        return 'error'

def server_program():
    host = socket.gethostname() # Replace with server IP!
    port = int(sys.argv[1])

    # Instantiate TCP socket & bind host to port
    server_socket = socket.socket(type=socket.SOCK_STREAM)  
    server_socket.bind((host, port))  # bind host address and port together
    
    # ---- User feedback ----
    print(f"Bound socket to host: {host}, port: {port}")
    # -----------------------

    # Start listening
    server_socket.listen(1) # arg: configure how many client the server can listen simultaneously

    # ---- User feedback ----
    print(f"Started listening at port {port}")
    # -----------------------

    while True:
        # ----- User feedback -----
        print("Awaiting new connection")
        # -------------------------
        
        # Wait for new connection to accept - blocking call
        conn, address = server_socket.accept()  
        
        # ----- User feedback -----
        print("Accepted connection from: " + str(address)) 
        # -------------------------

        # S2: Get the time as a 32 bit binary
        data = get_time_since_1900_bin()
        
        # Close connection if unable to get time on site
        # else send time
        if data != 'error':
            conn.send(data)  # send data to the client
            
            # ---- User feedback ----
            print("Time was send to client")
            # -----------------------

            # ---- User feedback ---- 
            print("Waiting for client to disconnect")
            # -----------------------

            # S3: Close the connection
            # Wait for client to close connection first
            while True:
                # Check if client have disconnected
                data = conn.recv(1024).decode()
                if not data:
                    # ----- User feedback -----
                    print("Client disconnected")
                    # -------------------------

                    break

        # Close the connection
        conn.close()  

        # ---- User feedback ----
        print("Closed connection")
        # -----------------------

        # Give user opertunity to terminate
        x = input('Do you want to terminate the server? Y: Yes, N: No \n').lower()
        if x == 'y' or x == 'yes':
            break


if __name__ == '__main__':
    server_program()
    