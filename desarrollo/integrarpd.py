#Listo el pollo
# desompresion y lectura/
# Ejer integracion_datos.py
# Ejercicico 1.2
import pandas as pd
import time

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

