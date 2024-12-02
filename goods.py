class Goods:
    """
    Класс, представляющий товар.
    """
    def __init__(self, name: str, price: float, expiration_date: str, description: str = ''):
        """
        Инициализация товара.
        :param name: Название товара.
        :param price: Цена товара.
        :param expiration_date: Срок годности товара в формате "YYYY-MM-DD".
        :param description: Описание товара (опционально).
        """
        if price <= 0:
            raise ValueError("Цена должна быть положительным числом")
        self.name = name
        self.price = price
        self.expiration_date = expiration_date
        self.description = description

    def __str__(self):
        """
        Возвращает строковое представление товара.
        """
        return f"Товар: {self.name}, Цена: {self.price}, Срок годности: {self.expiration_date}, Описание: {self.description}"

    def __repr__(self):
        """
        Возвращает строковое представление объекта для разработчиков.
        """
        return f"Goods(name={self.name!r}, price={self.price}, expiration_date={self.expiration_date!r}, description={self.description!r})"

    def __eq__(self, other):
        """
        Сравнивает товары по их ключевым атрибутам.
        """
        if isinstance(other, Goods):
            return (self.name == other.name and
                    self.price == other.price and
                    self.expiration_date == other.expiration_date and
                    self.description == other.description)
        return False

    def __hash__(self):
        """
        Возвращает хэш для объекта, чтобы его можно было использовать в словарях.
        """
        return hash((self.name, self.price, self.expiration_date, self.description))
