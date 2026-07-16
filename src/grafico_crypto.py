import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/processed/crypto_clean.csv")

df = df.sort_values(
    by="market_cap",
    ascending=False
)

plt.figure(figsize=(10, 6))

plt.bar(
    df["name"],
    df["market_cap"]
)

plt.title("Top Criptomonedas por Market Cap")

plt.xlabel("Criptomoneda")

plt.ylabel("Market Cap")

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig("reports/top_crypto_marketcap.png")

plt.show()

print("Grafico guardado correctamente")
