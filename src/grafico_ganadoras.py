import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/processed/crypto_clean.csv")

df = df.sort_values(
    by="price_change_percentage_24h",
    ascending=False
)

plt.figure(figsize=(10, 6))

plt.bar(
    df["name"],
    df["price_change_percentage_24h"]
)

plt.title("Top Ganadoras Ultimas 24 Horas")

plt.xlabel("Criptomoneda")
plt.ylabel("% Cambio 24h")

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig("reports/top_crypto_gainers_24h.png")

plt.show()

print("Grafico de ganadoras creado")