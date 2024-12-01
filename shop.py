from location_with_goods import LocationWithGoods
from goods import Goods
import unittest

class Shop(LocationWithGoods):
    """
    Класс магазина, наследующийся от LocationWithGoods.
    Добавлено поле склад для хранения товаров с их количеством.
    """
    def __init__(self, name: str, address: str, opening_hours: tuple = (), description: str = '', active: bool = True):
        """
        Инициализация магазина.
        """
        super().__init__(name, address, opening_hours, description, active)
        self.warehouse = {}  # Склад: {Goods: количество}

    def add_to_warehouse(self, good: Goods, quantity: int):
        """
        Добавить товар на склад.
        :param good: Объект товара.
        :param quantity: Количество добавляемого товара.
        """
        if quantity <= 0:
            raise ValueError("Количество должно быть больше 0")
        if good in self.warehouse:
            self.warehouse[good] += quantity
        else:
            self.warehouse[good] = quantity

    def remove_from_warehouse(self, good: Goods, quantity: int):
        """
        Уменьшить количество товара на складе.
        :param good: Объект товара.
        :param quantity: Количество снимаемого товара.
        """
        if good not in self.warehouse:
            raise ValueError(f"Товар '{good.name}' отсутствует на складе")
        if quantity > self.warehouse[good]:
            raise ValueError(f"Недостаточно товара '{good.name}' на складе")
        self.warehouse[good] -= quantity
        if self.warehouse[good] == 0:
            del self.warehouse[good]

    def get_warehouse_info(self):
        """
        Получить информацию о складе.
        :return: Список товаров на складе с их количеством.
        """
        return [(good.name, quantity) for good, quantity in self.warehouse.items()]





if __name__ == '__main__':
    # Создаем объект Shop
    souvenir_shop = Shop("Магазин сувениров", "Рядом с центральной площадью")

    # Создаем объекты Goods
    magnet = Goods(name="Магнит", price=50, expiration_date="2025-01-01", description="Сувенирный магнит")
    t_shirt = Goods(name="Футболка", price=500, expiration_date="2025-01-01", description="Футболка с логотипом парка")

    # Проверка: добавление товаров на склад
    print("Добавляем товары на склад...")
    souvenir_shop.add_to_warehouse(magnet, 100)
    souvenir_shop.add_to_warehouse(t_shirt, 50)

    # Выводим информацию о складе
    print("\nТекущий склад:")
    for good_name, quantity in souvenir_shop.get_warehouse_info():
        print(f"{good_name}: {quantity} шт.")

    # Проверка: удаление товаров со склада
    print("\nУменьшаем количество товаров...")
    souvenir_shop.remove_from_warehouse(magnet, 20)
    souvenir_shop.remove_from_warehouse(t_shirt, 5)

    # Выводим обновленную информацию о складе
    print("\nОбновленный склад:")
    for good_name, quantity in souvenir_shop.get_warehouse_info():
        print(f"{good_name}: {quantity} шт.")

    # Проверка: попытка удалить больше товаров, чем есть
    print("\nПроверка удаления большего количества, чем есть в наличии...")
    try:
        souvenir_shop.remove_from_warehouse(magnet, 200)
    except ValueError as e:
        print(f"Ошибка: {e}")

    # Проверка: попытка удалить несуществующий товар
    print("\nПроверка удаления несуществующего товара...")
    try:
        fake_good = Goods(name="Фальшивка", price=0, expiration_date="2023-01-01", description="Неизвестный товар")
        souvenir_shop.remove_from_warehouse(fake_good, 1)
    except ValueError as e:
        print(f"Ошибка: {e}")

    # Проверка: добавление некорректного количества
    print("\nПроверка добавления некорректного количества...")
    try:
        souvenir_shop.add_to_warehouse(magnet, -10)
    except ValueError as e:
        print(f"Ошибка: {e}")
