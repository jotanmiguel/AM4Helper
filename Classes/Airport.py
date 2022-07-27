class Airport:
    """
    This class represents an unique Airport in the game.
    """

    def __init__(self, icao: str, city: str, county: str, coords: dict[str, float]):
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
        self.city = city
        self.country = county
        self.coords = coords
        
    __file__

    def __repr__(self):
        pass

    def getCoords(self):
        """
        Returns the coordinates of this Airport.

        Returns:
            tuple(float,float): The par of lat and long coordinates.
        """
        return (self.coords["lat"], self.coords["long"])
