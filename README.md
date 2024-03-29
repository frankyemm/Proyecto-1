#README
# Programación para la ciencia de datos - PEC4

## Nombre del Proyecto:
PEC4: Análisis de Datos de Series de Televisión con TMDB

## Descripción Breve
Este proyecto realiza un análisis detallado de datos de series de televisión utilizando la base de datos The Movie Database (TMDB). Explora la distribución de géneros, la evolución temporal de las series, la producción en Japón, el estado y cancelaciones de series, y la diversidad de tipos de programas

## Instalación

1.   Clona el repositorio.
2.   Instala las dependencias ejecutando las celdas de instalación de paquetes al principio del notebook.

## Uso

1.  Ejecuta el código principal en orden.
2.  Sigue las instrucciones proporcionadas en el notebook de la PEC4.

## Tests
Se incluyen pruebas y test para determinar la calidad del código. 

## Ejercicios 
#### Ejercicio 1. Descompresion y lectura de archivos
Problema 1.1: Descomprimir Archivo

Este bloque de código define una función llamada descomprimir_archivo que toma una ruta de archivo como parámetro. La función identifica la extensión del archivo y utiliza las bibliotecas zipfile y tarfile para descomprimir el archivo según su extensión (.zip o .tar.gz). Se imprime un mensaje indicando si la operación fue exitosa o si hay algún error.

Ejemplo de Uso:

ruta_tmdb_zip = r"C:\Users\XXXX\XXXX\XXXX\dXXXX\activity_4-master\data\TMDB.zip"
descomprimir_archivo(ruta_tmdb_zip)
Resultados Esperados:

Se descomprimirá el archivo TMDB.zip en el mismo directorio que el archivo original, y se imprimirá un mensaje indicando el éxito de la operación.
Problema 1.2: Combinar CSV en DataFrame

Este bloque define una función llamada combinar_csv_en_dataframe que toma una lista de rutas de archivos CSV como parámetro. La función lee cada archivo CSV en un DataFrame de pandas, combina estos DataFrames en uno único utilizando la columna "id" como clave, y elimina duplicados. El tiempo de procesamiento se imprime al final.

Ejemplo de Uso:

python
Copy code
rutas_csv = [
    r"C:\Users\XXXX\XXXX\XXXX\dXXXX\activity_4-master\data\TMDB_distribution.csv",
    r"C:\Users\XXXX\XXXX\XXXX\dXXXX\activity_4-master\data\TMDB_info.csv", 
    r"C:\Users\XXXX\XXXX\XXXX\dXXXX\activity_4-master\data\TMDB_overview.csv" 
]
resultado_final = combinar_csv_en_dataframe(rutas_csv)
Resultados Esperados:

Se leerán y combinarán los archivos CSV especificados en un DataFrame. El DataFrame resultante se imprimirá, y se mostrará el tiempo de procesamiento.
Problema 1.3: Combinar CSV en Diccionario

Este bloque define una función llamada combinar_csv_en_diccionario que toma una lista de rutas de archivos CSV como parámetro. La función lee cada archivo CSV y combina los datos en un diccionario utilizando la columna "id" como clave. El tiempo de procesamiento se imprime al final.

Ejemplo de Uso:

rutas_csv = [
    r"C:\Users\XXXX\XXXX\XXXX\dXXXX\activity_4-master\data\TMDB_distribution.csv",
    r"C:\Users\XXXX\XXXX\XXXX\dXXXX\activity_4-master\data\TMDB_info.csv", 
    r"C:\Users\XXXX\XXXX\XXXX\dXXXX\activity_4-master\data\TMDB_overview.csv" 
]
diccionario_resultado = combinar_csv_en_diccionario(rutas_csv)
Resultados Esperados:

Se leerán los archivos CSV especificados y se combinarán en un diccionario utilizando "id" como clave. El diccionario resultante se imprimirá, y se mostrará el tiempo de procesamiento.
Problema 1.4: Comparación entre Métodos de Combinación

En este bloque, se proporciona una comparación entre dos métodos de combinación de archivos CSV: uno utilizando la biblioteca pandas y otro utilizando el módulo csv y diccionario. Se enumeran ventajas y desventajas de cada método y se menciona que la elección puede depender del tamaño del archivo.

Resultados Esperados:

Una descripción detallada de las ventajas y desventajas de ambos métodos y una recomendación basada en el tamaño del archivo.

#### Ejercicio 2. Procesamiento de datos

Problema 2.1: Análisis de Duración de Series

Este bloque resuelve el problema 2.1. Convierte las columnas de fechas "first_air_date" y "last_air_date" al formato de fecha utilizando la biblioteca pandas. Luego, calcula la duración en días de la emisión de las series y muestra las 10 series con mayor duración.

Resultados Esperados:

Se esperan datos sobre la duración de las series y una visualización de las 10 series con mayor duración.
Problema 2.2: Procesamiento de Posters

En este bloque, se resuelve el problema 2.2. Se llenan los valores NaN o "" en las columnas "homepage" y "poster_path". Luego, se crea un diccionario de posters utilizando las columnas "homepage" y "poster_path".

Resultados Esperados:

Se espera un diccionario de posters con los primeros 5 registros.
Continuaré en otro mensaje para abordar los problemas restantes.

#### Ejercicio 3. Filtrado de datos

Problema 3.1: Encontrar Series Interesantes

En este bloque se resuelve el problema 3.1. Se definen condiciones de filtro para encontrar series con idioma original inglés y palabras 'mystery' o 'crime' en el resumen. Se muestran por pantalla los nombres de las series que cumplen con estas condiciones.

Resultados Esperados:

Se esperan los nombres de las series que cumplen con las condiciones establecidas.
Problema 3.2: Series Canceladas en 2023

Este bloque resuelve el problema 3.2. Se establecen condiciones de filtro para encontrar series que empezaron en 2023 y han sido canceladas. Se muestran por pantalla los primeros 20 elementos de la lista de estas series.

Resultados Esperados:

Se esperan los nombres de las series que cumplen con las condiciones de cancelación en 2023.
Problema 3.3: Series en Japonés

En este bloque se resuelve el problema 3.3. Se crea un DataFrame con nombres, nombres originales, plataformas de emisión y empresas productoras de series cuyo idioma es japonés. Se muestran por pantalla los primeros 20 registros de este DataFrame.

Resultados Esperados:

Se esperan datos sobre series en japonés y una visualización de los primeros 20 registros.


#### Ejercicio 4. Análisis gráfico

Problema 4.1: Gráfico de Barras por Año de Inicio

En este bloque se resuelve el problema 4.1. Se presenta un gráfico de barras que muestra el número de series por año de inicio.

Resultados Esperados:

Se espera un gráfico de barras que representa el número de series por año de inicio.
Problema 4.2: Gráfico de Líneas por Década y Tipo

Este bloque resuelve el problema 4.2. Se construye un gráfico de líneas que muestra el número de series por década y categoría de "type".

Resultados Esperados:

Se espera un gráfico de líneas que representa el número de series por década y tipo.
Problema 4.3: Gráfico Circular de Porcentaje de Géneros

En este bloque se resuelve el problema 4.3. Se obtiene el número de series por género y se presenta en un gráfico circular.

Resultados Esperados:

Se espera un gráfico circular que representa el porcentaje de series por género.


#### Ejercicio 5. Conclusiones

## Ejerccio 5. Conclusiones

**Informe de Análisis de Datos de Series de Televisión**

**Resumen:**
En este informe, se presenta una revisión detallada del análisis de datos relacionados con series de televisión, utilizando la extensa base de datos proporcionada por The Movie Database (TMDB). Nuestra metodología se basó en el uso de herramientas de análisis de datos en Python, específicamente Pandas y Matplotlib, en el entorno de Google Colab. A continuación, resumimos las principales conclusiones derivadas de este análisis exhaustivo.

   - Se examinó de cerca la distribución de géneros en las series de televisión. Géneros como Drama, Comedia, Acción y Aventura se destacaron como los más comunes.
   - Representamos visualmente el porcentaje de series por género en un gráfico circular, agrupando los géneros que representan menos del 1% bajo la categoría "Other".
   - Exploramos la evolución de las series a lo largo de las décadas desde la década de 1940, identificando tendencias y cambios significativos en la producción televisiva.
   - Se focalizó en las series cuyo idioma original es japonés o que incluyen japonés como idioma adicional. Se recopilaron detalles esenciales, como nombres, plataformas de emisión y empresas productoras.
   - Analizamos las series que iniciaron en 2023 y fueron canceladas, proporcionando insights sobre la duración y éxito de las nuevas producciones.
   - Exploramos la diversidad de tipos de programas de televisión presentes en la base de datos y analizamos su distribución a lo largo de las décadas.

**Conclusiones Generales:**
Este análisis ha proporcionado una visión integral de la industria televisiva, destacando patrones significativos en áreas como géneros populares, evolución temporal y producciones japonesas. Estas conclusiones no solo ofrecen una panorámica general, sino que también sirven como punto de partida para investigaciones más específicas y detalladas en futuros análisis de datos.

