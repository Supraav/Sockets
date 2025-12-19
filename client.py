import socket

def client_socket():
    socket_client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    socket_client.connect(("127.0.0.1",8080))
    
    while True:
        msg = input("Enter the message: ")
        socket_client.sendall(msg.encode())

        if msg.lower() =="close":
            break

client_socket()