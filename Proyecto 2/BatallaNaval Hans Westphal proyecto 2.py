# Clase Barco
class Barco:
    def __init__(self, nombre, tamano):
        self.nombre = nombre
        self.tamano = tamano
        self.vida = tamano

    def recibir_disparo(self):
        self.vida -= 1

    def esta_destruido(self):
        return self.vida == 0

# Clase Tablero
class Tablero:
    def __init__(self, nombre):
        self.nombre = nombre
        self.tablero = [[' ' for _ in range(10)] for _ in range(10)]
        self.barcos = []

    def imprimir_tablero(self, mostrar_barcos=False):
        print("Tablero de", self.nombre)
        columnas = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
        print("   " + " ".join(columnas))
        for i, fila in enumerate(self.tablero):
            print(i, " |" + "|".join(fila) + "|")
        print()

    def agregar_barco(self, barco, fila, columna, orientacion):
        if orientacion == 'h':
            for i in range(barco.tamano):
                self.tablero[fila][columna + i] = 'O'
        else:
            for i in range(barco.tamano):
                self.tablero[fila + i][columna] = 'O'
        self.barcos.append(barco)

# Función para realizar un disparo
def realizar_disparo(tablero, fila, columna):
    if tablero.tablero[fila][columna] == 'O':
        print("¡Impacto!")
        for barco in tablero.barcos:
            if tablero.tablero[fila][columna] == 'O':
                barco.recibir_disparo()
                tablero.tablero[fila][columna] = 'X'
                if barco.esta_destruido():
                    print("¡Hundiste el", barco.nombre, "!")
                    tablero.barcos.remove(barco)
        return True
    else:
        print("Agua.")
        tablero.tablero[fila][columna] = 'M'
        return False

# Función para el turno de un jugador
def turno_jugador(jugador, oponente):
    print(jugador.nombre, ", es tu turno.")
    oponente.imprimir_tablero()
    while True:
        try:
            fila = int(input("Elige una fila (0-9): "))
            columna = input("Elige una columna (A-J): ").upper()
            if 0 <= fila < 10 and 'A' <= columna <= 'J':
                columna = ord(columna) - ord('A')
                break
            else:
                print("Coordenadas fuera de rango. Intenta de nuevo.")
        except ValueError:
            print("Entrada no válida. Ingresa números y letras válidos (0-9, A-J).")
    
    resultado_disparo = realizar_disparo(oponente, fila, columna)
    if resultado_disparo and not oponente.barcos:
        print(jugador.nombre, "ha ganado el juego!")

# Crear tableros para jugadores
jugador1_tablero = Tablero("Jugador 1")
jugador2_tablero = Tablero("Jugador 2")

# Iniciar el juego
print("Jugador 1, coloca tus barcos:")
for i in range(4):
    while True:
        try:
            fila = int(input("Elige una fila (0-9) para el barco {}: ".format(i + 1)))
            columna = input("Elige una columna (A-J) para el barco {}: ".format(i + 1)).upper()
            orientacion = input("Elige la orientación (h para horizontal, v para vertical) para el barco {}: ".format(i + 1))
            columna = ord(columna) - ord('A')
            if 0 <= fila < 10 and 0 <= columna < 10 and (orientacion == 'h' or orientacion == 'v'):
                break
            else:
                print("Coordenadas u orientación incorrectas. Intenta de nuevo.")
        except ValueError:
            print("Entrada no válida. Ingresa números y letras válidos (0-9, A-J).")
    jugador1_tablero.agregar_barco(Barco("Barco " + str(i + 1), 1), fila, columna, orientacion)

print("Jugador 2, coloca tus barcos:")
for i in range(4):
    while True:
        try:
            fila = int(input("Elige una fila (0-9) para el barco {}: ".format(i + 1)))
            columna = input("Elige una columna (A-J) para el barco {}: ".format(i + 1)).upper()
            orientacion = input("Elige la orientación (h para horizontal, v para vertical) para el barco {}: ".format(i + 1))
            columna = ord(columna) - ord('A')
            if 0 <= fila < 10 and 0 <= columna < 10 and (orientacion == 'h' or orientacion == 'v'):
                break
            else:
                print("Coordenadas u orientación incorrectas. Intenta de nuevo.")
        except ValueError:
            print("Entrada no válida. Ingresa números y letras válidos (0-9, A-J).")

    jugador2_tablero.agregar_barco(Barco("Barco " + str(i + 1), 1), fila, columna, orientacion)
# Iniciar el juego
while True:
    turno_jugador(jugador1_tablero, jugador2_tablero)
    if not jugador2_tablero.barcos:
        break

    turno_jugador(jugador2_tablero, jugador1_tablero)  # Agregar este turno
    if not jugador1_tablero.barcos:
        break


# Mostrar los tableros con barcos después de que termina el juego
jugador1_tablero.imprimir_tablero(True)
jugador2_tablero.imprimir_tablero(True)
