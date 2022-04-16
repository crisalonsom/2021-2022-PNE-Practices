import socket
import termcolor

IP = "127.0.0.1"
PORT = 8080


def process_client(client_socket):
    req_bytes = client_socket.recv(2000)
    req = req_bytes.decode()

    print("Message FROM CLIENT: ")
    termcolor.cprint(req, "green")

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((IP, PORT))
server_socket.listen()
print("SEQ Server configured!")

try:
    while True:
        print("Waiting for clients....")
        (client_socket, client_ip_port) = server_socket.accept()
        process_client(client_socket)
        client_socket.close()

except KeyboardInterrupt:
    print("Server Stopped!")
    server_socket.close()

