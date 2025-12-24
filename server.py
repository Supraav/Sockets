import socket
import threading

def recieve_message(conn):
    while True:
        try:
            data=conn.recv(1024)
            if not data:
                print("client disconnected")
                break
            request = data.decode()
            if request.lower() == "close":
                print("Closing connection...")
                break 
            print("Received data:",request)
        except:
            break

    pass

def send_message(conn):
    while True:
        msg= input("Enter message from server: ")
        conn.sendall(msg.encode())
        if msg.lower() =="close":
            break

def create_server_socket():
    socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #ip4 and TCP socket
    server_ip = '127.0.0.1'
    port= 8080
    socket_server.bind((server_ip,port))
    socket_server.listen(1) #one connection at a time

    print("server waiting for connection...")
    conn,addr = socket_server.accept()
    print(f"Connected from {addr[0]}:{addr[1]}")
    print(f"connection is {conn}")

    recieve_thread = threading.Thread(target=recieve_message,args=(conn,))
    send_thread = threading.Thread(target=send_message,args=(conn,))

    recieve_thread.start()
    send_thread.start()

    recieve_thread.join()
    send_thread.join()

    conn.close()
    socket_server.close()

create_server_socket()