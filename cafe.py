from foodcourt import FoodCourt

class Cafe(FoodCourt):
    """
    Класс Кафе, наследующийся от FoodCourt.
    """
    def __init__(self, cuisine:str, type_: str, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._cuisine = cuisine  
        self._cafe_type = type_ 
    
    @property
    def cuisine(self):
        return self._cuisine
    
    @property
    def cafe_type(self):
        return self._cafe_type
    

if __name__ == '__main__':
    cafe = Cafe(
        "Восточная кухня",
        "Ресторан высокой кухни",
        "Гурман Парк",
        "Улица Вкуса, 10",
        ("10:00", "22:00"),
        "Лучшие блюда со всего мира.")
    

    print(cafe.cuisine, cafe.cafe_type, sep = ',')