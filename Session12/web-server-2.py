import socket
import termcolor

IP = "127.0.0.1"
PORT = 8080


def process_client(client_socket):
    req_bytes = client_socket.recv(2000)
    req = req_bytes.decode()

    print("Message FROM CLIENT: ")
    lines = req.split('\n')
    req_line = lines[0]

    print("Request line: ", end="")
    termcolor.cprint(req_line, "green")

    body = """
        <!DOCTYPE html>
        <html lang="en" dir="ltr">
          <head>
            <meta charset="utf-8">
            <title>Green server</title>
          </head>
          <body style="background-color: lightgreen;">
            <h1>GREEN SERVER</h1>
            <p>I am the Green Server! :-)</p>
          </body>
        </html>
        """
    status_line = "HTTP/1.1 200 OK\n"
    header = "Content-Type: text/html\n"
    header += f"Content-Length: {len(body)}\n"
    response_msg = status_line + header + "\n" + body
    client_socket.send(response_msg.encode())


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

