from NumPlayersException import NumPlayersException


class Alineacion:


    def crearAlineacion():
        alineacion = []
        portero = input("Introduzca un portero:\n")
        alineacion.append(portero)
        numDefensas = input("Introduzca número de defensas:\n")
        numDefensas = int (numDefensas)
        i = 0
        while i < numDefensas:
            defensa = input("Introduzca un defensa:\n")
            alineacion.append(defensa)
            i+=1
        numCentros = input("Introduzca un número de mediocentros:\n")
        numCentros = int(numCentros)
        i = 0
        while i < numCentros:
            centro = input("Introduzca un mediocentro:\n")
            alineacion.append(centro)
            i += 1
        numDelanteros = input("Introduzca un número de delanteros:\n")
        numDelanteros = int(numDelanteros)
        i = 0
        while i < numDelanteros:
            delantero = input("Introduzca un delantero:\n")
            alineacion.append(delantero)
            i += 1
        if len(alineacion) != 11:
            print("La alineación debe tener 11 jugadores")
            raise NumPlayersException()
        else:
            return alineacion