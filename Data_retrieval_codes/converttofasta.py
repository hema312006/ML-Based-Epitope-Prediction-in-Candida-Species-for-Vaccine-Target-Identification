import pandas as pd

df = pd.read_csv("training_dataset_clean.csv")

with open("peptides.fasta", "w") as f:
    for i, seq in enumerate(df['Peptide']):
        f.write(f">pep{i}\n{seq}\n")

print("FASTA file created.")
