import requests
import pandas as pd

url = "https://jsonplaceholder.typicode.com/users"

respuesta = requests.get(url)

datos = respuesta.json()

df = pd.DataFrame(datos)

print("\nColumnas:")
print(df.columns)

print("\nDimensiones:")
print(df.shape)

print("\nPrimeras filas:")
print(df.head())

print("\nTipos de datos:")
print(df.info())

df.to_csv("data/raw/users_raw.csv", index=False)

print("\nArchivo guardado en data/raw/users_raw.csv")

