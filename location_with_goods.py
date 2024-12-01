
from location import Location


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




# Пример использования
if __name__ == '__main__':

    # Добавляем товары
    # food_court.add_good(Goods(name="Хот-дог", price=150, expiration_date="2024-12-01"))
    # food_court.add_good(Goods(name="Кофе", price=100, expiration_date="2024-12-01"))
    # shop.add_good(Goods(name="Магнит", price=50, expiration_date="2025-01-01"))
    # shop.add_good(Goods(name="Футболка", price=500, expiration_date="2025-01-01"))


