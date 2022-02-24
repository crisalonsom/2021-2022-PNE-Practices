from pathlib import Path
filename = "RNU6_269P.txt"
file_contents = Path(filename).read_text()

end_of_line = file_contents.find("\n")
seq_dna = file_contents[:end_of_line].replace("\n","")
print(seq_dna)