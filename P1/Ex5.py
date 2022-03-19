from Seq1 import Seq

print("-----| Exercise 5 |-----")
seqs_list = [Seq(), Seq("ACTGA"), Seq("Invalid sequence")]
for index, seq in enumerate(seqs_list):
    print(f"Sequence {index}: (Length: {seq.len()}) {seq}")
    for base in Seq.ALLOWED_BASES:
        print(f"{base}: {seq.count_base(base)}",end=" ")
    print()
