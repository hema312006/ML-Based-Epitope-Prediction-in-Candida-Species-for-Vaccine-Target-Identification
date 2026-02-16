import pandas as pd
import numpy as np

# Load dataset
df = pd.read_csv("training_dataset_final.csv")

# List of standard amino acids
amino_acids = list("ACDEFGHIKLMNPQRSTVWY")

# Convert peptide to amino acid composition vector
def aa_composition(seq):
    seq = str(seq).upper()
    length = len(seq)
    if length == 0:
        return [0]*20
    return [seq.count(aa)/length for aa in amino_acids]

# Convert peptides into vectors
vectors = df['Peptide'].apply(aa_composition).tolist()
vectors = np.array(vectors)

# Function to compute Tanimoto similarity
def tanimoto(a, b):
    dot = np.dot(a, b)
    denom = np.dot(a, a) + np.dot(b, b) - dot
    if denom == 0:
        return 0
    return dot / denom

# Compute Tanimoto similarity matrix
n = len(vectors)
similarities = []

for i in range(n):
    for j in range(i+1, n):
        sim = tanimoto(vectors[i], vectors[j])
        similarities.append(sim)

# Calculate average similarity
avg_similarity = np.mean(similarities)

print("Average Tanimoto similarity:", avg_similarity)
