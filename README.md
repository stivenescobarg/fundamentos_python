## 📌 Sección 1 – Hola Mundo y la función `print()`

En esta sección se desarrollaron varios programas básicos en Python con el objetivo de comprender el funcionamiento de la función `print()`, el manejo de cadenas de texto y la forma en que se muestran los datos en la consola.

---

### 🧠 ¿Qué es `print()`?

La función `print()` es una función integrada de Python que permite mostrar información en la consola. Es una de las herramientas más importantes, ya que permite visualizar los resultados de un programa.



```python
print("¡Hola, Mundo!")
```

```
¡Hola, Mundo!
```

---

### 🧵 Uso de cadenas

Las cadenas son textos que se escriben entre comillas. Estas pueden ser simples (`' '`) o dobles (`" "`).

```python
print("Hola")
```

---

### 📌 Múltiples instrucciones

Un programa puede tener varias instrucciones, y estas se ejecutan en orden de arriba hacia abajo.

```python
print("Hola")
print("Mundo")
```

```
Hola
Mundo
```

---

### ⬇️ Saltos de línea

Python permite generar saltos de línea de dos formas:

**✔ Usando `print()` vacío**
```python
print("Hola")
print()
print("Mundo")
```

**✔ Usando el carácter de escape `\n`**
```python
print("Hola\nMundo")
```

---

### 🔗 Múltiples argumentos

La función `print()` puede recibir varios argumentos separados por comas. Python los mostrará en una sola línea separados por espacios.

```python
print("Hola", "Mundo")
```

```
Hola Mundo
```

---

### ⚙️ Argumentos especiales de `print()`

**✔ `sep` — separador**

Permite cambiar el separador entre los argumentos.

```python
print("Hola", "Mundo", sep="-")
```
```
Hola-Mundo
```

**✔ `end` — final**

Permite cambiar lo que se imprime al final.

```python
print("Hola", end=" ")
print("Mundo")
```
```
Hola Mundo
```

---

## 📌 Sección 2 – Literales de Python

En esta sección se estudiaron los diferentes tipos de literales en Python, es decir, los valores que se escriben directamente en el código.

---

### 🧠 ¿Qué es un literal?

Un literal es un valor fijo que se escribe directamente en el programa.

```python
123
"Hola"
True
```

---

### 🔢 Tipos de literales

#### ✔ Enteros (`int`)

Son números sin parte decimal.

```python
print(123)
print(-50)
print(11_111_111)
```
```
123
-50
11111111
```

#### ✔ Números en otros sistemas

**Octal:**
```python
print(0o123)   # → 83
```

**Hexadecimal:**
```python
print(0x123)   # → 291
```

#### ✔ Números flotantes (`float`)

Son números con decimales.

```python
print(2.5)
print(.4)
print(4.)
```

#### ✔ Notación científica

Permite representar números grandes o pequeños.

```python
print(3E8)
print(6.62607E-34)
```

#### ✔ Cadenas (`string`)

Son textos entre comillas.

```python
print("Hola")
print('Python')

# Uso de comillas dentro de cadenas
print("Me gusta \"Monty Python\"")
print('Me gusta "Monty Python"')
```

#### ✔ Valores booleanos (`bool`)

Representan verdadero o falso.

```python
print(True)
print(False)
```

---

### ❓ Reto: Comparación de booleanos

```python
print(True > False)
print(True < False)
```

```
True
False
```

> 💡 En Python, `True` equivale a `1` y `False` equivale a `0`.  
> Por eso: `True > False` → `1 > 0` → `True`  
> Y: `True < False` → `1 < 0` → `False`

---

### ⚠️ Diferencia importante

```python
print("2")  # cadena (string)
print(2)    # número (int)
```

Aunque se ven iguales en consola, son **tipos diferentes en memoria**.

---

## 📌 Sección 3 – Operadores en Python

En esta sección se trabajó con operadores aritméticos para manipular datos y realizar cálculos, comprendiendo cómo Python evalúa las expresiones.

---

### 🧠 ¿Qué es un operador?

Un operador es un símbolo que permite realizar operaciones con valores.

```python
print(2 + 2)   # → 4
```

---

### 🔢 Operadores básicos

| Operador | Función           |
|:--------:|-------------------|
| `+`      | Suma              |
| `-`      | Resta             |
| `*`      | Multiplicación    |
| `/`      | División          |
| `//`     | División entera   |
| `%`      | Módulo (residuo)  |
| `**`     | Potencia          |

---

### ⚠️ Reglas importantes

**✔ División (`/`) — siempre devuelve `float`**
```python
print(6 / 3)   # → 2.0
```

**✔ División entera (`//`) — redondea hacia abajo**
```python
print(6 // 4)  # → 1
```

**✔ Módulo (`%`) — devuelve el residuo**
```python
print(14 % 4)  # → 2
```

---

### ❓ Ejercicios importantes

---

## 🧮 Ejercicios de Operadores Matemáticos

> En esta sección se documentan 15 ejercicios que aplican las reglas de **prioridad de operadores** en Python. Para cada uno se muestra la expresión, el desglose paso a paso y el resultado final.

---

### 📐 Reglas aplicadas

| Prioridad | Operadores           | Asociatividad       |
|:---------:|----------------------|---------------------|
| 1 (mayor) | `**`                 | Derecha a izquierda |
| 2         | `-x` (negación)      | Derecha a izquierda |
| 3         | `*`, `/`, `//`, `%`  | Izquierda a derecha |
| 4 (menor) | `+`, `-`             | Izquierda a derecha |
| —         | `( )`                | Se evalúan primero  |

---

### Ejercicio 1

```python
5 + 3 * 2
```

| Paso | Operación  | Resultado |
|:----:|:----------:|:---------:|
| 1    | `3 * 2`    | `6`       |
| 2    | `5 + 6`    | `11`      |

> ✅ Resultado: **`11`**

---

### Ejercicio 2

```python
8 / 2 + 4 * 3
```

| Paso | Operación  | Resultado |
|:----:|:----------:|:---------:|
| 1    | `8 / 2`    | `4.0`     |
| 2    | `4 * 3`    | `12`      |
| 3    | `4.0 + 12` | `16.0`    |

> ✅ Resultado: **`16.0`**

---

### Ejercicio 3

```python
(7 + 3) * 2 - 5
```

| Paso | Operación   | Resultado |
|:----:|:-----------:|:---------:|
| 1    | `7 + 3`     | `10`      |
| 2    | `10 * 2`    | `20`      |
| 3    | `20 - 5`    | `15`      |

> ✅ Resultado: **`15`**

---

### Ejercicio 4

```python
10 - 4 + 2 * 3
```

| Paso | Operación  | Resultado |
|:----:|:----------:|:---------:|
| 1    | `2 * 3`    | `6`       |
| 2    | `10 - 4`   | `6`       |
| 3    | `6 + 6`    | `12`      |

> ✅ Resultado: **`12`**

---

### Ejercicio 5

```python
(10 / 2) * (3 + 2) - 4
```

| Paso | Operación    | Resultado |
|:----:|:------------:|:---------:|
| 1    | `10 / 2`     | `5.0`     |
| 2    | `3 + 2`      | `5`       |
| 3    | `5.0 * 5`    | `25.0`    |
| 4    | `25.0 - 4`   | `21.0`    |

> ✅ Resultado: **`21.0`**

---

### Ejercicio 6

```python
2 + 3 * (4 - 1)
```

| Paso | Operación  | Resultado |
|:----:|:----------:|:---------:|
| 1    | `4 - 1`    | `3`       |
| 2    | `3 * 3`    | `9`       |
| 3    | `2 + 9`    | `11`      |

> ✅ Resultado: **`11`**

---

### Ejercicio 7

```python
5 * 2 ** 3
```

| Paso | Operación  | Resultado |
|:----:|:----------:|:---------:|
| 1    | `2 ** 3`   | `8`       |
| 2    | `5 * 8`    | `40`      |

> ✅ Resultado: **`40`**

---

### Ejercicio 8

```python
6 + 4 / 2 ** 2
```

| Paso | Operación  | Resultado |
|:----:|:----------:|:---------:|
| 1    | `2 ** 2`   | `4`       |
| 2    | `4 / 4`    | `1.0`     |
| 3    | `6 + 1.0`  | `7.0`     |

> ✅ Resultado: **`7.0`**

---

### Ejercicio 9

```python
10 % 3 + 2 * 5
```

| Paso | Operación  | Resultado |
|:----:|:----------:|:---------:|
| 1    | `10 % 3`   | `1`       |
| 2    | `2 * 5`    | `10`      |
| 3    | `1 + 10`   | `11`      |

> ✅ Resultado: **`11`**

---

### Ejercicio 10

```python
(8 + 2) * 3 ** 2
```

| Paso | Operación  | Resultado |
|:----:|:----------:|:---------:|
| 1    | `8 + 2`    | `10`      |
| 2    | `3 ** 2`   | `9`       |
| 3    | `10 * 9`   | `90`      |

> ✅ Resultado: **`90`**

---

### Ejercicio 11

```python
7 + 2 * (3 + 5) / 4
```

| Paso | Operación  | Resultado |
|:----:|:----------:|:---------:|
| 1    | `3 + 5`    | `8`       |
| 2    | `2 * 8`    | `16`      |
| 3    | `16 / 4`   | `4.0`     |
| 4    | `7 + 4.0`  | `11.0`    |

> ✅ Resultado: **`11.0`**

---

### Ejercicio 12

```python
2 ** 3 * 4 / 2
```

| Paso | Operación  | Resultado |
|:----:|:----------:|:---------:|
| 1    | `2 ** 3`   | `8`       |
| 2    | `8 * 4`    | `32`      |
| 3    | `32 / 2`   | `16.0`    |

> ✅ Resultado: **`16.0`**

---

### Ejercicio 13

```python
9 - 6 + 3 ** 2
```

| Paso | Operación  | Resultado |
|:----:|:----------:|:---------:|
| 1    | `3 ** 2`   | `9`       |
| 2    | `9 - 6`    | `3`       |
| 3    | `3 + 9`    | `12`      |

> ✅ Resultado: **`12`**

---

### Ejercicio 14

```python
(7 - 2) * 5 + 3 ** 2
```

| Paso | Operación  | Resultado |
|:----:|:----------:|:---------:|
| 1    | `7 - 2`    | `5`       |
| 2    | `3 ** 2`   | `9`       |
| 3    | `5 * 5`    | `25`      |
| 4    | `25 + 9`   | `34`      |

> ✅ Resultado: **`34`**

---

### Ejercicio 15

```python
4 * 2 ** 3 / 8 + 1
```

| Paso | Operación  | Resultado |
|:----:|:----------:|:---------:|
| 1    | `2 ** 3`   | `8`       |
| 2    | `4 * 8`    | `32`      |
| 3    | `32 / 8`   | `4.0`     |
| 4    | `4.0 + 1`  | `5.0`     |

> ✅ Resultado: **`5.0`**

---

## 🧪 Laboratorios

---

### LAB 1 – Trabajando con la función `print()`

**Descripción:** Se utilizó la función `print()` para mostrar mensajes en pantalla, comprendiendo su sintaxis básica y algunos errores comunes.

**Lógica utilizada:**
1. Se utilizó `print()` para mostrar el texto `"¡Hola, Mundo!"`.
2. Se imprimió un nombre usando otra llamada a `print()`.
3. Se realizaron pruebas eliminando elementos clave del código para observar errores.

**Errores observados:**

| Situación       | Error generado |
|-----------------|----------------|
| Sin comillas    | `NameError` — Python interpreta el texto como una variable no definida |
| Sin paréntesis  | `SyntaxError` — En Python 3, `print` es una función y requiere paréntesis |

---

### LAB 2 – La función `print()` y sus argumentos

**Objetivo:** Lograr la siguiente salida sin modificar la segunda instrucción `print()`:

```
Programming***Essentials***in...Python
```

**Lógica utilizada:**

Se configuraron los argumentos `sep` y `end`:
- `sep="***"` → separa los argumentos con tres asteriscos.
- `end="..."` → evita el salto de línea y agrega puntos suspensivos.

```python
print("Programming", "Essentials", "in", sep="***", end="...")
print("Python")
```

```
Programming***Essentials***in...Python
```

---

### LAB 3 – Dando formato a la salida

**Objetivos:**
- Reducir el número de instrucciones `print()` usando `\n`
- Manipular cadenas para construir figuras
- Duplicar una figura en consola

**Código utilizado:**

```python
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
```

**Resultado en consola:**

```
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
```

---

### LAB 4 – Literales de Python: Cadenas

**Objetivo:** Imprimir la siguiente cadena que contiene múltiples comillas dobles:

```
"Estoy"""aprendiendo"""""Python"""
```

**Lógica utilizada:**  
Se usaron comillas simples (`' '`) para delimitar la cadena principal, permitiendo incluir comillas dobles dentro del texto sin caracteres de escape.

```python
print('"Estoy"""aprendiendo"""""Python"""')
```

---

### LAB 5 – Variables en Python -- Sección 4

**Descripción:** Se crearon variables para representar la cantidad de manzanas de tres personas.

| Persona | Variable | Valor |
|:-------:|:--------:|:-----:|
| John    | `john`   | `3`   |
| Mary    | `mary`   | `5`   |
| Adam    | `adam`   | `6`   |



```python
john = 3
mary = 5
adam = 6

print(john, mary, adam)

total_apples = john + mary + adam
print(total_apples)

print("Número total de manzanas:", total_apples)
```

```
3 5 6
14
Número total de manzanas: 14
```

---

### LAB 6 – Convertidor simple (millas ↔ kilómetros)

**Descripción:** Programa que convierte distancias entre millas y kilómetros usando la equivalencia `1 milla ≈ 1.61 km`.

**Lógica utilizada:**
1. Se definen variables `miles` y `kilometers`.
2. Se realizan las conversiones multiplicando o dividiendo por `1.61`.
3. Se usa `round()` para limitar los resultados a 2 decimales.

**Ejemplo de salida:**
```
7.38 millas son 11.88 kilómetros
12.25 kilómetros son 7.61 millas
```

---

### LAB 7 – Operadores y expresiones

**Descripción:** Programa que evalúa la expresión algebraica `3x³ - 2x² + 3x - 1`.

**Lógica utilizada:**
1. Se define la variable `x` como `float`.
2. Se traduce la expresión matemática a Python usando `**` y `*`.
3. Se calcula `y` y se imprime el resultado.

**Resultados según valor de `x`:**

| `x`  | `y`    |
|:----:|:------:|
| `0`  | `-1.0` |
| `1`  | `3.0`  |
| `-1` | `-9.0` |

---

### LAB 8 – Ejercicios de Algoritmos

**Descripción:** Múltiples algoritmos enfocados en resolver problemas básicos dentro del contexto de un videojuego, aplicando variables, operadores y expresiones.

**Estructura común de cada ejercicio:**

1. **Entrada:** Se solicitan valores al usuario con `input()`.
2. **Procesamiento:** Se realizan operaciones matemáticas.
3. **Salida:** Se muestra el resultado con `print()`.

**Conceptos aplicados:**

- Variables (`int`, `float`)
- Operadores matemáticos (`+`, `-`, `*`, `/`, `//`, `%`)
- Conversión de tipos (`int()`, `float()`)
- Entrada de datos (`input()`)
- Cálculo de porcentajes y promedios

**Ejemplos de resultados:**

| Ejercicio         | Descripción                              |
|-------------------|------------------------------------------|
| Puntaje total     | Suma de puntajes por nivel               |
| Tiempo total      | Conversión de minutos a segundos         |
| Vida restante     | Cálculo porcentual de HP                 |
| Velocidad promedio| Distancia dividida entre tiempo          |
| Tiempo formateado | Horas y minutos con `//` y `%`           |

---