import pandas as pd
import time
import os
import zipfile
import tarfile
import csv
from matplotlib import pyplot as plt
    
# Función descomprimir
def descomprimir_archivo(ruta):
    # Obtener la extensión del archivo
    extension = os.path.splitext(ruta)[1]

    if extension == '.zip':
        with zipfile.ZipFile(ruta, 'r') as zip_ref:
            zip_ref.extractall(os.path.dirname(ruta))
        print(f"Archivo '{ruta}' descomprimido exitosamente.")
    elif extension == '.gz':
        with tarfile.open(ruta, 'r:gz') as tar_ref:
            tar_ref.extractall(os.path.dirname(ruta))
        print(f"Archivo '{ruta}' descomprimido exitosamente.")
    else:
        print(f"Error: El archivo '{ruta}' no es un archivo ZIP o tar.gz.")

# Ejemplo de uso para descomprimir TMDB.zip
if __name__ == "__main__":
    ruta_tmdb_zip = r"PEC_4_sol\PEC_4_sol\data\TMDB.zip"
    descomprimir_archivo(ruta_tmdb_zip) 
    
# Función combinar (integrar en un dataframe)
def combinar_csv_en_dataframe(lista_rutas_csv):
    # Iniciar el contador de tiempo
    inicio_tiempo = time.time()

    # Leer cada archivo CSV en un DataFrame y almacenarlo en una lista
    dataframes = [pd.read_csv(ruta_csv, encoding='utf-8') for ruta_csv in lista_rutas_csv]

    # Combinar los DataFrames en uno único utilizando la columna "id" como clave
    resultado = pd.concat(dataframes, axis=1, ignore_index=False)
    resultado=resultado.T.drop_duplicates().T
    # Calcular el tiempo de procesamiento
    tiempo_procesamiento = time.time() - inicio_tiempo
    if __name__ == "__main__":
        print(f'Tiempo de procesamiento: {tiempo_procesamiento:.4f} segundos')
    return resultado
if __name__ == "__main__":
# Ejemplo de uso con los archivos CSV
    rutas_csv = [r"PEC_4_sol\PEC_4_sol\data\TMDB_info.csv", 
         r"PEC_4_sol\PEC_4_sol\data\TMDB_overview.csv", 
         r"PEC_4_sol\PEC_4_sol\data\TMDB_distribution.csv"
         ]
    resultado_final = combinar_csv_en_dataframe(rutas_csv)
    print(resultado_final)

# Función integrar en un diccionario

def combinar_csv_en_diccionario(lista_rutas_csv, columna_comun):
    # Iniciar el contador de tiempo
    inicio_tiempo = time.time()

    # Inicializar el diccionario que contendrá los datos combinados
    diccionario_resultado = {}

    # Leer cada archivo CSV y agregar los datos al diccionario
    for ruta_csv in lista_rutas_csv:
        # Utilizar la función os.path.join() para unir las rutas
        ruta_csv = os.path.join(os.getcwd(), ruta_csv)

        # Comprobar si la ruta existe
        if not os.path.exists(ruta_csv):
            raise FileNotFoundError(f"El archivo '{ruta_csv}' no existe.")

        # Leer el archivo CSV
        with open(ruta_csv, 'r', encoding='utf-8') as archivo_csv:
            lector_csv = csv.DictReader(archivo_csv)
            
            # Verificar que la columna común está presente
            if columna_comun not in lector_csv.fieldnames:
                raise ValueError(f"La columna común '{columna_comun}' no está presente en el archivo CSV '{ruta_csv}'.")

            # Agregar las filas al diccionario
            for fila in lector_csv:
                clave_id = fila[columna_comun]
                diccionario_resultado.setdefault(clave_id, {}).update(fila)

    # Calcular el tiempo de procesamiento
    tiempo_procesamiento = time.time() - inicio_tiempo
    print(f'Tiempo de procesamiento: {tiempo_procesamiento:.4f} segundos')

    return diccionario_resultado

if __name__ == "__main__":
    # Ejemplo de uso con los archivos CSV
    rutas_csv = [r"PEC_4_sol\PEC_4_sol\data\TMDB_info.csv",
                 r"PEC_4_sol\PEC_4_sol\data\TMDB_overview.csv",
                 r"PEC_4_sol\PEC_4_sol\data\TMDB_distribution.csv"]

    # Columna común en los archivos CSV
    columna_comun = "id"

    # Imprimir el diccionario resultante
    print(combinar_csv_en_diccionario(rutas_csv, columna_comun))

#Función procesamiento air_days

def pro_air_days(resultado_final):
# Convertir las columnas first_air_date y last_air_date en formato de fecha
    resultado_final['first_air_date']=pd.to_datetime(resultado_final['first_air_date'])
    resultado_final['last_air_date']=pd.to_datetime(resultado_final['last_air_date'])
    # Añadir la variable air_days al DataFrame
    resultado_final['air_days']=(resultado_final['last_air_date']-resultado_final['first_air_date']).dt.days
    return resultado_final
# Mostrar los 10 registros que más días han estado en emisión
if __name__ == "__main__":
    procesado_days=pro_air_days(resultado_final)
    top_10_emision=procesado_days.sort_values(by='air_days', ascending=False).head(10)

# Imprimir el DataFrame resultante, para hacerlo borra el # que está a la izquierda del print

    print(top_10_emision)

#Función procesamiento canceled 2023

def pro_cancel(resultado_final):
    resultado_final['first_air_date']=pd.to_datetime(resultado_final['first_air_date'])
    resultado_final['last_air_date']=pd.to_datetime(resultado_final['last_air_date'])
    # Añadir la variable air_days al DataFrame
    resultado_final['air_days']=(resultado_final['last_air_date']-resultado_final['first_air_date']).dt.days
    # Filtrar las series que han empezado en 2023 y han sido canceladas
    condiciones_filtro = (
        (resultado_final['first_air_date'].dt.year == 2023) & 
        (resultado_final['status'].str.lower() == 'canceled')
    )

    # Obtener las series que cumplen con las condiciones
    series_canceladas_2023 = resultado_final.loc[condiciones_filtro, 'name']
    return series_canceladas_2023
if __name__ == "__main__":
# Mostrar por pantalla los primeros 20 elementos de la lista
    series_canceladas_2023=pro_cancel(resultado_final)
    print("Series que empezaron en 2023 y han sido canceladas (primeros 20):")
    print(series_canceladas_2023.head(20).tolist())
    
#Función procesamiento en_mys_crim

def pro_en_mys_crim(resultado_final):
#Escribo las condiciones de filtro que se deben de cumplir 
    condiciones_filtro = (
    (resultado_final['original_language'].str.lower() == 'en') & 
    (resultado_final['overview'].str.lower().str.contains('mystery|crime'))
)
    return resultado_final.loc[condiciones_filtro, 'name']
# Obtener los nombres de las series que cumplen con las condiciones

if __name__ == '__main__':

# Llamar a la función y obtener el resultado procesado
    series_cumplen_condiciones = pro_en_mys_crim(resultado_final)
# Mostrar por pantalla los nombres de las series
    print("Series con idioma original inglés y palabras 'mystery' o 'crime' en el resumen:")
    print(series_cumplen_condiciones.tolist())
    
#Función procesamiento ja_lang

def filtrar_series_japonesas(resultado_final):
    resultado_final=combinar_csv_en_dataframe(rutas_csv)
    if 'first_air_date' in resultado_final.columns and 'last_air_date' in resultado_final.columns:
        resultado_final['first_air_date']=pd.to_datetime(resultado_final['first_air_date'])
        resultado_final['last_air_date']=pd.to_datetime(resultado_final['last_air_date'])
# Añadir la variable air_days al DataFrame
        resultado_final['air_days']=(resultado_final['last_air_date']-resultado_final['first_air_date']).dt.days
# Filtrar las series cuyo idioma incluye el japonés
        lista_incluyen=['name', 'original_name', 'networks', 'production_companies']
# Filtrar las series cuyo idioma incluye el japonés
        condicion_idioma_japones = resultado_final['languages'].str.lower().str.contains('ja')
        condicion_idioma_japones.fillna(False, inplace=True)  # Llenar valores nulos con False
# Seleccionar las columnas requeridas y aplicar el filtro
        series_japonesas = resultado_final.loc[condicion_idioma_japones, lista_incluyen]
    else:
        exit
    return series_japonesas
if __name__ == "__main__":
# Mostrar los primeros 20 registros por pantalla
    resultado_series=filtrar_series_japonesas(resultado_final)
    print(resultado_series.head(20))

#Función procesamiento url_na


def pro_url_na(resultado_final):
    #print(resultado_final)
    # Rellenar NaN o "" en las columnas de homepage y poster_path
    resultado_final['homepage'].fillna('NOT AVAILABLE', inplace=True)
    resultado_final['poster_path'].fillna('NOT AVAILABLE', inplace=True)
    # Crear el diccionario de posters
    diccionario_posters = {}
    for index, row in resultado_final.iterrows():
        name = row['name']
        homepage = row['homepage']
        poster_path = row['poster_path']

        # Construir la dirección web completa del poster
        if homepage != "NOT AVAILABLE":
            poster_url = str(homepage) + str(poster_path)
        else:
            poster_url = "NOT AVAILABLE"
        diccionario_posters[name] = poster_url
    return diccionario_posters

if __name__ == "__main__":
# Mostrar los primeros 5 registros del diccionario, para hacerlo borra el # que está a la izquierda del print
    print("Primeros 5 registros del diccionario:")
    diccionario=pro_url_na(resultado_final)
    primeros_5_registros = dict(list(diccionario.items())[:5])
#Para imprimir hay que eliminar el # a la izquierda del print
    print(primeros_5_registros)


#Función plotear_bar

def plot_bar(resultado_final):
    resultado_final['first_air_date']=pd.to_datetime(resultado_final['first_air_date'])
    resultado_final['last_air_date']=pd.to_datetime(resultado_final['last_air_date'])
# Añadir la variable air_days al DataFrame
    resultado_final['air_days']=(resultado_final['last_air_date']-resultado_final['first_air_date']).dt.days
# Filtrar las series que han empezado en 2023 y han sido canceladas
    condiciones_filtro = (
    (  resultado_final['first_air_date'].dt.year == 2023) & 
    (resultado_final['status'].str.lower() == 'canceled'))
    resultado_final['first_air_date'] = pd.to_datetime(resultado_final['first_air_date'])

# Obtener el año de inicio de cada serie
    resultado_final['start_year'] = resultado_final['first_air_date'].dt.year
# Contar el número de series por año de inicio
    series_por_año = resultado_final['start_year'].value_counts().sort_index()
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
    return resultado_final.loc[condiciones_filtro, 'name']
#Muestra el gráfico
if __name__ =="__main__":
    plot_bar(resultado_final)
    

#Función plotear_lin


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
    plot_lin(resultado_final)


#Función plotear_pie


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
    plot_pie(resultado_final)