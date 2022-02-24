from Seq0 import *
FOLDER = "../Session4/"
GENES = ["U5", "ADA", "FRAT1", "FXN", "RNU6_269P"]
BASES = ["A", "C", "G", "T"]
for gene in GENES :
    filename = gene + ".txt"
    sequence = seq_read_fasta( FOLDER + filename)
    print(f" Gene {gene} : ")
    for base in BASES :
        print(f"  {base} : {seq_count_base(sequence,base)}")
    print()