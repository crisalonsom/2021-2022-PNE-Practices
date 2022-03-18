class Seq:
    ALLOWED_BASES = ["A", "C", "G", "T"]

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


    def __init__(self, bases):
        if Seq.bases_valid(bases):
            self.bases = bases
            print("New sequence created!")
        else:
            self.bases = "ERROR"
            print("INCORRECT Sequence detected")

    def __str__(self):
        return self.bases

    def len(self):
        return len(self.bases)

class Gene(Seq):

    def __init__(self, bases, name=""):
        super().__init__(bases)
        self.name = name
        print("New gene created")

    def __str__(self):
        return self.name + "-" + self.bases
