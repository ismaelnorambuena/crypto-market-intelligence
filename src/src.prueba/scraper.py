import requests
import pandas as pd
from bs4 import BeautifulSoup

url = "https://quotes.toscrape.com"

respuesta = requests.get(url)

soup = BeautifulSoup(respuesta.text, "html.parser")

citas = soup.find_all("span", class_="text")

lista_citas = []

for cita in citas:
    lista_citas.append(cita.text)

df = pd.DataFrame({
    "Cita": lista_citas
})

print(df)

df.to_csv("data/citas.csv", index=False)

print("CSV guardado correctamente")