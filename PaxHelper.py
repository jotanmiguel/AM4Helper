
import math

while True:
    dist = int(input("Distância: "))
    print(str(dist) + " kms")

    tempo = int(input("Tempo em mins: "))
    viagens = math.ceil(1080 / (tempo * 0.9))
    print(str(tempo) + "mins = " + str(viagens) + " viagens\dia")

    y = int(input
    ("Demand Passageiros Classe Eco: "))
    yviag = math.floor(y / viagens)
    print("y: " + str(y) + " pax/dia | " + str(yviag) + " pax/viagem")

    j = int(input("Demand Passageiros Classe Bus: "))
    jviag = math.floor(j / viagens)
    print("j: " + str(j) + " pax/dia | " + str(jviag) + " pax/viagem")

    f = int(input("Demand Passageiros Classe First: "))
    fviag = math.floor(f / viagens)
    print("f: " + str(f) + " pax/dia | " + str(fviag) + " pax/viagem")

    maxpax = yviag + (2 * jviag) + (3 * fviag)

    print("\n")

    print(
        "Configuração ideal: "
        + str(maxpax)
        + "pax -> "
        + str(yviag)
        + "y "
        + str(jviag)
        + "j "
        + str(fviag)
        + "f "
    )

    print("\n")

    profit = (
        (0.4 * dist + 170) * yviag
        + (0.8 * dist + 560) * jviag
        + (1.2 * dist + 1200) * fviag
    )
    print("Profit/viagem(100% procura): " + str(profit) + "$")
    print("Profit/Dia(100% procura): " + str(float(profit * viagens)) + "$")

    print("----------------------------")