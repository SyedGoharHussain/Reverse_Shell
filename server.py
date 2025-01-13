import socket
import base64

ip_adress = '0.0.0.0' //IPv4 format
port_number = 1234 

ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ss.bind((ip_adress,port_number))   //bind port with ip 
ss.listen(5)
print("Waiting For Connection....")
connection, address = ss.accept()
CLIENTS = connection
print("Found something.... ", CLIENTS)
try:
    while True:
            data_to_send = input("Enter data to send (type 'quit' to exit): ").encode()

            if data_to_send.decode().lower() == 'quit':
                break  
            connection.send(data_to_send)
            received_data = connection.recv(8096*10000)
            print("Received:", received_data.decode())

finally:
    connection.close()
