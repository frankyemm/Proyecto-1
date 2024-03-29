# Problema 2.1 Resuelto utilizando el problema 1.2 librería Pandas
import pandas as pd
from integrarpd import combinar_csv_en_dataframe
def pro_air_days(resultado_final):
# Convertir las columnas first_air_date y last_air_date en formato de fecha
    resultado_final['first_air_date']=pd.to_datetime(resultado_final['first_air_date'])
    resultado_final['last_air_date']=pd.to_datetime(resultado_final['last_air_date'])
    # Añadir la variable air_days al DataFrame
    resultado_final['air_days']=(resultado_final['last_air_date']-resultado_final['first_air_date']).dt.days
    return resultado_final
# Mostrar los 10 registros que más días han estado en emisión
if __name__ == "__main__":
    rutas_csv = [r"PEC_4_sol\PEC_4_sol\data\TMDB_info.csv", 
         r"PEC_4_sol\PEC_4_sol\data\TMDB_overview.csv", 
         r"PEC_4_sol\PEC_4_sol\data\TMDB_distribution.csv"
         ]
    resultado_final = combinar_csv_en_dataframe(rutas_csv)
    procesado_days=pro_air_days(resultado_final)
    top_10_emision=procesado_days.sort_values(by='air_days', ascending=False).head(10)

# Imprimir el DataFrame resultante, para hacerlo borra el # que está a la izquierda del print

    print(top_10_emision)