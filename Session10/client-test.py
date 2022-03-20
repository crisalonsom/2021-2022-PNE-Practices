from Client0 import Client

server_ip = "localhost"
server_port = 8080
MESSAGES = 5

c = Client(server_ip, server_port)
for i in range(MESSAGES):
    c.debug_talk(f"Message {i}")