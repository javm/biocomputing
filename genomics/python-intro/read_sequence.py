import re
def count_sra(sra_file):
    sra = open(sra_file)
    sra_lines = sra.readlines()
    print("Num of lines: {}".format(len(sra_lines)))
    for i in range(len(sra_lines)):
        # i = 0, 1, 2
        print("Line {}: {}".format(i, sra_lines[i]))
    #for i, l in enumerate(sra_lines, start=1):
    #    print("Line {}: {}".format(i,l))


def read_sequences(sra_file):
    sra = open(sra_file)
    sra_lines = sra.readlines()
    c = 0
    for i in range(len(sra_lines)):
        if re.match(r'^>', sra_lines[i]):
            c = c + 1
            print("Found {}: {}".format(c, sra_lines[i]))

# count_sra('sra_data.fasta')
read_sequences('sra_data.fasta')
