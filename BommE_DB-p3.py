import random
import yaml  # Importar la librería para manejar archivos YAML

# Cargar el mapa desde el archivo YAML
with open('Mapa.yaml', 'r') as file:
    data = yaml.safe_load(file)
    Mapa = data['Mapa']

# Verificar dimensiones del mapa
print(f"Tamaño del mapa cargado: {len(Mapa)} filas x {len(Mapa[0])} columnas")
for fila in Mapa:
    print(fila)

# Coordenadas iniciales y finales del robot
inicio = (0, 9)  # j:1 (fila 0, columna 9)
fin = (4, 0)     # a:5 (fila 4, columna 0)

# Asegurarse de que las coordenadas están dentro de los límites del mapa
if not (0 <= inicio[0] < len(Mapa) and 0 <= inicio[1] < len(Mapa[0])):
    raise ValueError(f"La coordenada inicial {inicio} está fuera de los límites del mapa.")
if not (0 <= fin[0] < len(Mapa) and 0 <= fin[1] < len(Mapa[0])):
    raise ValueError(f"La coordenada final {fin} está fuera de los límites del mapa.")

# Función para convertir coordenadas numéricas a formato de letras (filas j a a) y números (columnas 1 a 10)
def coordenadas_cartesianas(x, y):
    letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
    return f"({letras[y]}:{x + 1})"  # Las filas son letras, las columnas son números

# Función para imprimir el mapa con el rastro del robot
def imprimir_mapa(mapa):
    print("-------------------")
    for fila in mapa:
        print(" ".join(fila))  # Imprimir cada fila uniendo sus elementos separados por un espacio
    print("-------------------\n")

# Detector de bombas con falsos positivos y falsos negativos
def detector(valor):
    Vacias10 = [0, 0, 0, 0, 0, 0, 0, 0, 1, 1]
    Bombas10 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 0]
    FN = random.choice(Vacias10)
    FP = random.choice(Bombas10)
    if valor == 1:
        return FP
    else:
        return FN

# Movimiento del robot con detección de bombas en forma de "S"
def movimiento_robot_con_bayes(mapa, inicio, fin):
    x, y = inicio
    contador = 0
    IntB = 3
    Bomba = 1
    probabilidad_final = 0  # Variable para almacenar la última probabilidad
    
    # Marcar la posición inicial del robot
    mapa[x][y] = 'R'
    
    print(f"Coordenada inicial: {coordenadas_cartesianas(x, y)}")
    imprimir_mapa(mapa)

    while (x, y) != fin:
        input("Presiona Enter para avanzar.... \n")

        # Eliminar la "R" de la posición anterior
        mapa[x][y] = '_' 

        # Movimiento en forma de "S"
        if x % 2 == 0:  # Si estamos en una fila par (según índice), mover hacia la izquierda
            if y > 0:
                y -= 1
            else:
                x += 1  # Bajar a la siguiente fila
        else:  # Si estamos en una fila impar, mover hacia la derecha
            if y < len(mapa[0]) - 1:
                y += 1
            else:
                x += 1  # Bajar a la siguiente fila

        # Verificar que las nuevas coordenadas estén dentro de los límites
        if not (0 <= x < len(mapa) and 0 <= y < len(mapa[0])):
            print(f"Error: Coordenadas fuera del límite en {coordenadas_cartesianas(x, y)}")
            break

        # Marcar la nueva posición del robot
        mapa[x][y] = 'R'
        print(f"Coordenada actual: {coordenadas_cartesianas(x, y)}")
        imprimir_mapa(mapa)

        # Proceso de detección de bomba
        valor = 1
        resultado_det = detector(valor)
        contador += 1

        if resultado_det == 1:
            # Probabilidad de detectar bomba
            PBomba = 1 / (50 - contador) if contador < 50 else 0
            ProbBomPos = 9 / 10
            PNoBomba = 1 - PBomba
            PNoBombaPos = 2 / 10

            # Cálculo de la probabilidad de Bayes
            bayes = (PBomba * ProbBomPos) / ((PBomba * ProbBomPos) + (PNoBomba * PNoBombaPos))
            probabilidad_final = bayes  # Guardar la probabilidad final
            print(f"La probabilidad de bayes es: {bayes}")

            if bayes > 0.73: IntB -= 1

            # Toma de segunda probabilidad
            valor2 = detector(valor)
            if valor2 == 1:
                bayes2 = (bayes * ProbBomPos) / ((bayes * ProbBomPos) + (PNoBomba * PNoBombaPos))
                probabilidad_final = bayes2  # Actualizar la probabilidad final
                print(f"2da probabilidad de bayes es: {bayes2}")

                if bayes2 > 0.73: IntB -= 1

                # Toma de tercera probabilidad
                valor3 = detector(valor)
                if valor3 == 1:
                    bayes3 = (bayes2 * ProbBomPos) / ((bayes2 * ProbBomPos) + (PNoBomba * PNoBombaPos))
                    probabilidad_final = bayes3  # Actualizar la probabilidad final
                    print(f"3ra probabilidad de bayes es: {bayes3}")

                    if bayes3 > 0.73:
                        IntB -= 1
                        Bomba -= 1
                        print("-----------------------------------------------------------")
                        print(f"La bomba fue desactivada con éxito, quedan: {Bomba} bombas")
                        print("-----------------------------------------------------------")

                    if Bomba == 0:
                        print(f"La bomba estaba en la coordenada {coordenadas_cartesianas(x, y)}, probabilidad de: {bayes3:.2f}")
                        print("-----------------------------------------------------------")
                        break

                    if IntB == 0:
                        print(f"La bomba estaba en la coordenada {coordenadas_cartesianas(x, y)}, me morí :c")
                        print("-----------------------------------------------------------")
                        break

        else:
            print("Camino libre, no se detectaron bombas")

        if IntB == 0 or Bomba == 0:
            break

    return probabilidad_final  # Retornar la última probabilidad usada

# Menú interactivo para el usuario
def menu_interactivo(probabilidad_final):
    print("---------------------------------------------------")
    print("Bienvenido al Simulador de Movimiento del Robot 'R'")
    print("---------------------------------------------------")
    print(f"Probabilidad de bomba: {probabilidad_final:.2f}")

# Ejecutar el menú y movimiento del robot
probabilidad_final = 0  # Inicializar variable de probabilidad
menu_interactivo(probabilidad_final)
probabilidad_final = movimiento_robot_con_bayes(Mapa, inicio, fin)