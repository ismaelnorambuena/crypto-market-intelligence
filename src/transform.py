import pandas as pd

df = pd.read_csv("data/raw/users_raw.csv")

print("Columnas originales:")
print(df.columns)

df = df[["id", "name", "email", "website"]]

print("\nDatos transformados:")
print(df.head())

df.to_csv("data/processed/users_clean.csv", index=False)

print("\nArchivo limpio guardado")