from location_action import Location_Action

class Attraction(Location_Action):
    '''Класс аттракциона с добавлением свойств длительности и уровня фана'''

    def __init__(self, name: str, address: str, opening_hours: tuple = (), 
                 description: str = '', active: bool = True,
                 number_of_seats: int = 0, duration: int = 0, fun_level: int = 0):
        super().__init__(name=name, address = address, opening_hours = opening_hours, description = description, 
                         active = active, number_of_seats = number_of_seats)
        self.__duration = duration  # длительность действия в минутах
        self.__fun_level = fun_level  # уровень фана 

    @property
    def duration(self):
        return self.__duration

    @property
    def fun_level(self):
        return self.__fun_level
    
    def __str__(self):
        return f"{self.name} (Адрес: {self.address}, Длительность: {self.duration} мин, Уровень фана: {self.fun_level})"


if __name__ == "__main__":
    attraction1 = attraction("Карусель", "У озера", opening_hours = (10, 20), description="Средненькая карусель",
                                number_of_seats=20, duration=8, fun_level=5
                                )
    print(attraction1)
    print("Общее количество мест:", attraction1.number_of_seats)
    print("Посадочных мест:", attraction1.free_seats)

    # Продажа билетов
    attraction1.sell_ticket(5)
    print("Свободных мест:", attraction1.free_seats)