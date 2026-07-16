# 🚀 Crypto Market Intelligence

## Descripción

Proyecto de Data Science enfocado en la extracción, transformación y análisis de datos del mercado de criptomonedas utilizando la API pública de CoinGecko.

El proyecto implementa un pipeline ETL completo para obtener datos en tiempo real, procesarlos y generar análisis orientados al mercado financiero y blockchain.

---

## Objetivos

- Obtener datos de criptomonedas en tiempo real.
- Construir un pipeline ETL profesional.
- Analizar capitalización de mercado.
- Analizar volumen transado.
- Analizar variaciones porcentuales diarias.
- Generar visualizaciones para apoyar la toma de decisiones.

---

## Tecnologías Utilizadas

- Python
- Pandas
- Requests
- Matplotlib
- Git
- GitHub
- CoinGecko API

---

## Arquitectura ETL

```text
CoinGecko API
      ↓
extract_crypto.py
      ↓
crypto_raw.csv
      ↓
transform_crypto.py
      ↓
crypto_clean.csv
      ↓
analisis_crypto.py
      ↓
Visualizaciones
```

---

## Estructura del Proyecto

```text
crypto-market-intelligence/

├── data/
│   ├── raw/
│   │   └── crypto_raw.csv
│   │
│   └── processed/
│       └── crypto_clean.csv
│
├── reports/
│   ├── top_crypto_marketcap.png
│   ├── top_crypto_volume.png
│   └── top_crypto_gainers_24h.png
│
├── src/
│   ├── extract_crypto.py
│   ├── transform_crypto.py
│   ├── analisis_crypto.py
│   ├── grafico_crypto.py
│   ├── grafico_volumen.py
│   └── grafico_ganadoras.py
│
└── README.md
```

---

## Análisis Realizados

### Top Criptomonedas por Capitalización de Mercado

Identificación de los activos digitales más relevantes según su valor total de mercado.

### Top Criptomonedas por Volumen Transado

Análisis de los activos con mayor actividad y liquidez dentro del mercado.

### Top Ganadoras de las Últimas 24 Horas

Identificación de las criptomonedas con mejor rendimiento porcentual diario.

---

## Resultados

El proyecto permite:

- Extraer datos del mercado crypto en tiempo real.
- Procesar y limpiar información financiera.
- Analizar métricas clave del mercado.
- Generar visualizaciones para facilitar la interpretación de datos.

---

## Insights

- Bitcoin lidera la capitalización de mercado del ecosistema crypto.
- Ethereum se mantiene como el segundo activo más relevante.
- Las criptomonedas con mayor capitalización concentran gran parte del volumen transado.
- Algunas altcoins presentan variaciones diarias superiores a las criptomonedas de mayor tamaño.

---

## Próximas Mejoras

- Dashboard interactivo con Power BI.
- Integración con PostgreSQL.
- Automatización diaria del pipeline ETL.
- Análisis histórico de precios.
- Monitoreo automático de tendencias del mercado.
- Alertas para movimientos significativos de criptomonedas.

---

## Autor

**Ismael Norambuena**

Data Science | Python | ETL | Blockchain Analytics