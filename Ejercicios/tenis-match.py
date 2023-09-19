def contador_puntos(tabla_puntos):
    puntuacion = {'Love': 0, '15': 15, '30': 30, '40': 40}
    puntuacion1 = 0
    puntuacion2 = 0

    for puntos in tabla_puntos:
        if puntos == 'P1':
            puntuacion1 += 1
        elif puntos == 'P2':
            puntuacion2 += 1

        if puntuacion1 >= 3 and puntuacion2 >= 3:
            if puntuacion1 == puntuacion2:
                estado_juego = "Deuce"
            elif puntuacion1 > puntuacion2:
                estado_juego = "Ventaja P1"
            else:
                estado_juego = "Ventaja P2"
        else:
            estado_juego = f'{list(puntuacion.keys())[puntuacion1]} - {list(puntuacion.keys())[puntuacion2]}' if puntuacion1 <= 3 and puntuacion2 <= 3 else ""

        print(estado_juego)

        if "Ventaja" in estado_juego:
            ganador = "P1" if "P1" in estado_juego else "P2"
            print(f"Ha ganado el {ganador}")
            break

tabla_puntos = ['P2', 'P2', 'P2', 'P1', 'P1', 'P1', 'P2', 'P1']
contador_puntos(tabla_puntos)
