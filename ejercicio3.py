def contar_palabras(cadena):

    # Dividir la cadena en palabras
    palabras = cadena.split()

    # Crear un diccionario vacío para contar la frecuencia de cada palabra
    frecuencia = {}

    # Iterar sobre cada palabra en la lista de palabras
    for palabra in palabras:
        # Si la palabra ya está en el diccionario, aumentar su frecuencia en 1
        if palabra in frecuencia:
            frecuencia[palabra] += 1
        # Si no está en el diccionario, agregarla con una frecuencia de 1
        else:
            frecuencia[palabra] = 1

    # Retornar el diccionario con la frecuencia de cada palabra
                
    return frecuencia

cadena = "Si esto sigue asi como asi, ni una triste sombra quedara.Ya se ven los tigres en la lluvia."
frecuencia_palabras = contar_palabras(cadena)
print(frecuencia_palabras)



