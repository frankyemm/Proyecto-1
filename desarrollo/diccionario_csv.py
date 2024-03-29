#Listo el pollo
# desompresion y lectura/
# Ejer integracion_datos.py
# Ejercicico 1.2

import csv
import time
import os

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

