import sys
import pathlib
import os

from dotenv import load_dotenv

import objects

load_dotenv()
input_dir = os.environ.get("INPUT_DIR")
output_dir = os.environ.get("OUTPUT_DIR")

if( len(sys.argv) > 1):
    file1 = open(pathlib.PurePosixPath(input_dir).joinpath(sys.argv[1]))
    file2 = open(pathlib.PurePosixPath(input_dir).joinpath(sys.argv[2]))
    input1 = file1.read().strip()
    input2 = file2.read().strip()

    seqarg1 = objects.Sequence(input1)
    seqarg2 = objects.Sequence(input2)
    seqarg1.do_concatenation(seqarg2)
    file_out = open(pathlib.PurePosixPath(output_dir).joinpath('outconcat.txt'), 'w')
    file_out.write(seqarg1.__repr__())
    file_out.close()
    file1.close()
    file2.close()
else:
    seq1 = objects.Sequence('GTTAAAGGTTTATACCTTCCCAGGTAACAAACCAACCAAC')
    seq2 = objects.Sequence('TACCGTAAAGGTTTATACCTTCCCAGGTAACAAACCAACC')

    seq1.do_concatenation(seq2)
    print(seq1)

    seq3 = objects.Sequence(seq1.do_transcription())
    print(seq3)

    seq4 = objects.Sequence(seq1.do_revcomp())
    print(seq1)
    print(seq4)
