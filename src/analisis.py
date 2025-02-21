import pandas as pd
import matplotlib.pyplot as plt

def main():
    # Leer datos
    df = pd.read_csv('../data/precios.csv', parse_dates=['Fecha'])
    df.set_index('Fecha', inplace=True)

    # Calcular volatilidad: desviación estándar
    volatilidad = df['Precio'].std()
    print(f'Volatilidad: {volatilidad}')

    # Graficar precios
    df['Precio'].plot(title='Precios de Acciones')
    plt.xlabel('Fecha')
    plt.ylabel('Precio')
    plt.show()

if __name__ == '__main__':
    main()
