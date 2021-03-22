import sequence
import re
class SequencesReader():
    def __init__(self, input_file):
        #validaciones
        #1. Que inicie con >
        #raise Error('no tiene >')
        self.f = input_file
        self.sequences = []

    def __repr__(self):
        all_seq = ''
        for s in self.sequences:
            all_seq = all_seq + '{} \n'.format(str(s))
        return all_seq

    def read_sequences(self):
        sra = open(self.f)
        sra_lines = sra.readlines()
        c = 0

        for i in range(len(sra_lines)):
            if re.match(r'^>', sra_lines[i]):
                #s = dame_sig_linea()
                s_l = int(sra_lines[i].split()[2].split('=')[1])
                s = sra_lines[i+1]
                seq = sequence.Sequence(s, s_l)
            self.sequences.append(seq)

ss = SequencesReader('sra_data.fasta')
ss.read_sequences()
print(ss)
