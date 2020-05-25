import re
#from string import maketrans

STANDARD_GENETIC_CODE = {
'UUU':'Phe', 'UUC':'Phe',
'UAU':'Tyr', 'UAC':'Tyr',
'UUA':'Leu', 'UCA':'Ser',
'UUG':'Leu', 'UCG':'Ser',
'CUU':'Leu', 'CUC':'Leu',
'CAU':'His', 'CAC':'His',
'CUA':'Leu', 'CUG':'Leu',
'CAA':'Gln', 'CAG':'Gln',
'AUU':'Ile', 'AUC':'Ile',
'AAU':'Asn', 'AAC':'Asn',
'AUA':'Ile', 'ACA':'Thr',
'AUG':'Met', 'ACG':'Thr',
'GUU':'Val', 'GUC':'Val',
'GAU':'Asp', 'GAC':'Asp',
'GUA':'Val', 'GUG':'Val',
'GAA':'Glu', 'GAG':'Glu',
'UCU':'Ser',
'UGU':'Cys',
'UAA':None,
'UAG':None,
'CCU':'Pro',
'CGU':'Arg',
'CCA':'Pro',
'CGA':'Arg',
'ACU':'Thr',
'AGU':'Ser',
'AAA':'Lys',
'AAG':'Lys',
'GCU':'Ala',
'GGU':'Gly',
'GCA':'Ala',
'GGA':'Gly',
'UCC':'Ser',
'UGC':'Cys',
'UGA':None,
'UGG':'Trp',
'CCC':'Pro',
'CGC':'Arg',
'CCG':'Pro',
'CGG':'Arg',
'ACC':'Thr',
'AGC':'Ser',
'AGA':'Arg',
'AGG':'Arg',
'GCC':'Ala',
'GGC':'Gly',
'GCG':'Ala',
'GGG':'Gly'}

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

    #Yields the transcription assuming this is a DNA sequence
    def do_transcription(self):
        return re.sub("T","U",self.s)
        #return self.s.replace("T","U")

    #Yields the reverse complement assuming this is a DNA sequence
    def do_revcomp(self):
        intab = "ACGT"
        outtab = "TGCA"
        transtab = "".maketrans(intab, outtab)
        return self.s.translate(transtab)

    def protein_translation(self, geneticCode=STANDARD_GENETIC_CODE):
        """ This function translates a nucleic acid sequence into a protein sequence, until the end or until it comes across a stop codon """
        s = self.do_transcription()
        l = len(s)

        if (l % 3 != 0):
            raise Exception("Nucleotic acid sequence is not a multiple of 3")

        protein_sequence = []

        i=0
        while i+2 < l:
            codon = s[i:i+3]
            aminoacid = geneticCode[codon]
            if aminoacid is None:
                break
            protein_sequence.append(aminoacid)
            i += 3
        return protein_sequence
