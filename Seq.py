from Bio.Seq import Seq


if __name__ == '__main__':
    my_seq = Seq("AGTACACTGGT")
    print(my_seq)
    print(my_seq.complement())
    print(my_seq.reverse_complement())
