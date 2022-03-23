from pathlib import Path
filename = "ADA.txt"
file_contents = Path(filename).read_text()

end_of_line = file_contents.find("\n")
seq_dna = file_contents[end_of_line:].replace("\n","")
num_bases = len(seq_dna)
print(num_bases)
