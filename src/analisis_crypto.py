import pandas as pd

df = pd.read_csv("data/processed/crypto_clean.csv")

print("\nTOP 10 POR MARKET CAP\n")

print(
    df[[
        "name",
        "market_cap",
        "market_cap_rank"
    ]].sort_values(
        by="market_cap",
        ascending=False
    )
)

print("\nTOP GANADORAS 24H\n")

print(
    df[[
        "name",
        "price_change_percentage_24h"
    ]].sort_values(
        by="price_change_percentage_24h",
        ascending=False
    )
)

print("\nTOP VOLUMEN\n")

print(
    df[[
        "name",
        "total_volume"
    ]].sort_values(
        by="total_volume",
        ascending=False
    )
)