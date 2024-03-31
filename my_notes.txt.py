# Creación y escritura de notas en el archivo my_notes.txt
with open('my_notes.txt', 'w') as file:
    file.write("Notas Personales:\n")
    file.write("1. Revisar todas las mañanas el SERCOP\n")
    file.write("2. Tener en cuenta las fechas de los contratos\n")
    file.write("3. Terminar el informe del trabajo.\n")

# Lectura del contenido del archivo my_notes.txt
print("Contenido de my_notes.txt:")
with open('my_notes.txt', 'r') as file:
    # Leer el contenido del archivo línea por línea
    for line in file:
        # Imprimir cada línea en la consola
        print(line.strip())  # strip() elimina los caracteres de nueva línea al final de cada línea

# Cierre automático del archivo después de salir del bloque 'with'
# No es necesario agregar una línea de cierre de archivo explícita