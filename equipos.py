import pandas as pd
import os
import pandas as pd
import numpy as npo
import matplotlib.pyplot as plt

def obtener_datos_equipo_csv(file_path):
    try:
        # Utiliza pd.read_csv para leer el archivo CSV
        df_partidos = pd.read_csv(file_path, header=0)
        return df_partidos
    except FileNotFoundError:
        print(f'No se encontró el archivo CSV: {file_path}.')
        return None

def obtener_jugador_mas_ganador(datos_equipo):
    # Aquí debes implementar la lógica para encontrar el jugador con más partidos ganados
    # Devuelve el nombre del jugador y la cantidad de partidos ganados
    # (o devuelve None si no puedes determinar al jugador más ganador)
    pass

def obtener_jugador_mas_ganador(datos_equipo):
    # Supongamos que la columna 'Partidos Ganados' contiene la información necesaria
    # Debes ajustar esto según la estructura real de tus datos
    if 'Partidos Ganados' in datos_equipo.columns:
        # Encuentra el índice del jugador con más partidos ganados
        indice_max_partidos = datos_equipo['Partidos Ganados'].idxmax()

        # Obtiene el nombre del jugador y la cantidad de partidos ganados
        jugador = datos_equipo.at[indice_max_partidos, 'Nombre']
        partidos_ganados = datos_equipo.at[indice_max_partidos, 'Partidos Ganados']

        return jugador, partidos_ganados
    else:
        print('La columna "Partidos Ganados" no está presente en los datos del equipo.')
        return None, None


# Lee el nombre del equipo desde el usuario
nombre_equipo_usuario = input("Ingrese el nombre del equipo: ").strip()

# Construye el nombre del archivo CSV usando el nombre del equipo
nombre_archivo_csv = f'{nombre_equipo_usuario.lower()}_datos_equipo.csv'

# Obtener datos del equipo desde el archivo CSV
datos_equipo = obtener_datos_equipo_csv(nombre_archivo_csv)

if datos_equipo is not None:
    # Obtener el jugador con más partidos ganados
    jugador, partidos_ganados = obtener_jugador_mas_ganador(datos_equipo)

    if jugador is not None:
        print(f'El jugador con más partidos ganados en {nombre_equipo_usuario.capitalize()} es {jugador}, con un total de {partidos_ganados} partidos ganados.')

        # Ejemplo de visualización con matplotlib
        plt.bar(datos_equipo['Nombre'], datos_equipo['Partidos Ganados'])
        plt.xlabel('Jugador')
        plt.ylabel('Partidos Ganados')
        plt.title(f'Partidos Ganados por Jugador en {nombre_equipo_usuario.capitalize()}')
        plt.xticks(rotation=45, ha='right')
        plt.show()
    else:
        print(f'No se pudo determinar el jugador más ganador para {nombre_equipo_usuario.capitalize()}.')
else:
    print(f'No se encontró el archivo CSV: {nombre_archivo_csv}.')


