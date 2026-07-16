import pandas as pd

df = pd.read_csv("data/raw/crypto_raw.csv")

columnas_utiles = [
    "name",
    "symbol",
    "current_price",
    "market_cap",
    "market_cap_rank",
    "total_volume",
    "price_change_percentage_24h",
    "last_updated"
]

df = df[columnas_utiles]

print("Dataset limpio:")

print(df.head())

df.to_csv(
    "data/processed/crypto_clean.csv",
    index=False
)

print("\nArchivo guardado en data/processed/crypto_clean.csv")