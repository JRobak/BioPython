import sys

from Bio import Entrez
from Bio import SeqIO

Entrez.email = 'example@example.com'
handle = Entrez.efetch(db="nucleotide", id="NM_000546", rettype="gb", retmode="text")
record = SeqIO.read(handle, "genbank")
print(record)
