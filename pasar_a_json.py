# Práctica 1 Bloque 3 - Adquisición de datos - IMAT
# Autor: Lara Ocón Madrid

# En esta práctica vamos a pasar el csv con los leaks obtenidos en la Practica de
# Git Leaks a un json

import pandas as pd
import json

def extract(fichero):
    # Leemos el fichero csv, eliminamos la columna Unnamed: 0 y lo pasamos a un dataframe
    df = pd.read_csv(fichero).drop(columns=['Unnamed: 0'])
    return df


def transform(df):
    # creamos el diccionario 
    dic = {}
    # recorremos el dataframe
    for i in range(len(df)):
        # creamos un diccionario donde la clave es el hash y el valor el mensaje
        dic[df.loc[i]['Hash']] = df.loc[i]['Mensaje']
    return dic


def load(dic):
    # pasamos el diccionario a un json
    with open('leaks.json', 'w') as f:
        json.dump(dic, f, indent=4)
    return dic

if __name__ == "__main__":

    # Extraemos el csv y lo cargamos en un pandas dataframe
    df = extract("leaks_encontrados.csv")
    # Transformamos el dataframe en un diccionario
    dic = transform(df)
    # Cargamos el diccionario en un json: "leaks.json"
    load(dic)