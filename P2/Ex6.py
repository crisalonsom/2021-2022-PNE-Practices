from Client0 import Client
from Seq1 import Seq

PRACTICE = 2
EXERCISE = 6
GENE = "FRAT1"
FRAGMENTS = 5
BASES = 10

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")
SERVER_IP = "localhost"
SERVER_PORT = 8081
c = Client(SERVER_IP, SERVER_PORT)

s = Seq()
s.read_fasta(f"{GENE}.txt")
print(f"Gene {GENE} : {s}")

c.debug_talk(f"Sending {GENE}  Gene to the server , in fragments of {BASES} bases ")

start_index = 0
final_index = BASES
for f in range(1, FRAGMENTS +1):
    fragment = s.bases[start_index:final_index]
    print(f"Fragment{f}: {fragment} ")
    c.debug_talk(fragment)
    start_index += BASES
    final_index += BASES



