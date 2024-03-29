from integrarpd import combinar_csv_en_dataframe

def pro_en_mys_crim(resultado_final):
#Escribo las condiciones de filtro que se deben de cumplir 
    condiciones_filtro = (
    (resultado_final['original_language'].str.lower() == 'en') & 
    (resultado_final['overview'].str.lower().str.contains('mystery|crime'))
)
    return resultado_final.loc[condiciones_filtro, 'name']
# Obtener los nombres de las series que cumplen con las condiciones

if __name__ == '__main__':
    rutas_csv = [
    r"PEC_4_sol\PEC_4_sol\data\TMDB_distribution.csv",
    r"PEC_4_sol\PEC_4_sol\data\TMDB_info.csv", 
    r"PEC_4_sol\PEC_4_sol\data\TMDB_overview.csv" 
]
    resultado_final = combinar_csv_en_dataframe(rutas_csv)

# Llamar a la función y obtener el resultado procesado
    series_cumplen_condiciones = pro_en_mys_crim(resultado_final)
# Mostrar por pantalla los nombres de las series
    print("Series con idioma original inglés y palabras 'mystery' o 'crime' en el resumen:")
    print(series_cumplen_condiciones.tolist())