from Seq_Client import Client

SERVER_IP = "127.0.0.1"
SERVER_PORT = 8080
BASES = "ACGTACGT"
GENES = ["ADA", "FRAT1", "FXN", "RNU6_269P", "U5"]

c = Client(SERVER_IP, SERVER_PORT)
print(c)

c.debug_talk("PING")

print()

for n in range(5):
    c.debug_talk(f"GET {n}")
    print()

c.debug_talk(f"INFO {BASES}")
print()

c.debug_talk((f"COMP {BASES}"))
print()

c.debug_talk((f"REV {BASES}"))
print()


for gene in GENES:
    c.debug_talk(f"GENE {gene}")
    print()

c.debug_talk(f"ADD {BASES}")
print()
