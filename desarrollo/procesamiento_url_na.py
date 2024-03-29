# Problema 2.2
from integrarpd import combinar_csv_en_dataframe
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
    rutas_csv = [
    r"PEC_4_sol\PEC_4_sol\data\TMDB_distribution.csv",
    r"PEC_4_sol\PEC_4_sol\data\TMDB_info.csv", 
    r"PEC_4_sol\PEC_4_sol\data\TMDB_overview.csv"  
]
# Mostrar los primeros 5 registros del diccionario, para hacerlo borra el # que está a la izquierda del print
    print("Primeros 5 registros del diccionario:")
    resultado_final=combinar_csv_en_dataframe(rutas_csv)
    diccionario=pro_url_na(resultado_final)
    primeros_5_registros = dict(list(diccionario.items())[:5])
#Para imprimir hay que eliminar el # a la izquierda del print
    print(primeros_5_registros)
    

