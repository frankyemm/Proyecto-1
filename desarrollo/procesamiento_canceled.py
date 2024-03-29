import pandas as pd
from integrarpd import combinar_csv_en_dataframe
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
    rutas_csv = [
        r"PEC_4_sol\PEC_4_sol\data\TMDB_distribution.csv",
        r"PEC_4_sol\PEC_4_sol\data\TMDB_info.csv", 
        r"PEC_4_sol\PEC_4_sol\data\TMDB_overview.csv" 
        
    ]
    resultado_final = combinar_csv_en_dataframe(rutas_csv)
    series_canceladas_2023=pro_cancel(resultado_final)
    print("Series que empezaron en 2023 y han sido canceladas (primeros 20):")
    print(series_canceladas_2023.head(20).tolist())