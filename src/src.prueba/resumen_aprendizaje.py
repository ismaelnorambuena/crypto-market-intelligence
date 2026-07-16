import pandas as pd

datos = {
    "Paso": [
        "Requests",
        "BeautifulSoup",
        "Pandas",
        "CSV"
    ],
    "Funcion": [
        "Descargar paginas web",
        "Leer HTML",
        "Trabajar con tablas",
        "Guardar datos"
    ]
}

df = pd.DataFrame(datos)

print(df)