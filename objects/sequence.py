import re
class Sequence():
    def __init__(self, s):
            self.s = s.strip()

    def __repr__(self):
        return str("{} l={}".format(self.s, self.get_len()))
    #Concatenates the argument sequence, a Sequence object at the end of this sequence

    def get_len(self):
        return len(self.s)

    def get_sequence(self):
        return self.s

    def do_concatenation(self, sequence):
        self.s = self.s + sequence.get_sequence()

    def do_transcription(self):
        return re.sub("T","U",self.s)
        #return self.s.replace("T","U")
