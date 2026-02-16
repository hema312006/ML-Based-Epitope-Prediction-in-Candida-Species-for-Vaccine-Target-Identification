import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# Load dataset
df = pd.read_csv("training_dataset_final.csv")

# Amino acids
amino_acids = list("ACDEFGHIKLMNPQRSTVWY")

# Function to convert peptide to vector
def aa_composition(seq):
    seq = seq.upper()
    return [seq.count(aa)/len(seq) for aa in amino_acids]

# Convert first 10 peptides to vectors (for demo)
vectors = df['Peptide'].head(10).apply(aa_composition).tolist()

# Compute cosine similarity matrix
similarity_matrix = cosine_similarity(vectors)

print("Cosine Similarity Matrix:")
print(similarity_matrix)


# Remove diagonal (self-similarity)
mask = ~np.eye(similarity_matrix.shape[0], dtype=bool)
avg_similarity = similarity_matrix[mask].mean()

print("Average cosine similarity:", avg_similarity)
