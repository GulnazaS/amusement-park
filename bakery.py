from foodcourt import FoodCourt

class Bakery(FoodCourt):
    """
    Класс Кондитерской, наследующийся от FoodCourt. Отличается специальным дессертом
    """

    def __init__(self, name: str, address: str, opening_hours: tuple = (), description: str = '', active: bool = True):
        super().__init__(name=name, address=address, opening_hours=opening_hours, description=description, active=active)
        self._main_desert = None

    @property
    def main_dessert(self):
        '''Главный дессерт заведения'''
        return self._main_desert
    
    def add_good(self, good, is_main_dessert = False):
        super().add_good(good)
        # если это главный десерт - запомнить его
        if is_main_dessert:
           self._main_desert = good



if __name__ == "__main__":

    bakery1 = Bakery(
        name = "Выпечка",
        address = "Улица Вкуса, 10",
        opening_hours = ("10:00", "22:00"),
        description = "Лучшие десерты."
    )

    from food import Food
    
    bakery1.add_good(Food('Круасан', 4.5, 'Завтра', weight=1500))
    bakery1.add_good(Food('Пончик', 3.20, 'Завтра', weight=300), is_main_dessert = True)
    

    print("Супер дессерт:", bakery1.main_dessert)
    
