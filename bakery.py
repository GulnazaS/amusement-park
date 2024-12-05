from foodcourt import FoodCourt

class Bakery(FoodCourt):
    """
    Класс Кондитерской, наследующийся от FoodCourt. Отличается специальным дессертом
    """

    def __init__(self, special:str, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._special_dessert = special  
        self.best_sellers = set()  # Лучшие продавцы

    @property
    def main_dessert(self):
        '''Главный дессерт заведения'''
        return self._special_dessert


if __name__ == "__main__":

    bakery = Bakery(
        'Торт Медовик',
        "Гурман Парк",
        address="Улица Вкуса, 10",
        opening_hours=("10:00", "22:00"),
        description="Лучшие блюда со всего мира.",
    )

    # Добавляем пункты в меню
    bakery.add_item("Торт 'Медовик'", 15.00)
    bakery.add_item("Круассан", 2.50)
    bakery.add_item("Пирожное 'Эклер'", 3.00)


    # Получаем обновленное меню
    print("Меню:", bakery.menu)
    print("Супер дессерт:", bakery.main_dessert)
