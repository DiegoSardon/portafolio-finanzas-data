import pandas as pd
import matplotlib.pyplot as plt

def analizar_volatilidad(archivo_datos):
    # Leer datos reales de un archivo CSV
    df = pd.read_csv(archivo_datos, parse_dates=['Date'])
    df.set_index('Date', inplace=True)
    # Calcular volatilidad: desviación estándar del precio de cierre
    volatilidad = df['Close'].std()
    print(f'Volatilidad: {volatilidad}')
    # Graficar precios
    df['Close'].plot(title='Precios de Acciones')
    plt.xlabel('Fecha')
    plt.ylabel('Precio de Cierre')
    plt.show()

if __name__ == '__main__':
    analizar_volatilidad('../data/precios_AAPL.csv')
