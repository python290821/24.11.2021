class Shopping:
    def __init__(self, id, name, amount, maavar):
        self.id = id
        self.name = name
        self.amount = amount
        self.maavar = maavar

    def __repr__(self):
        return str(self.__dict__)

    def __str__(self):
        return str(self.__dict__)