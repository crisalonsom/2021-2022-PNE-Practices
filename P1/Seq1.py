class Seq:
    ALLOWED_BASES = ["A", "C", "G", "T"]
    COMPLEMENTS = {"A": "T", "T": "A", "C": "G", "G": "C"}

    @staticmethod
    def bases_valid(bases):
        valid = len(bases) != 0
        i = 0
        while valid and i < len(bases):
            if bases[i]  in Seq.ALLOWED_BASES:
                i += 1
            else:
                valid = False
        return valid


    def __init__(self, bases="NULL"):
        if bases == "NULL":
            self.bases = bases
            print("NULL sequence created!")
        elif Seq.bases_valid(bases):
            self.bases = bases
            print("New sequence created!")
        else:
            self.bases = "ERROR"
            print("INCORRECT Sequence detected")

    def __str__(self):
        return self.bases

    def len(self):
        if self.bases == "NULL" or self.bases == "ERROR":
            return 0
        return len(self.bases)

    def count_base(self, base):
        if self.bases == "NULL" or self.bases == "ERROR":
            return 0
        return self.bases.count(base)

    def count(self):
        result = {}
        for base in Seq.ALLOWED_BASES :
            result[base] = self.count_base(base)
        return result

    def reverse(self):
        if self.bases == "NULL" or self.bases == "ERROR":
            return self.bases

        return self.bases[::-1]

    def complement(self):
        if self.bases == "NULL" or self.bases == "ERROR":
            return self.bases
        result = ""
        for base in self.bases:
            result += Seq.COMPLEMENTS[base]
        return result

    def read_fasta(self,filename):
        from pathlib import Path
        file_contents = Path(filename).read_text()
        lines = file_contents.splitlines()
        body = lines[1:]
        self.bases = ""
        for line in body:
            self.bases += line
        return self.bases

    def most_frequent(self):
        max_base = None
        max_count = 0
        for base, count in self.count().items():
            if count >= max_count:
                max_base = base
                max_count = count
        return max_base

class Gene(Seq):

    def __init__(self, bases, name=""):
        super().__init__(bases)
        self.name = name
        print("New gene created")

    def __str__(self):
        return self.name + "-" + self.bases
