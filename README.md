# 🚀 Crypto Market Intelligence

## Descripción

Proyecto de Data Science enfocado en la extracción, transformación y análisis de datos del mercado de criptomonedas utilizando la API pública de CoinGecko.

El proyecto implementa un pipeline ETL completo para obtener datos en tiempo real, procesarlos y generar análisis visuales orientados al mercado financiero y blockchain.

---

## Objetivos

- Obtener datos de criptomonedas en tiempo real
- Construir un pipeline ETL profesional
- Analizar capitalización de mercado
- Analizar volumen transado
- Analizar variaciones porcentuales diarias
- Generar visualizaciones para apoyar la toma de decisiones

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

## Visualizaciones

### Top Criptomonedas por Market Cap

reports/top_crypto_marketcap.png

### Top Criptomonedas por Volumen

reports/top_crypto_volume.png

### Top Ganadoras 24 Horas

reports/top_crypto_gainers_24h.png


---

## Insights

- Bitcoin lidera la capitalización de mercado del ecosistema crypto.
- Ethereum se mantiene como el segundo activo más relevante.
- Las criptomonedas con mayor capitalización concentran gran parte del volumen transado.
- Algunas altcoins presentan variaciones diarias significativamente superiores a Bitcoin y Ethereum.

---

## Próximas Mejoras

- Dashboard interactivo con Power BI
- Integración con PostgreSQL
- Automatización diaria del pipeline ETL
- Análisis histórico de precios
- Alertas automáticas para movimientos importantes del mercado

---

## Autor

**Ismael Norambuena**

Data Science | Python | ETL | Blockchain Analytics