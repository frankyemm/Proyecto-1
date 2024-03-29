import pandas as pd
import os
from matplotlib import pyplot as plt
from integrarpd import combinar_csv_en_dataframe

def plot_pie(resultado_final):
    resultado_final['first_air_date']=pd.to_datetime(resultado_final['first_air_date'])
    resultado_final['last_air_date']=pd.to_datetime(resultado_final['last_air_date'])
# Añadir la variable air_days al DataFrame
    resultado_final['air_days']=(resultado_final['last_air_date']-resultado_final['first_air_date']).dt.days
# Copia explícita para evitar SettingWithCopyWarning
    series_con_genero = resultado_final[resultado_final['genres'].notnull()].copy()

# Dividir los géneros en una lista para cada serie
    series_con_genero['genres'] = series_con_genero['genres'].apply(lambda x: x.split(','))

# Crear una lista plana con todos los géneros
    todos_generos = [genero.strip() for sublist in series_con_genero['genres'] for genero in sublist]

# Obtener la cuenta de cada género
    conteo_generos = pd.Series(todos_generos).value_counts()

# Calcular el porcentaje
    porcentaje_generos = conteo_generos / len(series_con_genero) * 100

# Agrupar los géneros que representan menos del 1% en la categoría 'Other'
    umbral = 1
    generos_filtrados = porcentaje_generos[porcentaje_generos >= umbral]
    generos_filtrados['Other'] = porcentaje_generos[porcentaje_generos < umbral].sum()

# Crear un gráfico circular
    plt.figure(figsize=(10, 10))
    plt.pie(generos_filtrados, labels=generos_filtrados.index, autopct='%1.1f%%', startangle=140)
    plt.title('Porcentaje de series por género')
#Ruta del directorio donde se guardará la imagen
    carpeta_destino = os.path.abspath("PEC_4_sol/PEC_4_sol/plots")
    # Asegurar que la carpeta de destino exista
    os.makedirs(carpeta_destino, exist_ok=True)
    # Guardar el gráfico en la ruta completa
    ruta_completa = os.path.join(carpeta_destino, "plot_pie.png")
    plt.savefig(ruta_completa)
    #Muestra el gráfico
    plt.show()
if __name__ == "__main__":
#mostramos el gráfico
    rutas_csv = [r"PEC_4_sol\PEC_4_sol\data\TMDB_info.csv", 
         r"PEC_4_sol\PEC_4_sol\data\TMDB_overview.csv", 
         r"PEC_4_sol\PEC_4_sol\data\TMDB_distribution.csv"
         ]
    resultado_final = combinar_csv_en_dataframe(rutas_csv)
    plot_pie(resultado_final)