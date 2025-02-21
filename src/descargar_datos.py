import yfinance as yf
import pandas as pd

def descargar_datos(ticker, start, end, archivo_destino):
    # Descarga datos del ticker especificado entre las fechas dadas
    data = yf.download(ticker, start=start, end=end)
    # Guardar datos en CSV
    data.to_csv(archivo_destino)
    print(f'Datos de {ticker} guardados en {archivo_destino}')

if __name__ == '__main__':
    # Ejemplo: descarga datos de Apple (AAPL) para el año 2022
    descargar_datos('AAPL', '2022-01-01', '2022-12-31', '../data/precios_AAPL.csv')
