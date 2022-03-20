from Client0 import Client
PRACTICE = 2
EXERCISE = 1
print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")
SERVER_IP = "localhost"
SERVER_PORT = 8081
c = Client(SERVER_IP, SERVER_PORT)
c.ping()
print(f"IP: {c.server_ip}, PORT: {c.server_port}")