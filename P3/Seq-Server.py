import socket
import termcolor
import os
from Sequence import Seq

IP = "localhost"
PORT = 8080
GENES = ["U5", "ADA", "FRAT1", "FXN", "RNU6_269P"]

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
try:
    server_socket.bind((IP, PORT))
    server_socket.listen()

    print("Seq Server configured")

    while True:
        print(f"Waiting for client ...")
        (client_socket, client_address) = server_socket.accept()

        msg_bytes = client_socket.recv(2048)
        msg = msg_bytes.decode("utf-8")

        slices = msg.split(" ")
        command = slices[0]
        termcolor.cprint(f"{command} command", 'green')
        response = ""
        if command == "PING":
            response = f"OK! \n"
        elif command == "GET":
            gene_num = int(slices[1])
            gene = GENES[gene_num]
            seq = Seq()
            filename = os.path.join("..", "Genes", f"{gene}.txt")
            seq.read_fasta(filename)
            response = f"{seq} \n"

        elif command == "INFO":
            bases = slices[1]
            sequence = Seq(bases)
            response = f"{sequence.info()}\n"

        elif command == "COMP":
            bases = slices[1]
            sequence = Seq(bases)
            response = f"{sequence.complement()}\n"

        elif command == "REV":
            bases = slices[1]
            sequence = Seq(bases)
            response = f"{sequence.reverse()}\n"

        elif command == "GENE":
            gene = slices[1]
            sequence = Seq()
            filename = os.path.join("..", "Genes", f"{gene}.txt")
            sequence.read_fasta(filename)

            response = f"{sequence}\n"

        print(response)
        response_bytes = str.encode(response)
        client_socket.send(response_bytes)


        client_socket.close()

except socket.error:
    print(f"Problems using port {PORT}. Do you have permission?")

except KeyboardInterrupt:
    print("Server stopped by the user")
    server_socket.close()
