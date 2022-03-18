import termcolor
from Seq1 import Seq

def generate_seqs(pattern, number):
    seq_list = []
    bases = pattern
    for i in range(number):
        seq_list.append(Seq(bases))
        bases += pattern
    return seq_list

def print_seqs(seq_list,color):
    for index,seq in enumerate(seq_list):
        termcolor.cprint (f" Sequence {index} : (Lenght : {seq.len()})  {seq}", color)



seq_list1 = generate_seqs("A", 3)
seq_list2 = generate_seqs("AC", 5)

termcolor.cprint("List 1:", 'blue')
print_seqs(seq_list1, 'blue')

print()
termcolor.cprint("List 2:", 'green')
print_seqs(seq_list2, 'green')