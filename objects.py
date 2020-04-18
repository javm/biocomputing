import objects
seq1 = objects.Sequence('GTTAAAGGTTTATACCTTCCCAGGTAACAAACCAACCAAC')
seq2 = objects.Sequence('TACCGTAAAGGTTTATACCTTCCCAGGTAACAAACCAACC')

seq1.do_concatenation(seq2)
print(seq1)
seq3 = objects.Sequence(seq1.do_transcription())
print(seq3)
