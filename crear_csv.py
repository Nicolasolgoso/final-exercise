import csv

# Datos que deseas escribir en el archivo CSV
datos = [
    ["Jugador1", 20, 30, 10],
    ["Jugador2", 15, 25, 8],
    ["Jugador3", 18, 28, 12]
]

# Nombre del archivo CSV
nombre_archivo_csv = 'datos_equipo.csv'

# Escribir en el archivo CSV
with open(nombre_archivo_csv, mode='w', newline='') as file:
    writer = csv.writer(file)
    
    # Escribir el encabezado
    writer.writerow(['Nombre', 'Partidos Ganados', 'Partidos Jugados', 'Goles Marcados'])
    
    # Escribir los datos
    writer.writerows(datos)

print(f'Se ha creado el archivo CSV: {nombre_archivo_csv}')
