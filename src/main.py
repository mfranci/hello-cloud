#!/usr/local/bin/python3
from pathlib import Path
import pandas as pd
import os


def buscar_archivos(ruta, extension=".csv"):
    archivos = []
    for file in os.listdir(ruta):
        if file.endswith(extension):
            # print(file)
            archivos.append(file)
    return archivos


def convertir_csv_xlsx(ruta, archivos_csv):
    for archivo_csv in archivos_csv:
        ruta_csv = ruta + "/" + archivo_csv
        ruta_xlsx = ruta + "/" + archivo_csv.replace(".csv", ".xlsx")

        print(f'Archivo csv: {ruta_csv}')

        #print("[*] Leyendo CSV...")
        #df = pd.read_csv(ruta_csv)
        # print(df.to_string())

        # verificar si existe output
        ## print("[*] Verificar directorio output...")
        # verificar_dir(ruta)
        # print("---")

        # convertir CSV to XLSX
        print("[*] Convertir CSV to XLSX...")
        print(f'Archivo xlsx: {ruta_xlsx}')
        read_file = pd.read_csv(ruta_csv)
        read_file.to_excel(ruta_xlsx, index=None, header=True)
        print("Convertir CSV a XLSX: OK")

        print("[*] Leyendo XLSX...")
        df_excel = pd.read_excel(ruta_xlsx)
        print(df_excel.to_string())


def verificar_dir(file_path):
    # verifica si el directorio existe y si no existe, lo crea.
    Path(file_path).mkdir(parents=True, exist_ok=True)


def app():
    print("----------------")
    ruta = os.environ.get('ENV_RUTA')

    if not ruta:
        print("[!] No existe ENV_RUTA, se utiliza path por defecto")
        ruta = "../files"
    else:
        print("[*] Existe ENV_RUTA")

    print(f'RUTA: {ruta}')

    archivos_csv = buscar_archivos(ruta)
    print(archivos_csv)
    convertir_csv_xlsx(ruta, archivos_csv)

    print("----------------")


if __name__ == "__main__":
    app()
