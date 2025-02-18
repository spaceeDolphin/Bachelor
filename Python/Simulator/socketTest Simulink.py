import socket
import struct 
import time

# Set up a TCP/IP server
tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 
# Bind the socket to server address and port 81
server_address = ('localhost', 8080)
tcp_socket.bind(server_address)
 
# Listen on port 81
tcp_socket.listen(1)
 
while True:
    print("Waiting for connection")
    connection, client = tcp_socket.accept()
 
    try:
        print("Connected to client IP: {}".format(client))
         
        # Receive and print data 32 bytes at a time, as long as the client is sending something
        while True:
            # FLUSH
            connection.setblocking(0)  # Set socket to non-blocking mode
            try:
                while True:
                # Try to read any outstanding bytes
                    connection.recv(1024)
            except BlockingIOError:
                pass
            connection.setblocking(1)  # Set socket back to blocking mode

            # READ
            data = connection.recv(32)
            float_value1 = struct.unpack('<d', data[:8])[0]
            float_value2 = struct.unpack('<d', data[8:16])[0]
            float_value3 = struct.unpack('<d', data[16:24])[0]
            print(float_value1,float_value2,float_value3)
            print("###################################################")
            
            time.sleep(3)
            
            if not data:
                break
 
    finally:
        connection.close()