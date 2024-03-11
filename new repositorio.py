def calcular_temperatura_promedio(datos):
    temperatura_promedio_ciudades = {}

    for ciudad, semanas in datos.items():
        temperatura_promedio_semanal = {}
        for semana, temperaturas in semanas.items():
            temperatura_promedio_semanal[semana] = sum(temperaturas) / len(temperaturas)
        temperatura_promedio_ciudades[ciudad] = temperatura_promedio_semanal

    return temperatura_promedio_ciudades


# Ejemplo de uso:
datos = {
    'Quito A': {
        'Semana 1': [20, 21, 22, 23, 24, 25, 26],
        'Semana 2': [19, 20, 21, 22, 23, 24, 25]
    },
    'Pastaza B': {
        'Semana 1': [18, 19, 20, 21, 22, 23, 24],
        'Semana 2': [17, 18, 19, 20, 21, 22, 23]
    }
}

resultado = calcular_temperatura_promedio(datos)
for ciudad, semanas in resultado.items():
    print(f'Ciudad: {ciudad}')
    for semana, temp_promedio in semanas.items():
        print(f'Semana: {semana}, Temperatura promedio: {temp_promedio}')