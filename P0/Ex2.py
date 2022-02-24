import Seq0
FOLDER = "../Session4/"
filename = input("File´s name : ")
print(f"DNA file : {filename}")
sequence = Seq0.seq_read_fasta( FOLDER + filename)
print("The first 20 bases are :")
print(sequence[:20])