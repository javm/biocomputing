class Sequence():
    def __init__(self, s, length=None):
            self.s = s.strip()
            self.l = length or len(s)
    def __repr__(self):
        return str("{} l={}".format(self.s, self.l))

#my_seq = Sequence('GTTAAAGGTTTATACCTTCCCAGGTAACAAACCAACCAAC', 40)
