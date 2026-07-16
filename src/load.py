import pandas as pd

df = pd.read_csv("data/processed/users_clean.csv")

print("Dataset cargado correctamente")

print("\nCantidad de registros:")
print(len(df))

print("\nColumnas:")
print(df.columns)

print("\nPrimeras filas:")
print(df.head())