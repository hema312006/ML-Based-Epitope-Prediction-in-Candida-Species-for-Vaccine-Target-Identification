import pandas as pd
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

# Load dataset
df = pd.read_csv("training_dataset_final.csv")

# List of standard amino acids
amino_acids = list("ACDEFGHIKLMNPQRSTVWY")

# Function to convert peptide to amino acid composition vector
def aa_composition(seq):
    seq = str(seq).upper()
    length = len(seq)
    if length == 0:
        return [0]*20
    return [seq.count(aa)/length for aa in amino_acids]

# Convert all peptides to vectors
X = df['Peptide'].apply(aa_composition).tolist()

# Perform K-Means clustering
kmeans = KMeans(n_clusters=2, random_state=42)
cluster_labels = kmeans.fit_predict(X)

# Calculate silhouette score
score = silhouette_score(X, cluster_labels)

print("K-Means clustering completed.")
print("Silhouette Score:", score)
