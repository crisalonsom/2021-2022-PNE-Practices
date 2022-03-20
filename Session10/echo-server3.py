import socket
import termcolor

IP = "localhost"
PORT = 8080
n = 0
clients = []
CONNECTIONS = 5


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
try:
    server_socket.bind((IP, PORT))
    server_socket.listen()

    while n != CONNECTIONS:
        print(f"Waiting for connections at {IP}: {PORT} ")
        (client_socket, client_address) = server_socket.accept()

        n += 1
        clients.append(client_address)


        print(f"CONNECTION {n}: From the IP:({client_address})")
        msg_bytes = client_socket.recv(2048)
        msg = msg_bytes.decode("utf-8")
        print(f"Message from client: ", end="")
        termcolor.cprint(msg, 'green')


        msg = f"ECHO : {msg}"
        send_bytes = str.encode(msg)

        client_socket.send(send_bytes)
        client_socket.close()

    server_socket.close()
    print("The following clients have connect to the server:")
    for client, index in enumerate(clients):
        print(f"Client {index} : {client} ")

except socket.error:
    print(f"Problems using port {PORT}. Do you have permission?")

except KeyboardInterrupt:
    print("Server stopped by the user")
    server_socket.close()
