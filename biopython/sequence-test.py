from Bio import SeqIO
from Bio.Seq import Seq
from Bio.Alphabet import generic_dna

#for seq_record in SeqIO.parse("sra_data.fasta", "fasta"):
#    print(seq_record.id)
#    print(repr(seq_record.seq))
#    print(len(seq_record))

sequences = list(SeqIO.parse("sra_data.fasta", "fasta"))

seq0 = sequences[0].seq
seq1 = sequences[1].seq

seq2 = seq0 + seq1

seq3 = Seq("GATCTAAAGTCATTTGACTTAGGCGACGAGCTTGGCACT", generic_dna)
seq4 = seq3.transcribe()
seq5 = seq3.translate()
print(repr(seq2))
print(repr(seq3))
print(repr(seq4))
print(repr(seq5))
