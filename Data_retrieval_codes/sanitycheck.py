import pandas as pd

df = pd.read_csv("training_dataset_final.csv")

print("Total samples:", len(df))
print("\nClass distribution:")
print(df['Label'].value_counts())

print("\nEmpty peptides:", df['Peptide'].isnull().sum())
