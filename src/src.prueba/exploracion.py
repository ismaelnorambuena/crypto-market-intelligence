import pandas as pd

df = pd.read_csv("data/vacantes.csv")

print("Primeras filas:")
print(df.head())

print("\nColumnas:")
print(df.columns)

print("\nDimensiones:")
print(df.shape)

print("\nInformación:")
print(df.info())