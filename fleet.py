import Aircraft as ac


def ViewFleet():
    fleet = open("./data/fleet.txt", "r")
    fleet = fleet.readlines()[1:]
    for aircraft in fleet:
        print(aircraft)


def FleetSize():
    """
    Return the current fleet size.

    Returns:
        int: Size of the fleet.
    """
    fleet = open("./data/fleet.txt", "r")
    fleet = fleet.readlines()[1:]
    return len(fleet)


def AddtoFleet(aircraft: ac.Aircraft):
    """
    Adds to the fleet a new or a not yet registered aircraft.

    Args:
        aircraft (ac.Aircraft): Unique Aircraft to add.

    Returns:
        str: Confirmation message
    """
    #
    fleet = open("./data/fleet.txt", "a")
    fleet = fleet.write(
        " " + str(FleetSize() + 1) + " -> " + str(aircraft) + "\n"
    )  # change the aircraft representation to a more coherent form
    return "added"

def ResetFleet():
    """
    Resets the fleet and returns a simple confirmation message.

    Returns:
        str: Confimartion message.
    """
    fleet = open("./data/fleet.txt", "w")
    fleet = fleet.write("Fleet:\n")
    return "done"