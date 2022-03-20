import socket
import termcolor

IP = "localhost"
PORT = 8080


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
try:
    server_socket.bind((IP, PORT))
    server_socket.listen()

    while True:
        print(f"Waiting for connections at {IP}: {PORT} ")
        (client_socket, client_address) = server_socket.accept()


        print(f"CONNECTION: From the IP:({client_address})")
        msg_bytes = client_socket.recv(2048)
        msg = msg_bytes.decode("utf-8")
        print(f"Message from client: ", end="")
        termcolor.cprint(msg, 'green')


        msg = f"ECHO : {msg}"
        send_bytes = str.encode(msg)

        client_socket.send(send_bytes)
        client_socket.close()

except socket.error:
    print(f"Problems using port {PORT}. Do you have permission?")

except KeyboardInterrupt:
    print("Server stopped by the user")
    server_socket.close()
