# Este programa muestra el clásico mensaje "Hola Mundo"
# Sirve como primer contacto con Python
# print() es una función que muestra texto en la consola
print("¡Hola, Mundo!")


# Este programa muestra varias líneas en consola
# Cada print() se ejecuta en orden
print("La Witsi Witsi Araña subió a su telaraña.")
print("Vino la lluvia y se la llevó.")

# Este programa muestra cómo generar una línea en blanco
print("La Witsi Witsi Araña subió a su telaraña.")
# print() vacío genera un salto de línea
print()
print("Vino la lluvia y se la llevó.")

# Este programa muestra el uso del carácter de escape \n
# \n permite hacer saltos de línea dentro del mismo print
print("La Witsi Witsi Araña\nsubió a su telaraña.")
print()
print("Vino la lluvia\ny se la llevó.")

# Este programa muestra cómo usar varios argumentos en print()
# Los argumentos se separan por comas
# Python automáticamente agrega espacios entre ellos
print("La Witsi Witsi Araña", "subió", "a su telaraña.")

# Este programa muestra cómo funcionan los argumentos posicionales
# El orden en que se escriben los argumentos es el orden en que se muestran
print("Mi nombre es", "Python.")
print("Monty Python.")

# Este programa muestra el uso del argumento end
# end permite cambiar lo que se imprime al final
# Normalmente print termina con un salto de línea (\n)
# Aquí lo cambiamos por un espacio
print("Mi nombre es", "Python.", end=" ")
print("Monty Python.")

# Este programa muestra el uso del argumento sep
# sep cambia el separador entre los argumentos
# Por defecto es un espacio, aquí usamos "-"
print("Mi", "nombre", "es", "Monty", "Python.", sep="-")

# Este programa combina sep y end
# sep cambia el separador entre palabras
# end cambia lo que se imprime al final
print("Mi", "nombre", "es", sep="_", end="*")
print("Monty", "Python.", sep="*", end="*\n")

