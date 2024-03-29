class Aircraft:
    """
    This class represents an unique aircraft model.
    """

    def __init__(
        self,
        number: str,
        manufacturer: str,
        model: str,
        engine: str,
        speed: int,
        range: int,
        consumption: float,
        emission: float,
        check: int,
        capacity: int,
    ):
        """
        Constructor of this class Aircraft.

        Args:
            number (_type_): _description_
            manufacturer (_type_): _description_
            model (_type_): _description_
            engine (_type): _description_
            speed (_type_): _description_
            range (_type_): _description_
            consumption (_type_): _description_
            emission (_type_): _description_
            check (_type_): _description_
            capacity (_type_): _description_
        """
        self.number = number.upper()
        self.manufacturer = manufacturer
        self.model = model
        self.engine = engine
        self.speed = speed
        self.range = range
        self.consumption = consumption
        self.emission = emission
        self.check = check
        self.capacity = capacity

    def __repr__(self):
        """
        this method is a textual representation of the Aircraft class.

        Returns:
            str: textual representation of the aircraft.
        """
        return f"{self.number} - {self.manufacturer} {self.model}"
