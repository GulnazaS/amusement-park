# Author: Сахапова Г.М.
# Date: 2024-12-05
# Description: Класс для создания фудкорта.

from location_with_goods import LocationWithGoods
from food import Food


class FoodCourt(LocationWithGoods):
    """
    Класс Фудкорта, наследующийся от LocationWithGoods.
    """
    def __init__(self, *args, **kwargs):
        """
        Инициализация объекта фудкорта.
        :param foodcourt_name: Название объекта фудкорта.
        :param name: Имя локации (например, название зоны или аттракциона).
        :param address: Адрес заведения.
        :param opening_hours: Часы работы заведения.
        :param description: Описание заведения.
        """
        super().__init__(*args, **kwargs)

    def place_order(self, food: str, quantity: int) -> float:
        """Размещает заказ """

        if not isinstance(quantity, int):
            raise ValueError(f'quantity must be int value, found: {type(quantity)}')

        for food_menu in self.goods:
            if food == food_menu.name:
                return quantity * food_menu.price

        raise ValueError(f'No food {food} in this foodcourt')

if __name__ == "__main__":
    # Создание объекта Фудкорта
    foodcourt = FoodCourt(
        "Гурман Парк",
        "Улица Вкуса, 10",
        ("10:00", "22:00"),
        "Лучшие блюда со всего мира.",
    )



    foodcourt.add_good(Food('Паста', 4.5, 'Завтра', weight=1500))
    foodcourt.add_good(Food('Салат', 3.20, 'Завтра', weight=300))

    # Заказ из кафе
    print(foodcourt.place_order("Паста", 2))
    print(foodcourt.place_order("Салат", 1))

