# main.py
from codcomp import combinar_csv_en_dataframe
from codcomp import combinar_csv_en_diccionario
from codcomp import filtrar_series_japonesas
from codcomp import descomprimir_archivo
from codcomp import pro_url_na
from codcomp import pro_air_days
from codcomp import plot_bar
from codcomp import plot_lin
from codcomp import plot_pie
from codcomp import pro_cancel
from codcomp import pro_en_mys_crim
#Rutas

ruta_tmdb_zip = r"PEC_4_sol\PEC_4_sol\data\TMDB.zip"
lista_rutas_csv = [r"PEC_4_sol\PEC_4_sol\data\TMDB_info.csv", 
         r"PEC_4_sol\PEC_4_sol\data\TMDB_overview.csv", 
         r"PEC_4_sol\PEC_4_sol\data\TMDB_distribution.csv"
         ]
# Descomprimir archivo ZIP (OK)

descomprimir_archivo(ruta_tmdb_zip)

# Integrar los DataFrames a partir de una lista de rutas csv (OK)

resultado_final = combinar_csv_en_dataframe(lista_rutas_csv)
print(resultado_final)

# Integrar los DataFrames en un diccionario a partir de una ruta (OK)

print(combinar_csv_en_diccionario(lista_rutas_csv))

# Filtrar las series japonesas (OK)

japanese_series = filtrar_series_japonesas(resultado_final)

# Mostrar los primeros 20 registros por pantalla (OK)

print("Primeros 20 registros de series en japonés:")
print(japanese_series.head(20))

#Mostrar los primeros 5 registros del diccionario nombre - url

diccionario=pro_url_na(resultado_final)
primeros_5_registros = dict(list(diccionario.items())[:5])
print("Primeros 5 registros del diccionario:")
print(primeros_5_registros)

#Imprimir por días al aire (air_days)

procesado_days=pro_air_days(resultado_final)
top_10_emision=procesado_days.sort_values(by='air_days', ascending=False).head(10)

#Imprimir por series canceladas en el 2023

series_canceladas_2023=pro_cancel(resultado_final)
print("Series que empezaron en 2023 y han sido canceladas (primeros 20):")
print(series_canceladas_2023.head(20).tolist())

# Imprimir por series de crimen y misterio en inglés (en_mys_cri)

series_cumplen_condiciones = pro_en_mys_crim(resultado_final)

# Mostrar por pantalla los nombres de las series

print("Series con idioma original inglés y palabras 'mystery' o 'crime' en el resumen:")
print(series_cumplen_condiciones.tolist())

# Mostrar el gráfico de barras

plot_bar()

#Mostrar el gráfico de líneas

plot_lin()

#Mostrar el gráfico circulas

plot_pie()
