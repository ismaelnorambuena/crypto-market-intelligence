import pandas as pd

datos = {
    "Empresa": ["Binance", "Coinbase", "Kraken"],
    "Cargo": ["Data Scientist", "Data Analyst", "ML Engineer"],
    "Pais": ["USA", "Canada", "Remote"]
}

df = pd.DataFrame(datos)

print(df)

df.to_csv("data/vacantes.csv", index=False)

print("Archivo guardado correctamente")
