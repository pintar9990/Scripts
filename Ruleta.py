import math

final = 1

print("Con este Script puedes calcular las diferentes opciones que se muestran a continuación dando\n"
      "por hecho que estamos haciendo Martingala en la ruleta europea y estamos apostando siempre \n"
      "a cualquiera de estas opciones: Rojo/Negro, Par/Impar, 1-18/19-36\n")

while final == 1:
    print("\nPresiona \"1\" si quieres calcular la cantidad de dinero que te gastarás indicando la\n"
          "apuesta inicial y las rondas perdidas\n")
    print("Presiona \"2\" si quieres calcular cuantas hasta cuantas rondas seguidas podrías perder\n"
          "indicando la apuesta inicial y el dinero total\n")
    print("Presiona \"3\" si quieres calcular la apuesta inicial indicando el dinero total\n"
          "y el número máximo de rondas a perder\n")
    print("Presiona \"4\" si quieres calcular la probabilidad que existe de perder x rondas seguidas\n")
    print("Presiona \"5\" si quieres calcular las rondas que podrías hacer indicando una cantidad x de\n"
          "probabilidades de perder\n")

    terminar = 1

    while terminar == 1:

        while True:
            try:
                x = Hacer = int(input())
                break
            except ValueError:
                print("\nEso no era un número entero, inténtalo de nuevo\n")

        if Hacer == 1:
            print("\nUtiliza puntos en vez de comas para especificar con decimales\n")

            while True:
                try:
                    Inicio = float(input("Introduce Cantidad Inicial : "))
                    break
                except ValueError:
                    print("\nCantidad no reconocida, no olvide utilizar puntos en vez de comas si utiliza decimales\n")

            while True:
                try:
                    Rondas = int(input("Introduce Rondas : "))
                    break
                except ValueError:
                    print("\nCantidad no reconocida, recuerde que las rondas debe ser un número entero\n")

            Acumulado = Inicio
            Suma = 0

            for x in range(Rondas):
                Suma += Acumulado
                Acumulado = Acumulado * 2

            x = Suma
            x = x * 100
            x = int(x)
            x = (str(x))
            if (x[-2:]) == "00":
                print(f"\nTe gastarás {int(Suma)}€ después de {Rondas} rondas")
            else:
                Suma = Suma * 100
                Suma = math.ceil(Suma)
                Suma = Suma / 100
                print(f"\nTe gastarás {Suma:.2f}€ después de {Rondas} rondas")

        elif Hacer == 2:

            print("\nUtiliza puntos en vez de comas para especificar con decimales\n")
            while True:
                try:
                    Inicio1 = float(input("Introduce Cantidad Inicial : "))
                    break
                except ValueError:
                    print("\nCantidad no reconocida, no olvide utilizar puntos en vez de comas si utiliza decimales\n")

            Inicio = int(Inicio1 * 100)
            Acumulado = Inicio

            while True:
                try:
                    Dinero1 = float(input("Introduce Dinero Total : "))
                    break
                except ValueError:
                    print("\nCantidad no reconocida, no olvide utilizar puntos en vez de comas si utiliza decimales\n")

            Dinero = int(Dinero1 * 100)

            R = 0
            DineroRestante = Dinero
            while True:
                DineroRestante = DineroRestante - Acumulado
                Acumulado = Acumulado * 2
                R += 1
                if DineroRestante < 0:
                    break
            R = R - 1
            print("\nPuedes hacer", R, "rondas")

            Suma = 0
            for x in range(R):
                Suma += Inicio1
                Inicio1 = Inicio1 * 2

            x = Suma
            x = x * 100
            x = int(x)
            x = (str(x))
            y = Dinero1 - Suma
            y = y * 100
            y = int(y)
            y = (str(y))
            if (x[-2:]) == "00" and (y[-2:]) == "00":
                print(
                    f"Te gastarás un total de {int(Suma)}€ después de {R} rondas y te sobrarán {int(Dinero1 - Suma)}€")
            elif (x[-2:]) == "00":
                print(
                    f"Te gastarás un total de {int(Suma)}€ después de {R} rondas y te sobrarán {(Dinero1 - Suma):.2f}€")
            elif (y[-2:]) == "00":
                Suma = Suma * 100
                Suma = math.ceil(Suma)
                Suma = Suma / 100
                print(f"Te gastarás un total de {Suma:.2f}€ después de {R} rondas y te sobrarán {int(Dinero1 - Suma)}€")
            else:
                Suma = Suma * 100
                Suma = math.ceil(Suma)
                Suma = Suma / 100
                Dinero1 = Dinero1 - Suma
                print(f"Te gastarás {Suma:.2f}€ después de {R} rondas y te sobrarán {Dinero1:.2f}€")

        elif Hacer == 3:
            print("\nUtiliza puntos en vez de comas para especificar con decimales\n")
            while True:
                try:
                    Dinero = float(input("Introduce Dinero Total : "))
                    break
                except ValueError:
                    print("\nCantidad no reconocida, no olvide utilizar puntos en vez de comas si utiliza decimales\n")

            while True:
                try:
                    Rondas = int(input("Introduce Rondas : "))
                    break
                except ValueError:
                    print("\nCantidad no reconocida, recuerde que las rondas debe ser un número entero\n")

            while True:
                try:
                    o = int(input(
                        "\nIntroduce \"1\" si tu ruleta admite cantidades inferiores a 10 céntimos,\n"
                        "de lo contrario introduce \"0\" : "))
                    assert o == 1 or o == 0
                    break
                except ValueError:
                    print("\nCantidad no reconocida recuerde que solo puede introducir o \"0\" o \"1\"")
                except AssertionError:
                    print("\nSolo se admite el valor \"0\" ó \"1\"")

            Multiplicador = 1
            Tempo = 1
            for x in range(Rondas - 1):
                Tempo = Tempo * 2
                Multiplicador = Multiplicador + Tempo

            Inicial = Dinero / Multiplicador

            x = Inicial
            x = x * 100
            x = int(x)
            x = (str(x))
            if o == 1:
                if (x[-2:]) == "00":
                    print(f"\nTendrás que poner {int(Inicial)}€ inicialmente para poder hacer {Rondas} rondas")
                else:
                    Inicial = Inicial * 100
                    Inicial = math.floor(Inicial)
                    Inicial = Inicial / 100
                    print(f"\nTendrás que poner {Inicial:.2f}€ inicialmente para poder hacer {Rondas} rondas")

                Acumulado = int(Inicial * 100)
                Suma = 0

                for x in range(Rondas):
                    Suma += Acumulado
                    Acumulado = Acumulado * 2

                if (Dinero - Suma / 100) != 0:
                    print(
                        f"\nYa que los céntimos solo se pueden dividir en unidades de hasta 2 decimales y estamos\n"
                        f"multiplicando por 2, el resultado obtenido anteriormente sería la cantidad más alta que\n"
                        f"podremos apostar para llegar a las {Rondas} rondas, ya que si apostamos 1 céntimo más al\n"
                        f"principio, se nos pasará de nuestra cantidad de dinero máxima\n")

                    print(
                        f"Si pones esa cantidad inicial y pierdes las {Rondas} rondas\n"
                        f"seguidas te habrás gastado {Suma / 100:.2f}€, quedarás con {Dinero - (Suma / 100):.2f}€")

            elif o == 0:
                if (x[-2:]) == "00":
                    print(f"\nTendrás que poner {int(Inicial)}€ inicialmente para poder hacer {Rondas} rondas")
                else:
                    Inicial = Inicial * 10
                    Inicial = math.floor(Inicial)
                    Inicial = Inicial / 10
                    print(f"\nTendrás que poner {Inicial:.2f}€ inicialmente para poder hacer {Rondas} rondas")

                Acumulado = int(Inicial * 10)
                Suma = 0

                for x in range(Rondas):
                    Suma += Acumulado
                    Acumulado = Acumulado * 2

                if (Dinero - Suma / 10) != 0:
                    print(
                        f"\nYa que los céntimos solo se pueden dividir en unidades de hasta 2 decimales y estamos\n"
                        f"multiplicando por 2, el resultado obtenido anteriormente sería la cantidad más alta que\n"
                        f"podremos apostar para llegar a las {Rondas} rondas, ya que si apostamos 10 céntimos más al\n"
                        f"principio, se nos pasará de nuestra cantidad de dinero máxima\n")

                    print(
                        f"Si pones esa cantidad inicial y pierdes las {Rondas} rondas\n"
                        f"seguidas te habrás gastado {Suma / 10:.2f}€, quedarás con {Dinero - (Suma / 10):.2f}€")

        elif Hacer == 4:

            while True:
                try:
                    Intentos = int(input("\nIntroduce Rondas: "))
                    break
                except ValueError:
                    print("\nCantidad no reconocida, recuerde que las rondas debe ser un número entero")

            Probabilidad = (1 - ((19 ** Intentos) / (37 ** Intentos))) * 100
            Probabilidad = Probabilidad * 10000
            Probabilidad = math.floor(Probabilidad)
            Probabilidad = Probabilidad / 10000

            print(f"\nLa probabilidad de perder en todas las rondas es del {100 - Probabilidad:.4f}%")
            print(f"O lo que es lo mismo, la probabilidad de que en {Intentos} rondas\n"
                  f"ganes al menos 1 de las rondas es del {Probabilidad}%")

        elif Hacer == 5:
            print("\nUtiliza puntos en vez de comas para especificar con decimales")
            while True:
                try:
                    Pr = float(input("\nIntroduce Probabilidad de Perder: "))
                    break
                except ValueError:
                    print("\nCantidad no reconocida, no olvide utilizar puntos en vez de comas si utiliza decimales")
            Pr = 100 - Pr
            Puro = (math.log((100 - Pr) / 100) / math.log(19 / 37))
            Intentos = math.ceil(math.log((100 - Pr) / 100) / math.log(19 / 37))

            print(f"\nRondas que tendrías que realizar para tener esa probabilidad de perder {Puro:.4f}")
            print("Tendrías que hacer entonces", Intentos, "rondas ya que no puedes hacer rondas con parte decimal")

            Probabilidad = (1 - ((19 ** Intentos) / (37 ** Intentos))) * 100
            Probabilidad = Probabilidad * 10000
            Probabilidad = math.floor(Probabilidad)
            Probabilidad = Probabilidad / 10000

            print(f"\nLa probabilidad de perder en todas las rondas es del {100 - Probabilidad:.4f}%\n")
            print(f"O lo que es lo mismo, la probabilidad de que en {Intentos} rondas\n"
                  f"ganes al menos 1 de las rondas es del {Probabilidad}%")

        else:
            print("\nNúmero no válido, introduzca un número del 1 al 5\n")
            continue
        terminar = 0

    final = 2
    print("\n")
    while final == 2:

        final = input("¿Desea salir? presiones \"s\" para salir o \"n\" para volver a ejecutar\n")

        if final == "S" or final == "s":
            final = 0
        elif final == "n" or final == "N":
            final = 1
        else:
            print("\nCaracter no reconocido, vuelva a intentarlo\n")
            final = 2
