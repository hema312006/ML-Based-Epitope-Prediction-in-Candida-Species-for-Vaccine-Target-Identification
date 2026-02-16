import pandas as pd

# Load original dataset
df = pd.read_csv("training_dataset_clean.csv")

# Load BLAST results
blast = pd.read_csv("blast_results.txt", sep="\t", header=None)

# Keep only needed columns
blast = blast[[0, 1, 2]]
blast.columns = ["query", "subject", "identity"]

# Remove self-matches
blast = blast[blast["query"] != blast["subject"]]

# Find redundant sequences
redundant = set()

for _, row in blast.iterrows():
    if row["identity"] >= 70:
        redundant.add(row["subject"])

# Convert FASTA IDs to indices
indices = [int(x.replace("pep", "")) for x in redundant]

# Remove redundant peptides
df_clean = df.drop(indices, errors="ignore")

# Save new dataset
df_clean.to_csv("non_redundant_dataset.csv", index=False)

print("Original size:", len(df))
print("Non-redundant size:", len(df_clean))
