
import math

while True:
    dist = int(input("Distância: "))
    print(str(dist) + " kms")

    tempo = int(input("Tempo em mins: "))
    viagens = math.ceil(1080 / (tempo * 0.9))
    print(str(tempo) + "mins = " + str(viagens) + " viagens\dia")

    large = int(input("Demand Large Load: "))
    largeviag = math.floor(large / viagens)
    print("large: " + str(large) + " cargo/dia | " + str(largeviag) + " cargo/viagem")

    heavy = int(input("Demand Heavy Load: "))
    heavyviag =  math.floor(heavy / viagens)
    print("heavy: " + str(heavy) + " cargo/dia | " + str(heavyviag) + " cargo/viagem")

    ratio = 81600/57120
    maxcargo = math.ceil(largeviag + (heavyviag/ratio))

    print("\n")

    print(
        "Configuração ideal: "
        + str(maxcargo)
        + "cargo -> "
        + str(largeviag)
        + "large "
        + str(heavyviag)
        + "heavy"
    )
    print("-------")
    