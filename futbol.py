import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def obtener_datos_equipo_csv(file_path):
    try:
        # Utiliza pd.read_csv para leer el archivo CSV
        df_partidos = pd.read_csv(file_path)
        return df_partidos
    except FileNotFoundError:
        print(f'No se encontró el archivo CSV: {file_path}.')
        return None

def obtener_jugador_mas_ganador(datos_equipo):
    if 'Partidos Jugados' in datos_equipo.columns:
        indice_max_partidos = datos_equipo['Partidos Jugados'].idxmax()
        jugador = datos_equipo.at[indice_max_partidos, 'Nombre']
        partidos_ganados = datos_equipo.at[indice_max_partidos, 'Partidos Jugados']
        return jugador, partidos_ganados
    else:
        print('La columna "Partidos Jugados" no está presente en los datos del equipo.')
        return None, None

def calcular_promedio(datos_equipo, jugador):
    datos_jugador = datos_equipo[datos_equipo['Nombre'] == jugador]

    print(f'Columnas disponibles para el jugador {jugador}: {datos_jugador.columns}')

    if 'Goles' in datos_jugador.columns and 'Asistencias' in datos_jugador.columns and 'Amarillas' in datos_jugador.columns and 'Rojas' in datos_jugador.columns:
        promedio_goles = np.mean(datos_jugador['Goles'])
        promedio_asistencias = np.mean(datos_jugador['Asistencias'])
        promedio_amarillas = np.mean(datos_jugador['Amarillas'])
        promedio_rojas = np.nanmean(datos_jugador['Rojas'])
        return promedio_goles, promedio_asistencias, promedio_amarillas, promedio_rojas
    else:
        print('Columnas necesarias no encontradas para calcular el promedio.')
        return None, None, None, None


# Lee el nombre del equipo desde el usuario
nombre_equipo_usuario = input("Ingrese el nombre del equipo de la liga: ").strip()

# Construye el nombre del archivo CSV usando el nombre del equipo
nombre_archivo_csv = f'{nombre_equipo_usuario.lower()}_datos_equipo.csv'

# Obtener datos del equipo desde el archivo CSV
datos_equipo = obtener_datos_equipo_csv('jugadores.csv')

if datos_equipo is not None:
    # Obtener el jugador con más partidos jugados
    jugador, partidos_ganados = obtener_jugador_mas_ganador(datos_equipo)

    if jugador is not None:
        print(f'El jugador con más partidos jugados en {nombre_equipo_usuario.capitalize()} es {jugador}, con un total de {partidos_ganados} partidos jugados.')

        # Calcular el promedio de goles, asistencias, amarillas y rojas del jugador
        promedio_goles, promedio_asistencias, promedio_amarillas, promedio_rojas = calcular_promedio(datos_equipo, jugador)

        if promedio_goles is not None:
            print(f'Promedio de Goles: {promedio_goles}')
            print(f'Promedio de Asistencias: {promedio_asistencias}')
            print(f'Promedio de Amarillas: {promedio_amarillas}')
            print(f'Promedio de Rojas: {promedio_rojas}')

            # Ejemplo de visualización con matplotlib
            plt.bar(datos_equipo['Nombre'], datos_equipo['Partidos Jugados'])
            plt.xlabel('Jugador')
            plt.ylabel('Partidos Jugados')
            plt.title(f'Partidos Jugados por Jugador en {nombre_equipo_usuario.capitalize()}')
            plt.xticks(rotation=45, ha='right')
            plt.show()
        else:
            print(f'No se pudieron calcular los promedios para {jugador}.')
    else:
        print(f'No se pudo determinar el jugador más ganador para {nombre_equipo_usuario.capitalize()}.')
else:
    print(f'No se encontró el archivo CSV: jugadores.csv.')
