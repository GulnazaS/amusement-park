from goods import Goods
class Food(Goods):
    """
    Класс, представляющий товар.
    """
    def __init__(self,
                 name: str,
                 price: float,
                 expiration_date: str,
                 description: str = '',
                 product_composition: str = '',
                 weight: int = 0,
                 nutrition_val : str = ''):
        """
        Инициализация товара.
        :param name: Название товара.
        :param price: Цена товара.
        :param expiration_date: Срок годности товара в формате "YYYY-MM-DD".
        :param description: Описание товара (опционально).
        
        :param product_composition: Состав товара (опционально).
        :param nutrition_val: Пищевая ценность товара (опционально).
        :param weight: Вес товара (опционально).
        """
        super().__init__(name=name, price=price, expiration_date=expiration_date, description=description)
        if price <= 0:
            raise ValueError("Цена должна быть положительным числом")
        self.product_composition = product_composition
        self.weight = weight
        self.nutrition_val = nutrition_val

    def __str__(self):
        """
        Возвращает строковое представление товара.
        """
        return f'''Товар: {self.name},
                Цена: {self.price},
                Срок годности: {self.expiration_date}, 
                Состав товара: {self.product_composition},
                Вес: {self.weight},
                Пищевая ценность: {self.nutrition_val}'''

    def __repr__(self):
        """
        Возвращает строковое представление объекта для разработчиков.
        """
        return f'''Food(name={self.name!r}, 
                price={self.price}, 
                expiration_date={self.expiration_date!r}, 
                product_composition={self.product_composition!r},
                weight ={self.weight!r}, 
                nutrition_val={self.nutrition_val!r})'''

    def __hash__(self):
        """
        Возвращает хэш для объекта, чтобы его можно было использовать в словарях.
        """
        return hash((self.name, self.price, self.expiration_date, self.product_composition,self.weight, self.nutrition_val))


