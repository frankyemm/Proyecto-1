#Listo el pollo
import pandas as pd
from integrarpd import combinar_csv_en_dataframe
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
    print("Primeros 20 registros de series en japonés:")
    rutas_csv = [r"PEC_4_sol\PEC_4_sol\data\TMDB_info.csv",
                 r"PEC_4_sol\PEC_4_sol\data\TMDB_overview.csv",
                 r"PEC_4_sol\PEC_4_sol\data\TMDB_distribution.csv"]
    resultado_final=combinar_csv_en_dataframe(rutas_csv)
    resultado_series=filtrar_series_japonesas(resultado_final)
    print(resultado_series.head(20))