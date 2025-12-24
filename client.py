import socket
import threading

def recieve_message(conn):
    while True:
        try:
            data = conn.recv(1024)
            if not data:
                print("server disconnected")
                break
            request = data.decode()
            if request.lower()=="close":
                print("closing connection...")
                break
        except:
            break 

def send_message(conn):
    while True:
        msg=input("Enter message from client: ")
        conn.sendall(msg.encode())
        if msg.lower()=="close":
            break

def client_socket():
    socket_client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    socket_client.connect(("127.0.0.1",8080))
    
    recieve_thread = threading.Thread(target=recieve_message,args=(socket_client,))
    send_thread = threading.Thread(target=send_message,args=(socket_client,))

    recieve_thread.start()
    send_thread.start()

    recieve_thread.join()
    send_thread.join()

    socket_client.close()
client_socket()