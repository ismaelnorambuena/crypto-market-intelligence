import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/processed/crypto_clean.csv")

df = df.sort_values(
    by="total_volume",
    ascending=False
)

plt.figure(figsize=(10, 6))

plt.bar(
    df["name"],
    df["total_volume"]
)

plt.title("Top Criptomonedas por Volumen Transado")

plt.xlabel("Criptomoneda")
plt.ylabel("Volumen")

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig("reports/top_crypto_volume.png")

plt.show()

print("Grafico de volumen creado")