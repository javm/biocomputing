import re
from objects.sequence import Sequence
from objects.rna_sequence import RNASequence

class DNASequence(Sequence):
    ValidChars = 'TCAGtcag'
    # construct a string translation table for use with str.translate
    TranslationTable = "".maketrans('TCAGtcag', 'AGUCaguc')
    def __init__(self, s):
        super().__init__(s)
    def revcomp(self):
        super().do_revcomp()
    def includes(self, r):
        re.search(r, self.s)
    def translate(self):
        return RNASequence(
        self.get_sequence().translate(self.TranslationTable))
