# 1. Puntaje total de un jugador
nivel1 = int(input("Puntos nivel 1: "))
nivel2 = int(input("Puntos nivel 2: "))
nivel3 = int(input("Puntos nivel 3: "))
puntaje_total = nivel1 + nivel2 + nivel3
print("Puntaje total:", puntaje_total)

# 2. Tiempo total en segundos
horas = int(input("Horas jugadas: "))
minutos = int(input("Minutos jugados: "))
segundos = int(input("Segundos jugados: "))
tiempo_total = horas * 3600 + minutos * 60 + segundos
print("Tiempo total en segundos:", tiempo_total)

# 3. Daño total
ataque1 = float(input("Daño ataque 1: "))
ataque2 = float(input("Daño ataque 2: "))
ataque3 = float(input("Daño ataque 3: "))
danio_total = ataque1 + ataque2 + ataque3
print("Daño total:", danio_total)

# 4. Experiencia total
exp1 = int(input("Experiencia misión 1: "))
exp2 = int(input("Experiencia misión 2: "))
exp3 = int(input("Experiencia misión 3: "))
exp_total = exp1 + exp2 + exp3
print("Experiencia total:", exp_total)

# 5. Porcentaje de vida restante
vida_max = float(input("Vida máxima: "))
vida_actual = float(input("Vida actual: "))
porcentaje_vida = (vida_actual / vida_max) * 100
print("Porcentaje de vida:", porcentaje_vida, "%")

# 6. Oro total
oro1 = int(input("Oro misión 1: "))
oro2 = int(input("Oro misión 2: "))
oro3 = int(input("Oro misión 3: "))
oro_total = oro1 + oro2 + oro3
print("Oro total:", oro_total)

# 7. Velocidad promedio
distancia = float(input("Distancia recorrida: "))
tiempo = float(input("Tiempo tomado: "))
velocidad = distancia / tiempo
print("Velocidad promedio:", velocidad)

# 8. Costo total de mejoras
mejora1 = float(input("Costo mejora 1: "))
mejora2 = float(input("Costo mejora 2: "))
mejora3 = float(input("Costo mejora 3: "))
costo_total = mejora1 + mejora2 + mejora3
print("Costo total mejoras:", costo_total)

# 9. Tiempo restante
tiempo_total_mision = float(input("Tiempo total misión: "))
tiempo_transcurrido = float(input("Tiempo transcurrido: "))
tiempo_restante = tiempo_total_mision - tiempo_transcurrido
print("Tiempo restante:", tiempo_restante)

# 10. Nivel promedio
nivel1 = int(input("Nivel jugador 1: "))
nivel2 = int(input("Nivel jugador 2: "))
nivel3 = int(input("Nivel jugador 3: "))
promedio = (nivel1 + nivel2 + nivel3) / 3
print("Nivel promedio:", promedio)

# 11. Daño crítico
danio_base = float(input("Daño base: "))
multiplicador = float(input("Multiplicador crítico: "))
danio_critico = danio_base * multiplicador
print("Daño crítico:", danio_critico)

# 12. Tiempo en horas y minutos
min_total = int(input("Tiempo total en minutos: "))
horas = min_total // 60
min_restantes = min_total % 60
print("Tiempo:", horas, "horas y", min_restantes, "minutos")

# 13. Porcentaje misiones completadas
misiones_total = int(input("Total misiones: "))
misiones_completadas = int(input("Misiones completadas: "))
porcentaje = (misiones_completadas / misiones_total) * 100
print("Porcentaje completado:", porcentaje, "%")

# 14. Costo total objetos
obj1 = float(input("Costo objeto 1: "))
obj2 = float(input("Costo objeto 2: "))
obj3 = float(input("Costo objeto 3: "))
total_objetos = obj1 + obj2 + obj3
print("Costo total objetos:", total_objetos)

# 15. Tiempo promedio de partidas
partida1 = float(input("Tiempo partida 1: "))
partida2 = float(input("Tiempo partida 2: "))
partida3 = float(input("Tiempo partida 3: "))
promedio_partidas = (partida1 + partida2 + partida3) / 3
print("Tiempo promedio:", promedio_partidas)

# 16. Porcentaje enemigos derrotados
enemigos_total = int(input("Total enemigos: "))
enemigos_derrotados = int(input("Enemigos derrotados: "))
porcentaje_enemigos = (enemigos_derrotados / enemigos_total) * 100
print("Porcentaje derrotados:", porcentaje_enemigos, "%")