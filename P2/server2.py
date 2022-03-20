import socket
import termcolor

IP = "localhost"
PORT = 8081
MAX_OPEN_REQUEST = 5

n = 0

server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
try:
    server_socket.bind((IP,PORT))
    server_socket.listen(MAX_OPEN_REQUEST)

    while True:
        print(f"Waiting for connections at {IP}: {PORT} ")
        (client_socket, client_address) = server_socket.accept()


        n += 1

        print(f"CONNECTION: {n}. From the IP: ({client_address})")
        msg_bytes = client_socket.recv(2048)
        msg = msg_bytes.decode("utf-8")
        print(f"Message from client: ", end="")
        termcolor.cprint(msg, 'green')


        msg = "Hello from the teacher's server"
        send_bytes = str.encode(msg)

        client_socket.send(send_bytes)
        client_socket.close()

except socket.error:
    print(f"Problems using port {PORT}. Do you have permission?")

except KeyboardInterrupt:
    print("Server stopped by the user")
    server_socket.close()