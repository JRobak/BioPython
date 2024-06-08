from Bio import SeqIO


for seq_record in SeqIO.parse("assets/arsa.fasta", "fasta"):
    print(seq_record.id)
    print(seq_record.seq)
    print(len(seq_record))