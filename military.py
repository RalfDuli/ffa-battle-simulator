class Military:

    def __init__(self, id: str, num_troops: int, firepower: float):
        self.__id = id
        self.__num_troops = num_troops
        self.__firepower = firepower

    def update(self, change_in_troops: float):
        self.__num_troops += change_in_troops

    def get_num_troops(self):
        return self.__num_troops

    def get_firepower(self):
        return self.__firepower

    def get_id(self):
        return self.__id
