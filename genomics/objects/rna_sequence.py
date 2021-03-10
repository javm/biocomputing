from objects.sequence import Sequence
class RNASequence(Sequence):
    def __init__(self, s):
        super().__init__(s)
    def translate_codon(self, codon):
        return self.CodonTable[codon]
    def translate(self, frame=1):
        """Produce a protein sequence by translating this RNA sequence starting at frame 1, 2, or 3"""
        #codons = []
        #for n in range(frame -1, len(self.get_sequence()) - (len(self.get_sequence()) - (frame-1)) % 3, 3):
        #    codons.append(self.translate_codon(self.get_sequence()[n:n+3]))
        #return ''.join(codons)
        return ''.join([self.translate_codon(self.get_sequence()[n:n+3])
        for n in
        range(frame-1,
        # ignore 1 or 2 bases after last triple
        len(self.get_sequence()) -
        (len(self.get_sequence()) - (frame-1)) % 3,
        3)])
