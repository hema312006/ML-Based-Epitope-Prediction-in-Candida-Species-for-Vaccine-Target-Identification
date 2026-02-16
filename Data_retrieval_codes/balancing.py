import pandas as pd
import random

# Load cleaned unique peptides
df = pd.read_csv("training_dataset_clean.csv")

peptides = df['Peptide'].tolist()

# Shuffle peptides
random.shuffle(peptides)

# Split into two halves
half = len(peptides) // 2

pos = peptides[:half]
neg = peptides[half:half*2]

# Create dataframes
df_pos = pd.DataFrame({
    "Peptide": pos,
    "Label": 1
})

df_neg = pd.DataFrame({
    "Peptide": neg,
    "Label": 0
})

# Combine
df_final = pd.concat([df_pos, df_neg], ignore_index=True)

# Save final dataset
df_final.to_csv("training_dataset_final.csv", index=False)

print("Final dataset created.")
print(df_final['Label'].value_counts())
