import decimal
import math

final = 1

print("\nEste Script calcula probabilidades al intentar algo varias veces")

while final == 1:
    print("\nPresiona \"1\" si quieres calcular la probabilidad total que tienes de que algo ocurra al intentar eso\n"
          "un número determinado de veces conociendo la probabilidad individual de que ocurra")

    print("\nPresiona \"2\" si quieres calcular los intentos que tendrías que realizar para que la probabilidad\n"
          "global de que salga en al menos uno de los intentos sea la especificada, indicando entonces\n"
          "la probabilidad global que queremos tener y la probabilidad individual en cada intento\n")

    terminar = 1

    while terminar == 1:

        while True:
            try:
                Hacer = int(input())
                if (Hacer != 1 and Hacer !=2):
                    print("\nRecuerde que solo puede introducir \"1\" o \"2\", vuelva a intentarlo\n")
                    continue
                break
            except ValueError:
                print("\nEso no era un número entero, inténtalo de nuevo\n")

        if Hacer == 1:

            while True:
                try:
                    Intentos = int(input("Introduce número de veces a intentar algo : "))
                    if Intentos == 0:
                        print("\nNo tiene sentido que no haya intentos, vuelva a intentarlo\n")
                        continue
                    if Intentos < 0:
                        print("\nNo puede haber intentos negativos\n")
                        continue
                    break
                except ValueError:
                    print("\nCantidad no reconocida, recuerde que tiene que ser un número entero\n")

            while True:
                try:
                    Pr = float(input("\nIntroduce Probabilidad de que ocurra: "))
                    if Pr <= 0:
                        print("\nNo puede haber una probabilidad menor o igual que 0")
                        continue

                    if Pr >= 100:
                        print("\nLa probabilidad no puede ser mayor al 100%")
                        continue
                    break
                except ValueError:
                    print("\nCantidad no reconocida, no olvide utilizar puntos en vez de comas si utiliza decimales")

            Probabilidad = (decimal.Decimal(1) - (((decimal.Decimal(100 - Pr)) ** decimal.Decimal(Intentos)) / (decimal.Decimal(100) ** decimal.Decimal(Intentos)))) * decimal.Decimal(100)
            Probabilidad = Probabilidad * 10000
            Probabilidad = math.floor(Probabilidad)
            Probabilidad = Probabilidad / 10000

            print(f"\nLa probabilidad de que en {Intentos} intentos te salga en al menos 1 es del {Probabilidad}%")

            print(f"\nLa probabilidad de en ninguno de los intentos te salga del {100 - Probabilidad:.4f}%")

        if Hacer == 2:
            Retry = 3
            while Retry == 3:
                print("\nUtiliza puntos en vez de comas para especificar con decimales")
                while True:
                    try:
                        Pr = float(input("\nIntroduce Probabilidad individual de que ocurra en cada intento: "))
                        if Pr <= 0:
                            print("\nNo puede haber una probabilidad menor o igual que 0")
                            continue

                        if Pr >= 100:
                            print("\nLa probabilidad no puede ser mayor al 100%")
                            continue
                        break
                    except ValueError:
                        print("\nCantidad no reconocida, no olvide utilizar puntos en vez de comas si utiliza decimales")

                while True:
                    try:
                        Probabilidad = float(input("\nIntroduce Probabilidad total que quieres tener: "))
                        if Pr <= 0:
                            print("\nNo puede haber una probabilidad menor o igual que 0")
                            continue

                        if Probabilidad >= 100:
                            print("\nLa probabilidad no puede ser mayor al 100%")
                            continue

                        if Probabilidad <= Pr:
                            print("\nHas introducido una probabilidad total menor que la probabilidad individual,\n"
                                  "esto no tiene sentido ya necesitarías menos de un intento para alcanzarla.")
                            print("\n¿Desea continuar de todos modos?\n")
                            Retry = 2
                            while Retry == 2:
                                Retry = input("Presione \"c\" para continuar, \"t\" para introducir otra probabilidad total o \"p\" \n"
                                              "para introducir otra probabilidad individual de que ocurra en cada intento\n")

                                if Retry == "c" or Retry == "C":
                                    Retry = 0
                                elif Retry == "t" or Retry == "T":
                                    Retry = 1
                                elif Retry == "p" or Retry == "P":
                                    Retry = 3
                                else:
                                    print("\nCaracter no reconocido, vuelva a intentarlo\n")
                            if (Retry == 1):
                                continue
                        else:
                            Retry = 2
                        break
                    except ValueError:
                        print("\nCantidad no reconocida, no olvide utilizar puntos en vez de comas si utiliza decimales")



            Puro = math.log((100-Probabilidad) / 100) / math.log((100 - Pr) / 100)
            Intentos = math.ceil(math.log((100 - Probabilidad) / 100) / math.log((100 - Pr) / 100))

            print(f"\nIntentos que tendrías que realizar para tener esa probabilidad de que salga en al menos uno de ellos {Puro:.4f}")

            print("\nTendrías que hacer entonces", Intentos, "intentos ya que no puedes hacer intentos con parte decimal")

            Probabilidad = (decimal.Decimal(1) - (((decimal.Decimal(100 - Pr)) ** decimal.Decimal(Intentos)) / (decimal.Decimal(100) ** decimal.Decimal(Intentos)))) * decimal.Decimal(100)
            Probabilidad = Probabilidad * 10000
            Probabilidad = math.floor(Probabilidad)
            Probabilidad = Probabilidad / 10000

            print(f"\nLa probabilidad de que en {Intentos} intentos te salga en al menos 1 es del {Probabilidad}%")

            print(f"\nLa probabilidad de en ninguno de los intentos te salga del {100 - Probabilidad:.4f}%")

        terminar = 0

    final = 2
    print("\n")
    while final == 2:

        final = input("¿Desea salir? presione \"s\" para salir o \"n\" para volver a ejecutar\n")

        if final == "S" or final == "s":
            final = 0
        elif final == "n" or final == "N":
            final = 1
        else:
            print("\nCaracter no reconocido, vuelva a intentarlo\n")
            final = 2
