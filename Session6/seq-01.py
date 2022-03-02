class Seq:
    ALLOWED_BASES = ["A", "C", "G", "T"]

    @staticmethod
    def  bases_valid(bases):
        valid = len(bases) != 0
        i = 0
        while  valid and i < len(bases):
            if bases[i] not in Seq.ALLOWED_BASES :
                valid = False
        return valid


    def __init__(self, strbases):
        if Seq.bases_valid(bases)
            self.strbases = strbases
            print("New sequence created!")
        else:
            self.bases = "ERROR"
            print("INCORRECT Sequence detected" )

    def __str__(self):
        return self.strbases

    def len(self):
        return len(self.strbases)

class Gene(Seq):
    def __init__(self, strbases, name=""):
        super().__init__(strbases)
        self.name = name
        print("New gene created")

    def __str__(self):
        return self.name + "-" + self.strbases


s1 = Seq("ACCTGC")
s2 = Seq("Hello? Am I a valid sequence?")
print(f"Sequence 1: {s1}")
print(f"Sequence 2: {s2}")