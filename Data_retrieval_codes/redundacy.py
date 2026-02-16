import pandas as pd

# Load dataset
df = pd.read_csv("training_dataset.csv")

# Remove duplicate peptide sequences
df_clean = df.drop_duplicates(subset="Peptide")

# Save cleaned dataset
df_clean.to_csv("training_dataset_clean.csv", index=False)

print("Redundancy removed.")
print("Original size:", len(df))
print("Cleaned size:", len(df_clean))
