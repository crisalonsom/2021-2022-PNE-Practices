from Seq0 import *
FOLDER = "../Session4/"
GENES = ["U5", "ADA", "FRAT1", "FXN", "RNU6_269P"]
for gene in GENES :
    filename = gene + ".txt"
    sequence = seq_read_fasta( FOLDER + filename)
    print(f" Gene {gene} ---> Length : {seq_len(sequence)} ")
