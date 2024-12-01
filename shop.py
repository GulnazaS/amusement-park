# Author: Лейман М.А.
# Date: 2024-12-01
# Description: Класс для создания магазина с товарами.

import unittest
from location_with_goods import LocationWithGoods
from goods import Goods


class Shop(LocationWithGoods):
    """
    Класс магазина, наследующийся от LocationWithGoods.
    Добавлено поле склад для хранения товаров с их количеством.
    """
    def __init__(self, store_name: str, name: str, address: str, opening_hours: tuple = (), description: str = '', active: bool = True):
        """
        Инициализация магазина.
        :param store_name: Название магазина.
        :param name: Имя локации (например, название зоны или аттракциона).
        :param address: Адрес магазина.
        :param opening_hours: Часы работы магазина.
        :param description: Описание магазина.
        :param active: Активен ли магазин.
        """
        super().__init__(name, address, opening_hours, description, active)
        self.store_name = store_name  # Название магазина
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

    def __str__(self):
        """ Возвращает строковое представление магазина """
        return f"Магазин: {self.store_name}, Локация: {self.name}, Адрес: {self.address}"


class TestShop(unittest.TestCase):
    def setUp(self):
        """
        Инициализация тестовых данных.
        """
        self.souvenir_shop = Shop("Магазин сувениров", "Магазин на площади", "Рядом с центральной площадью")
        self.magnet = Goods(name="Магнит", price=50, expiration_date="2025-01-01", description="Сувенирный магнит")
        self.t_shirt = Goods(name="Футболка", price=500, expiration_date="2025-01-01", description="Футболка с логотипом парка")

    def test_add_to_warehouse(self):
        """
        Тест добавления товаров на склад.
        """
        self.souvenir_shop.add_to_warehouse(self.magnet, 100)
        self.souvenir_shop.add_to_warehouse(self.t_shirt, 50)
        warehouse_info = self.souvenir_shop.get_warehouse_info()
        self.assertIn(("Магнит", 100), warehouse_info)
        self.assertIn(("Футболка", 50), warehouse_info)

    def test_remove_from_warehouse(self):
        """
        Тест удаления товаров со склада.
        """
        self.souvenir_shop.add_to_warehouse(self.magnet, 100)
        self.souvenir_shop.remove_from_warehouse(self.magnet, 20)
        warehouse_info = self.souvenir_shop.get_warehouse_info()
        self.assertIn(("Магнит", 80), warehouse_info)

    def test_remove_from_warehouse_invalid_quantity(self):
        """
        Тест ошибки при попытке удалить больше товара, чем есть на складе.
        """
        self.souvenir_shop.add_to_warehouse(self.magnet, 10)
        with self.assertRaises(ValueError) as context:
            self.souvenir_shop.remove_from_warehouse(self.magnet, 20)
        self.assertEqual(str(context.exception), "Недостаточно товара 'Магнит' на складе")

    def test_remove_nonexistent_good(self):
        """
        Тест ошибки при удалении несуществующего товара.
        """
        with self.assertRaises(ValueError) as context:
            fake_good = Goods(name="Фальшивка", price=0, expiration_date="2023-01-01", description="Неизвестный товар")
            self.souvenir_shop.remove_from_warehouse(fake_good, 1)
        self.assertEqual(str(context.exception), "Товар 'Фальшивка' отсутствует на складе")

    def test_add_invalid_quantity(self):
        """
        Тест ошибки при добавлении некорректного количества товара.
        """
        with self.assertRaises(ValueError) as context:
            self.souvenir_shop.add_to_warehouse(self.magnet, -5)
        self.assertEqual(str(context.exception), "Количество должно быть больше 0")

    def test_warehouse_info(self):
        """
        Тест вывода информации о складе.
        """
        self.souvenir_shop.add_to_warehouse(self.magnet, 100)
        self.souvenir_shop.add_to_warehouse(self.t_shirt, 50)
        warehouse_info = self.souvenir_shop.get_warehouse_info()
        self.assertEqual(warehouse_info, [("Магнит", 100), ("Футболка", 50)])

    def test_shop_str(self):
        """
        Тест для метода __str__.
        """
        self.assertEqual(str(self.souvenir_shop), "Магазин: Магазин сувениров, Локация: Магазин на площади, Адрес: Рядом с центральной площадью")




if __name__ == '__main__':
    # Создаем объект Shop
    # Проверка: Создание магазина
    print("\nСоздаём магазин...\n")
    souvenir_shop = Shop("Магазин сувениров","Магазин сувениров", "Рядом с центральной площадью")

    shop_str = str(souvenir_shop)  
    print(shop_str) 

    # Создаем объекты Goods
    magnet = Goods(name="Магнит", price=50, expiration_date="2025-01-01", description="Сувенирный магнит")
    t_shirt = Goods(name="Футболка", price=500, expiration_date="2025-01-01", description="Футболка с логотипом парка")

    # Проверка: добавление товаров на склад
    print("\nДобавляем товары на склад...")
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
      
    unittest.main()
    
    