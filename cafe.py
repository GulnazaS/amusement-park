from foodcourt import FoodCourt

class Cafe(FoodCourt):
    """
    Класс Кафе, наследующийся от FoodCourt.
    Отличия - указание типа кафе и типа кухни
    """
    def __init__(self, name: str, address: str, opening_hours: tuple = (), description: str = '', active: bool = True, cuisine:str = None, cafe_type: str = None) :
        super().__init__(name=name, address=address, opening_hours=opening_hours, description=description, active=active)
        self._cuisine = cuisine  
        self._cafe_type = cafe_type 
    
    @property
    def cuisine(self):
        return self._cuisine
    
    @property
    def cafe_type(self):
        return self._cafe_type
    

if __name__ == '__main__':
    cafe = Cafe(
        name = "Гурман Парк",
        address = "Улица Вкуса, 10",
        opening_hours = ("10:00", "22:00"),
        description = "Лучшие блюда со всего мира.",
        cuisine = "Восточная кухня",
        cafe_type = "Ресторан высокой кухни",
        )

    print(cafe.cuisine, cafe.cafe_type, sep = ',')