class Airport:
    """
    This class represents an unique Airport in the game.
    """

    def __init__(
        self, icao: str, name: str, city: str, county: str, lat: float, long: float
    ):
        """
        This is the Airport constructor, where the necessary data is inicialized.

        Args:
            iata (str): ICAO code for this Airport.
            name (str): Name of this Airport.
            city (str): City where this Airport is located.
            county (str): Country where this Airport is located.
            lat (float): Latitude coordinate of the Airport location.
            long (float): Longitude coordinate of the Airport location.
        """
        self.icao = icao
        self.name = name
        self.city = city
        self.country = county

    def __repr__(self):
        pass

class Route:
    """ """

    def __init__(
        self,
        departure=None,
        arrival=None,
        distance=None,
        tempo=None,
        yDemand=None,
        jDemand=None,
        fDemand=None,
    ):
        """


        Args:
            departure (_type_, optional): _description_. Defaults to None.
            arrival (_type_, optional): _description_. Defaults to None.
            distance (_type_, optional): _description_. Defaults to None.
            tempo (_type_, optional): _description_. Defaults to None.
            yDemand (_type_, optional): _description_. Defaults to None.
            jDemand (_type_, optional): _description_. Defaults to None.
            fDemand (_type_, optional): _description_. Defaults to None.
        """
        self.departure = departure
        self.arrival = arrival
        self.distance = distance
        self.tempo = tempo
        self.yDemand = yDemand
        self.jDemand = jDemand
        self.fDemand = fDemand

    def __repr__(self):
        """

        Returns:
            _type_: _description_
        """
        return f"from {self.departure} to {self.arrival}"


class Pax:
    def __init__(self, route):
        self.route = route

    def SavePaxRoute():
        routes = open("routes.txt", "a")
        routes.write("a\n")
        routes.close()

    def __repr__(self):
        """
        This is the textual representation of the Pax class.

        Returns:
            str: ---
        """
        return f"{self.route}"


class Cargo:
    def __init__(self, *args):
        super(Cargo, self).__init__(*args)

    def __str__(self):
        return f"Pax route from {self.route.departure} to {self.route.arrival}"


routeTest = Route("LPPT", "LPMA")
paxTest = Pax(routeTest)

import math

while True:
    dist = int(input("Distância: "))
    print(str(dist) + " kms")

    tempo = int(input("Tempo em mins: "))
    viagens = math.ceil(1080 / (tempo * 0.9))
    print(str(tempo) + "mins = " + str(viagens) + " viagens\dia")

    y = int(input("Demand Passageiros Classe Eco: "))
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
