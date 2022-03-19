from Seq1 import Seq

GENES = ["U5", "ADA", "FRAT1", "FXN", "RNU6_269P"]
for gene in GENES :
    filename = gene + ".txt"
    try:
        seq = Seq()
        seq.read_fasta(filename)
        max_base = seq.most_frequent()
        print(f"Gene {gene}: {max_base[1]}")
    except FileNotFoundError:
        print(f"[ERROR]: file '{filename}' not found ")

