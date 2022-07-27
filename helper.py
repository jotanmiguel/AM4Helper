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