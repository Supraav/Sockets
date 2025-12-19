import socket

def create_server_socket():
    socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #ip4 and TCP socket
    server_ip = '127.0.0.1'
    port= 8080
    socket_server.bind((server_ip,port))
    socket_server.listen(1) #one connection at a time

    print("server waiting for connection...")
    conn,addr = socket_server.accept()
    print(f"Connected from {addr[0]}:{addr[1]}")

    while True:
        data = conn.recv(1024)
        request = data.decode()
        if request.lower() == "close":
            print("Closing connection...")
            break 
        print("Received data",request)
    
    conn.close()
    socket_server.close()

create_server_socket()


