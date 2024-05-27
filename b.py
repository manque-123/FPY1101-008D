arreglo = [
    [["amarillo", "rojo", "Naranja"], ["Verde", "Blanco", "amarillo"], ["rojo", "Naranja", "Verde"]],
    [["Blanco", "amarillo", "rojo"], ["Naranja", "Verde", "Blanco"], ["amarillo", "rojo", "Naranja"]],
    [["Verde", "Blanco", "amarillo"], ["rojo", "Naranja", "Verde"], ["Blanco", "amarillo", "rojo"]]
]

# Contar el número de elementos de cada color
num_amarillo = sum(sublista.count("amarillo") for lista in arreglo for sublista in lista)
num_rojo = sum(sublista.count("rojo") for lista in arreglo for sublista in lista)
num_naranja = sum(sublista.count("Naranja") for lista in arreglo for sublista in lista)
num_verde = sum(sublista.count("Verde") for lista in arreglo for sublista in lista)
num_blanco = sum(sublista.count("Blanco") for lista in arreglo for sublista in lista)

# Mostrar la información
print("Número de elementos 'amarillo':", num_amarillo)
print("Número de elementos 'rojo':", num_rojo)
print("Número de elementos 'Naranja':", num_naranja)
print("Número de elementos 'Verde':", num_verde)
print("Número de elementos 'Blanco':", num_blanco)