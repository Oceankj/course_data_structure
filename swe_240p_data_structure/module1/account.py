class Account:
    def __init__(
        self, name: str, address: str, ssn: str, initial_deposit: float
    ):
        if initial_deposit < 0.0:
            raise ValueError("initial_deposit shoulb be positive")

        self.name = name
        self.address = address
        self.ssn = ssn
        self.balance = initial_deposit
