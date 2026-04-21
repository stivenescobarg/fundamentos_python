# 🐍 Fundamentos de Python

## 📌 Sección 1 – Hola Mundo y función `print()`

En esta sección se desarrollaron varios programas básicos en Python con el objetivo de comprender el funcionamiento de la función `print()`, el manejo de cadenas de texto y la forma en que se muestran los datos en la consola.

---

## 🧠 ¿Qué es `print()`?

La función `print()` es una función integrada de Python que permite mostrar información en la consola. Es una de las herramientas más importantes, ya que permite visualizar los resultados de un programa.

**Ejemplo:**

```python
print("¡Hola, Mundo!")
Salida:

¡Hola, Mundo!
🧵 Uso de cadenas
Las cadenas son textos que se escriben entre comillas. Estas pueden ser simples (' ') o dobles (" ").

Ejemplo:

python
print("Hola")
📌 Múltiples instrucciones
Un programa puede tener varias instrucciones, y estas se ejecutan en orden de arriba hacia abajo.

Ejemplo:

python
print("Hola")
print("Mundo")
Salida:


Hola
Mundo
⬇️ Saltos de línea
Python permite generar saltos de línea de dos formas:

✔ Usando print() vacío

python
print("Hola")
print()
print("Mundo")
✔ Usando el carácter de escape \n

python
print("Hola\nMundo")
🔗 Múltiples argumentos
La función print() puede recibir varios argumentos separados por comas. Python los mostrará en una sola línea separados por espacios.

Ejemplo:

python
print("Hola", "Mundo")
Salida:


Hola Mundo
⚙️ Argumentos especiales de print()
✔ sep (separador)
Permite cambiar el separador entre los argumentos.

python
print("Hola", "Mundo", sep="-")
Salida:


Hola-Mundo
✔ end (final)
Permite cambiar lo que se imprime al final.

python
print("Hola", end=" ")
print("Mundo")
Salida:


Hola Mundo


🧪 LAB – La función print() y sus argumentos
📌 Descripción del problema
En este laboratorio se debía modificar una instrucción print() utilizando los argumentos de palabra clave sep y end, con el objetivo de obtener una salida específica sin modificar la segunda función print().

🎯 Objetivo
Lograr la siguiente salida en consola:


ProgrammingEssentialsin...Python
💡 Lógica utilizada
Para resolver el ejercicio se utilizaron dos argumentos clave de la función print():

sep : permite definir cómo se separan los argumentos dentro de print().

end : permite definir qué se imprime al final de la instrucción, evitando el salto de línea por defecto.

Se configuró:

sep="***" para separar las palabras con tres asteriscos.

end="..." para evitar el salto de línea y agregar puntos suspensivos, permitiendo que el siguiente print() continúe en la misma línea.

🧾 Código utilizado
python
print("Programming", "Essentials", "in", sep="***", end="...")
print("Python")
📤 Resultado en consola

Programming***Essentials***in...Python


🧪 LAB – Dando formato a la salida
📌 Descripción del problema
En este laboratorio se trabajó con la función print() para comprender cómo dar formato a la salida en consola, utilizando cadenas, caracteres de escape y operaciones con o.

🎯 Objetivos del ejercicio
Reducir el número de instrucciones print() usando \n

Manipular cadenas para construir figuras

Duplicar una figura en consola

Comprender cómo funcionan los errores en Python

💡 Lógica utilizada
Se utilizó el carácter de escape \n para generar saltos de línea dentro de una sola cadena, lo que permitió reducir múltiples llamadas a print().

Además, se aplicó la concatenación de cadenas para construir una segunda figura (flecha) ubicada al lado de la primera.

También se exploró el uso de operaciones con cadenas como la multiplicación y la combinación de textos.

🧾 Código utilizado
python
flecha = (
    "    *\n"
    "   * *\n"
    "  *   *\n"
    " *     *\n"
    "***   ***\n"
    "  *   *\n"
    "  *   *\n"
    "  *****"
)

print(flecha)

print()

flecha_doble = (
    "    *     " + "    *\n" +
    "   * *    " + "   * *\n" +
    "  *   *   " + "  *   *\n" +
    " *     *  " + " *     *\n" +
    "***   *** " + "***   ***\n" +
    "  *   *   " + "  *   *\n" +
    "  *   *   " + "  *   *\n" +
    "  *****   " + "  *****"
)

print(flecha_doble)
📤 Resultado en consola
text
    *
   * *
  *   *
 *     *
***   ***
  *   *
  *   *
  *****

    *         *
   * *       * *
  *   *     *   *
 *     *   *     *
***   ******   ***
  *   *     *   *
  *   *     *   *
  *****     *****

##  📌 Sección 2 – Literales de Python

En esta sección se estudiaron los diferentes tipos de literales en Python, es decir, los valores que se escriben directamente en el código.

---

## 🧠 ¿Qué es un literal?

Un literal es un valor fijo que se escribe directamente en el programa.

**Ejemplos:**

```python
123
"Hola"
True
🔢 Tipos de literales
✔ Enteros (int)
Son números sin parte decimal.

python
print(123)
print(-50)
print(11_111_111)
Salida:

text
123
-50
11111111
✔ Números en otros sistemas
Octal
python
print(0o123)
Salida:

text
83
Hexadecimal
python
print(0x123)
Salida:

text
291
✔ Números flotantes (float)
Son números con decimales.

python
print(2.5)
print(.4)
print(4.)
✔ Notación científica
Permite representar números grandes o pequeños.

python
print(3E8)
print(6.62607E-34)
✔ Cadenas (string)
Son textos entre comillas.

python
print("Hola")
print('Python')
Uso de comillas dentro de cadenas
python
print("Me gusta \"Monty Python\"")
print('Me gusta "Monty Python"')
✔ Valores booleanos (bool)
Representan verdadero o falso.

python
print(True)
print(False)
❓ Pregunta importante (RETO)
Código:

python
print(True > False)
print(True < False)
Resultado:

text
True
False
💡 Explicación
En Python:

True equivale a 1

False equivale a 0

Entonces:

True > False → 1 > 0 → True

True < False → 1 < 0 → False

⚠️ Diferencia importante
python
print("2")  # cadena (string)
print(2)    # número (int)
Aunque se ven iguales en la consola, son tipos diferentes en memoria.

🧪 LAB – Literales de Python: Cadenas
📌 Descripción del problema
En este laboratorio se debía imprimir una cadena específica que contiene múltiples comillas dobles, utilizando correctamente los literales de tipo cadena en Python.

🎯 Objetivo
Obtener la siguiente salida en consola:

text
"Estoy"""aprendiendo"""""Python"""
💡 Lógica utilizada
Para resolver el ejercicio se utilizaron comillas simples (' ') para delimitar la cadena principal. Esto permitió incluir comillas dobles (" ") dentro del texto sin necesidad de usar caracteres de escape.

Python interpreta todo el contenido entre comillas simples como texto literal, por lo que las comillas triples (""") se imprimen sin problema.

🧾 Código utilizado
python
print('"Estoy"""aprendiendo"""""Python"""')
📤 Resultado en consola
text
"Estoy"""aprendiendo"""""Python"""