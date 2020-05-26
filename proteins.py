import sys
import pathlib
import os

from dotenv import load_dotenv

import objects

seq1 = objects.Sequence('ATGGTGUGACATCTGACTCCTGAGGAGAAGTCTGCCGTTACTGCCCTGTGGGGCAAGGTGTGT')
protein = seq1.protein_translation()
print(protein)

rna_seq = objects.RNASequence('UUACCUGGCAUUGCAA')
for n in range(1,4):
    print('Frame', n, rna_seq.translate(n), sep = ' ')
