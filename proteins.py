import sys
import pathlib
import os

from dotenv import load_dotenv

import objects

seq1 = objects.Sequence('ATGGTGUGACATCTGACTCCTGAGGAGAAGTCTGCCGTTACTGCCCTGTGGGGCAAGGTGTGT')
protein = seq1.protein_translation()

print(protein)
