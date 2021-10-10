#!/usr/local/bin/python3
from pathlib import Path
import pandas as pd
import os


def app():
    #ruta = "../files"
    ruta = os.environ['ENV_RUTA']

    ruta_csv = ruta + "/data.csv"
    ruta_xlsx = ruta + "/data.xlsx"

    print("----------------")
    print("[*] Leyendo CSV...")
    df = pd.read_csv(ruta_csv)
    print(df.to_string())

    # verificar si existe output
    # print("[*] Verificar directorio output...")
    # verificar_dir(ruta)
    print("---")

    # convertir CSV to XLSX
    print("[*] Convertir CSV to XLSX...")
    #read_file = pd.read_csv(r'../files/data.csv')
    read_file = pd.read_csv(ruta_csv)
    print("Convertir: OK")

    #read_file.to_excel(r'../files/data.xlsx', index=None, header=True)
    read_file.to_excel(ruta_xlsx, index=None, header=True)

    print("[*] Leyendo XLSX...")
    df_excel = pd.read_excel(ruta_xlsx)
    print(df.to_string())

    print("----------------")


def verificar_dir(file_path):
    # verifica si el directorio existe y si no existe, lo crea.
    Path(file_path).mkdir(parents=True, exist_ok=True)


if __name__ == "__main__":
    app()
