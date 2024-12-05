from location_action import Location_Action
class Theater(Location_Action):
    '''Класс театра с добавлением свойств списка актеров'''

    def __init__(self, name: str, address: str, opening_hours: tuple = (), 
                 description: str = '', active: bool = True,
                 number_of_seats: int = 0, actors: tuple = ()):
        super().__init__(name=name, address = address, opening_hours = opening_hours, description = description, 
                         active = active, number_of_seats = number_of_seats)
        self.__actors = actors  # Список актеров

    @property
    def actors(self):
        return self.__actors
    
    def __str__(self):
        return f"{self.name}  Список акторов: {self.actors})"
    
if __name__ == "__main__":
    theater1 = theater("Театр Супер", "За забором", opening_hours = (10, 20), description="Самый крутой театр",
                                number_of_seats=150, actors=('Иванов', 'Петров', 'Сидоров', 'Дж.Клуни')
                                )
    print(theater1)