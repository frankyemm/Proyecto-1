import pandas as pd
import os
from matplotlib import pyplot as plt
from integrarpd import combinar_csv_en_dataframe


def plot_bar(resultado_integra):
    resultado_integra['first_air_date']=pd.to_datetime(resultado_integra['first_air_date'])
    resultado_integra['last_air_date']=pd.to_datetime(resultado_integra['last_air_date'])
# Añadir la variable air_days al DataFrame
    resultado_integra['air_days']=(resultado_integra['last_air_date']-resultado_integra['first_air_date']).dt.days
# Filtrar las series que han empezado en 2023 y han sido canceladas
    condiciones_filtro = (
    (  resultado_integra['first_air_date'].dt.year == 2023) & 
    (resultado_integra['status'].str.lower() == 'canceled'))
    resultado_integra['first_air_date'] = pd.to_datetime(resultado_integra['first_air_date'])

# Obtener el año de inicio de cada serie
    resultado_integra['start_year'] = resultado_integra['first_air_date'].dt.year
# Contar el número de series por año de inicio
    series_por_año = resultado_integra['start_year'].value_counts().sort_index()
# Crear el gráfico de barras
    plt.figure(figsize=(20, 6))
    bars = plt.bar(series_por_año.index, series_por_año, color='skyblue')
    for bar in bars:
        yval=bar.get_height()
        plt.text(bar.get_x()+bar.get_width()/2, yval, round(yval, 1), ha='center', va='bottom')
    plt.title('Número de series por año de inicio')
    plt.xlabel('Año de inicio')
    plt.ylabel('Número de series')
    plt.yticks(range(0,12000,1000))
    #Ruta del directorio donde se guardará la imagen
    carpeta_destino = os.path.abspath("PEC_4_sol/PEC_4_sol/plots")
    # Asegurar que la carpeta de destino exista
    os.makedirs(carpeta_destino, exist_ok=True)
    # Guardar el gráfico en la ruta completa
    ruta_completa = os.path.join(carpeta_destino, "plot_bar.png")
    plt.savefig(ruta_completa)
    #Muestra el gráfico
    plt.show()
    return resultado_integra.loc[condiciones_filtro, 'name']
#Muestra el gráfico
if __name__ =="__main__":
    rutas_csv = [r"PEC_4_sol\PEC_4_sol\data\TMDB_info.csv", 
         r"PEC_4_sol\PEC_4_sol\data\TMDB_overview.csv", r"PEC_4_sol\PEC_4_sol\data\TMDB_distribution.csv"
         ]
    resultado_integra = combinar_csv_en_dataframe(rutas_csv)
    plot_bar(resultado_integra)