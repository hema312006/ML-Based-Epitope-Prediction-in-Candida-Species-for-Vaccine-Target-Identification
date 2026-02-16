import pandas as pd
import random

# Load positive epitopes
df = pd.read_csv("training_dataset_clean.csv")
peptides = df['Peptide'].tolist()

amino_acids = "ACDEFGHIKLMNPQRSTVWY"

# Generate highly random peptides
def random_peptide():
    length = random.randint(8, 20)  # variable length
    return ''.join(random.choice(amino_acids) for _ in range(length))

negatives = [random_peptide() for _ in peptides]

df_pos = pd.DataFrame({"Peptide": peptides, "Label": 1})
df_neg = pd.DataFrame({"Peptide": negatives, "Label": 0})

df_final = pd.concat([df_pos, df_neg], ignore_index=True)
df_final.to_csv("training_dataset_final.csv", index=False)

print("Dataset with more diverse negatives created.")
