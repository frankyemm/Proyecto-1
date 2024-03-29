import unittest
import pandas as pd
import os
from codcomp import descomprimir_archivo, combinar_csv_en_dataframe, combinar_csv_en_diccionario, pro_air_days, pro_cancel, pro_en_mys_crim, filtrar_series_japonesas

class TestTMDBFunctions(unittest.TestCase):

    def setUp(self):
        # Descomprimir el archivo ZIP antes de las pruebas
        ruta_tmdb_zip = r"PEC_4_sol\PEC_4_sol\data\TMDB.zip"
        descomprimir_archivo(ruta_tmdb_zip)

    def tearDown(self):
        # Eliminar los archivos descomprimidos después de las pruebas
        archivos_csv = [
            r"PEC_4_sol\PEC_4_sol\data\TMDB_info.csv",
            r"PEC_4_sol\PEC_4_sol\data\TMDB_overview.csv",
            r"PEC_4_sol\PEC_4_sol\data\TMDB_distribution.csv"
        ]
        for archivo_csv in archivos_csv:
            if os.path.exists(archivo_csv):
                os.remove(archivo_csv)

    def test_combinar_csv_en_dataframe(self):
        # Rutas a los archivos CSV
        lista_rutas_csv = [
            r"PEC_4_sol\PEC_4_sol\data\TMDB_info.csv",
            r"PEC_4_sol\PEC_4_sol\data\TMDB_overview.csv",
            r"PEC_4_sol\PEC_4_sol\data\TMDB_distribution.csv"
        ]

        # Combina los DataFrames
        resultado_final = combinar_csv_en_dataframe(lista_rutas_csv)

        # Verifica que el DataFrame tenga las columnas correctas
        self.assertEqual(resultado_final.columns.tolist(), ["id", "title", "original_title", "original_language", "genres", "overview", "release_date", "runtime", "vote_average", "vote_count", "budget", "revenue", "popularity", "tagline", "homepage", "production_companies", "production_countries", "spoken_languages", "status", "imdb_id", "tmdb_id", "tvdb_id", "freebase_id", "tvrage_id"])

        # Verifica que el DataFrame tenga el número correcto de filas
        self.assertEqual(len(resultado_final), 165555)

    def test_combinar_csv_en_diccionario(self):
        # Rutas a los archivos CSV
        lista_rutas_csv = [
            r"PEC_4_sol\PEC_4_sol\data\TMDB_info.csv",
            r"PEC_4_sol\PEC_4_sol\data\TMDB_overview.csv",
            r"PEC_4_sol\PEC_4_sol\data\TMDB_distribution.csv"
        ]

        # Combina los DataFrames en un diccionario
        diccionario = combinar_csv_en_diccionario(lista_rutas_csv, "id")

        # Verifica que el diccionario tenga el número correcto de elementos
        self.assertEqual(len(diccionario), 128)

        # Verifica que las claves del diccionario son los IDs únicos
        self.assertEqual(set(diccionario.keys()), set(map(str, range(1, 129))))

    def test_pro_air_days(self):
        # Mock DataFrame para la prueba
        data = {'name': ['Serie1', 'Serie2', 'Serie3'],
                'first_air_date': ['2022-01-01', '2020-01-01', '2021-01-01'],
                'last_air_date': ['2022-12-31', '2023-01-01', '2022-12-31']}
        df = pd.DataFrame(data)

        # Procesa air_days
        df_processed = pro_air_days(df)

        # Verifica que la columna air_days se haya creado correctamente
        self.assertTrue('air_days' in df_processed.columns)

    def test_pro_cancel(self):
        # Mock DataFrame para la prueba
        data = {'name': ['Serie1', 'Serie2', 'Serie3'],
                'first_air_date': ['2022-01-01', '2020-01-01', '2021-01-01'],
                'last_air_date': ['2022-12-31', '2023-01-01', '2022-12-31'],
                'status': ['Canceled', 'Renewed', 'Canceled']}
        df = pd.DataFrame(data)

        # Procesa cancel
        series_canceladas_2023 = pro_cancel(df)

        # Verifica que las series correctas sean canceladas en 2023
        self.assertListEqual(series_canceladas_2023.tolist(), ['Serie1', 'Serie3'])

    def test_pro_en_mys_crim(self):
        # Mock DataFrame para la prueba
        data = {'name': ['Serie1', 'Serie2', 'Serie3'],
                'original_language': ['en', 'fr', 'en'],
                'overview': ['Mystery Crime Drama', 'Comedy', 'Crime Thriller']}
        df = pd.DataFrame(data)

        # Procesa en_mys_crim
        series_cumplen_condiciones = pro_en_mys_crim(df)

        # Verifica que las series correctas cumplan las condiciones
        self.assertListEqual(series_cumplen_condiciones.tolist(), ['Serie1', 'Serie3'])

    def test_filtrar_series_japonesas(self):
        # Mock DataFrame para la prueba
        data = {'name': ['Serie1', 'Serie2', 'Serie3'],
                'languages': ['ja,en', 'fr', 'ja']}
        df = pd.DataFrame(data)

        # Filtra series japonesas
        series_japonesas = filtrar_series_japonesas(df)

        # Verifica que las series correctas sean japonesas
        self.assertListEqual(series_japonesas['name'].tolist(), ['Serie1', 'Serie3'])

if __name__ == '__main__':
    unittest.main()
