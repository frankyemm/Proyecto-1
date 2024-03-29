import pandas as pd
import os
from matplotlib import pyplot as plt
from integrarpd import combinar_csv_en_dataframe

def plot_lin(resultado_final):
    resultado_final['first_air_date']=pd.to_datetime(resultado_final['first_air_date'])
    resultado_final['last_air_date']=pd.to_datetime(resultado_final['last_air_date'])
    # Añadir la variable air_days al DataFrame
    resultado_final['air_days']=(resultado_final['last_air_date']-resultado_final['first_air_date']).dt.days
    # Obtener el año de inicio de cada serie
    resultado_final['start_year'] = resultado_final['first_air_date'].dt.year
    # Crear una columna para la década
    resultado_final['decade'] = (resultado_final['start_year'] // 10) * 10

    # Contar el número de series por década y categoría de "type"
    series_por_decada_tipo = resultado_final.groupby(['decade', 'type']).size().unstack().fillna(0)

    # Crear el gráfico de líneas
    plt.figure(figsize=(12, 8))
    for tipo in series_por_decada_tipo.columns:
        plt.plot(series_por_decada_tipo.index, series_por_decada_tipo[tipo], label=tipo)

    plt.title('Número de series por década y tipo')
    plt.xlabel('Década')
    plt.ylabel('Número de series')
    plt.legend()
    #Ruta del directorio donde se guardará la imagen
    carpeta_destino = os.path.abspath("PEC_4_sol/PEC_4_sol/plots")
    # Asegurar que la carpeta de destino exista
    os.makedirs(carpeta_destino, exist_ok=True)
    # Guardar el gráfico en la ruta completa
    ruta_completa = os.path.join(carpeta_destino, "plot_lin.png")
    plt.savefig(ruta_completa)
    #Mostrar el gráfico
    plt.show()

if __name__ == "__main__":
#Mostrar el gráfico
    rutas_csv = [r"PEC_4_sol\PEC_4_sol\data\TMDB_info.csv", 
         r"PEC_4_sol\PEC_4_sol\data\TMDB_overview.csv", 
         r"PEC_4_sol\PEC_4_sol\data\TMDB_distribution.csv"
         ]
    resultado_final = combinar_csv_en_dataframe(rutas_csv)
    plot_lin(resultado_final)