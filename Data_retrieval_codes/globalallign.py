from Bio import pairwise2
from Bio.pairwise2 import format_alignment

# Two peptide sequences (example from your dataset)
seq1 = "ASSHRALARLRTACERAKRT"
seq2 = "AVKLQNNELSPVALR"

# Perform global alignment
alignments = pairwise2.align.globalxx(seq1, seq2)

# Print the best alignment
for alignment in alignments[:1]:
    print(format_alignment(*alignment))
