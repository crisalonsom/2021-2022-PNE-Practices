from pathlib import Path
filename = "U5.txt"
file_contents = Path(filename).read_text()

end_of_line = file_contents.find("\n")
seq_dna = file_contents[end_of_line:]
print(seq_dna)