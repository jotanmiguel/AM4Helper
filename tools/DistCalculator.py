from Classes.Airport import Airport
import geopy.distance


def calcDistance(departure:Airport, arrival:Airport):
    """
    Returns the distance between two Airports.

    Returns:
        float: The distance in kilometers.
    """
    
    return round(geopy.distance.geodesic(departure.coords,arrival.coords).km)
