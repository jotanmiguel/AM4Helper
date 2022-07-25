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
    fleet = fleet.readlines[1:]
    return len(fleet)

def HighestIndex():
    """
    Returns the highest index of the fleet.

    Returns:
        int: Index.
    """
    fleet = open("./data/fleet.txt", "r")
    fleet = fleet.readlines()[1:]
    return int(max([line[1] for line in fleet]))


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
        " " + str(HighestIndex() + 1) + " -> " + str(aircraft) + "\n"
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


def RemovefromFleet(index: int):
    fleet = open("./data/fleet.txt", "r")
    fleet = fleet.readlines()
    fleet.pop(index)
    for line in fleet[index:]:
        line.replace(line, UpdateIndex(line, int(line[1]) - 1))
    saveFleet = open("./data/fleet.txt", "w")
    saveFleet.writelines(fleet)
    return fleet


def UpdateIndex(line: str, newIndex: int):
    """
    simple update fuction to replace the index from the fleet to a new given one.

    Args:
        line (str): Line from from the fleet file.
        newIndex (int): New index to be set.

    Returns:
        str: Returns the new line.
    """
    return line.replace(line, line[0] + str(newIndex) + line[2:])
