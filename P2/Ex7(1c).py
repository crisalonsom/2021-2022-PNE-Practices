from Client0 import Client
from Seq1 import Seq

PRACTICE = 2
EXERCISE = 7
GENE = "FRAT1"
FRAGMENTS = 10
BASES = 10

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

SERVER_IP = "localhost"
SERVER1_PORT = 8080
SERVER2_PORT = 8081


s = Seq()
s.read_fasta(f"{GENE}.txt")
print(f"Gene {GENE} : {s}")

c = Client(SERVER_IP, SERVER1_PORT)
c.debug_talk(f"Sending {GENE}  Gene to the server , in fragments of {BASES} bases ")
c = Client(SERVER_IP, SERVER2_PORT)
c.debug_talk(f"Sending {GENE}  Gene to the server , in fragments of {BASES} bases ")

start_index = 0
final_index = BASES
for f in range(1, FRAGMENTS +1):
    fragment = s.bases[start_index:final_index]
    print(f"Fragment{f}: {fragment} ")
    if f % 2 == 0 :
        c = Client(SERVER_IP, SERVER2_PORT)
        c.debug_talk(f"Fragment{f}: {fragment}")
    else:
        c = Client(SERVER_IP, SERVER1_PORT)
        c.debug_talk(f"Fragment{f}: {fragment} ")
    start_index += BASES
    final_index += BASES