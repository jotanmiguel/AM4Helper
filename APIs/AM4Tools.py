import requests, json
from Classes.Airport import Airport
import tools.CheckRequests as checkreq

# GET /aircraft/search
baseUrl = "https://api.am4tools.com"


def SearchAirport(code: str):
    """
    Search Airport with the given ICAO or IATA code.

    Args:
        code (str): Code of the airport being search. Be sure to use a valid code.

    Returns:
        Airport: The airport with the IATA or ICAO code.
    """
    endpoint = "/airport/search"
    params = {"mode": "normal", "code": code}

    response = requests.get(
        baseUrl + endpoint,
        params=params,
        headers={
            "x-access-token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOjIxOTgyNjMsImlhdCI6MTY1ODc4MTkzNn0.pN9f-ArhqWDTac4GEM0Aueb_Ea8PLg-bge4bWogmIOI"
        },
    )

    if response.status_code == 200:
        data_json = json.loads(response.text)
        data_json = data_json["airports"]
        data = data_json[0]

        return Airport(
            data["icao"],
            data["city"],
            data["country"],
            (data["latitude"], data["longitude"]),
        )
    else:
        return "Error"
