# Author: Сахапова Г.М.
# Date: 2024-12-05
# Description: Класс для создания фудкорта.

from location_with_goods import LocationWithGoods
from cafe import Cafe
from food import Food


class FoodCourt(LocationWithGoods):
    """
    Класс Фудкорта, наследующийся от LocationWithGoods.
    """
    def __init__(self, foodcourt_name: str, 
                 name: str, 
                 address: str, 
                 opening_hours: tuple = (), 
                 description: str = '', 
                 foodcourt_type: str = '',
                 kitchen: str = ''):
        """
        Инициализация объекта фудкорта.
        :param foodcourt_name: Название объекта фудкорта.
        :param name: Имя локации (например, название зоны или аттракциона).
        :param address: Адрес заведения.
        :param opening_hours: Часы работы заведения.
        :param description: Описание заведения.
        :param foodcourt_type: Тип заведения (ресторан, кафе и т.д.).
        :param kitchen: Вид кухни (итальянская, грузинская и т.д.).
        """
        super().__init__(name, address, opening_hours, description, foodcourt_type, kitchen)
        self.store_name = foodcourt_name  # Название заведения

    def add_cafe(self, name):
        """Добавляет новый ресторан в фудкорт."""
        if name not in self.cafe:
            self.cafe[name] = Cafe(name)
        else:
            print(f"Заведение {name} создано.")

    def remove_cafe(self, name):
        """Удаляет ресторан из фудкорта."""
        if name in self.cafes:
            del self.cafes[name]
        else:
            print(f"Заведение {name} не найдено на фудкорте.")

    def get_cafe_menu(self, name):
        """Возвращает меню указанного ресторана."""
        if name in self.cafes:
            return self.cafes[name].get_menu()
        else:
            print(f"Заведение {name} не найдено.")
            return None
        
    def place_order(self, cafe_name, food, quantity):
        """Размещает заказ у указанного ресторана."""
        if cafe_name in self.cafes:
            cafe = self.cafes[cafe_name]
            if food in cafe.menu:
                total_price = cafe.menu[food] * quantity
                print(f"Order placed: {quantity} x {food} from {cafe_name}. Итого: ${total_price:.2f}")
            else:
                print(f"Блюдо {food} отсутствует в меню заведения {cafe_name}.")
        else:
            print(f"Заведение {cafe_name} не найдено.") 


if __name__ == "__main__":
    # Создание объекта Фудкорта
    foodcourt = FoodCourt(
        foodcourt_name="Гурман Парк",
        name="Гурман",
        address="Улица Вкуса, 10",
        opening_hours=("10:00", "22:00"),
        description="Лучшие блюда со всего мира.",
        foodcourt_type="Фудкорт",
        kitchen="Разнообразная"
    )

    # Добавление кафе
    foodcourt.add_cafe("Итальянская кухня")
    foodcourt.add_cafe("Греческая таверна")
    foodcourt.add_cafe("Суши-бар")

    # Проверка меню кафе
    print(foodcourt.get_cafe_menu("Итальянская кухня"))

    # Заказ из кафе
    foodcourt.place_order("Итальянская кухня", "Паста", 2)
    foodcourt.place_order("Итальянская кухня", "Салат", 1)

    # Удаление кафе
    foodcourt.remove_cafe("Суши-бар")
