# LAB: Dando formato a la salida

# En este ejercicio se trabajó con la función print()
# para mejorar el formato de salida usando \n y operaciones con cadenas

# Flecha original usando un solo print y saltos de línea (\n)
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

print()  # Espacio entre figuras

# Flecha duplicada (una al lado de la otra)
# Se usa concatenación de cadenas
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