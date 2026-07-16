import requests
import pandas as pd

url = "https://api.coingecko.com/api/v3/coins/markets"

parametros = {
    "vs_currency": "usd",
    "order": "market_cap_desc",
    "per_page": 10,
    "page": 1,
    "sparkline": False
}

respuesta = requests.get(url, params=parametros)

datos = respuesta.json()

df = pd.DataFrame(datos)

print("Columnas disponibles:\n")
print(df.columns)

print("\nDimensiones:")
print(df.shape)

df.to_csv("data/raw/crypto_raw.csv", index=False)

print("\nArchivo guardado en data/raw/crypto_raw.csv")