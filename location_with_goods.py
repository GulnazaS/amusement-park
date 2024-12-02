# Author: Лейман М.А.
# Date: 2024-12-01
# Description: Класс для управления локацией с товарами.

from location import Location
import unittest


class LocationWithGoods(Location):
    """
    Класс локации с возможностью работы с товарами.
    """
    def __init__(self, name: str, address: str, opening_hours: tuple = (), description: str = '', active: bool = True):
        """
        Инициализация локации с товарами.
        """
        super().__init__(name, address, opening_hours, description, active)
        self.goods = []  # Список товаров
        self.promotions = {}  # Акции в формате {название товара: описание акции}

    def add_good(self, good):
        """
        Добавить товар в список.
        :param good: Объект товара.
        """
        self.goods.append(good)

    def add_promotion(self, good_name: str, promotion: str):
        """
        Добавить акцию на товар.
        :param good_name: Название товара.
        :param promotion: Описание акции.
        """
        self.promotions[good_name] = promotion

    def get_goods(self):
        """
        Получить список товаров.
        :return: Список товаров с акциями (если есть).
        """
        return [(good.name, f"Акция: {self.promotions[good.name]}" if good.name in self.promotions else "Без акции")
                for good in self.goods]



class TestLocationCreation(unittest.TestCase):
    def test_location_creation(self):
        loc = Location("Большая карусель", "У озера", opening_hours=(10, 20), description="Самая большая карусель")
        self.assertEqual(loc.name, "Большая карусель")
        self.assertEqual(loc.address, "У озера")
        self.assertEqual(loc.opening_hours, (10, 20))
        self.assertEqual(loc.description, "Самая большая карусель")
        self.assertTrue(loc.active)

    def test_location_with_goods_creation(self):
        loc_with_goods = LocationWithGoods("Магазин сувениров", "Рядом с выходом")
        self.assertEqual(loc_with_goods.name, "Магазин сувениров")
        self.assertEqual(loc_with_goods.address, "Рядом с выходом")
        self.assertListEqual(loc_with_goods.goods, [])
        self.assertDictEqual(loc_with_goods.promotions, {})






# Пример использования
if __name__ == '__main__':


    
    print("Creating Location...")
    loc = Location('Большая карусель', 'У озера', opening_hours=(10, 20), description='Самая большая карусель')
    print(f"Location created: {loc.name}, {loc.address}, {loc.opening_hours}, {loc.description}, Active: {loc.active}")

    print("\nCreating LocationWithGoods...")
    loc_with_goods = LocationWithGoods('Магазин сувениров', 'Рядом с выходом')
    print(f"LocationWithGoods created: {loc_with_goods.name}, {loc_with_goods.address}")
    print(f"Goods: {loc_with_goods.goods}, Promotions: {loc_with_goods.promotions}")
    
    
    unittest.main()