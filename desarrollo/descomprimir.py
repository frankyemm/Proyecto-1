#Listo el pollo
#Ejercicio 1.1: Descompresion de archivos
# desompresion y lectura/ejer1.1_descompresion.py
import os
import zipfile
import tarfile

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
