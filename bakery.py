from foodcourt import FoodCourt

class Bakery(FoodCourt):
    """
    Класс Кондитерской, наследующийся от FoodCourt.
    """

    def __init__(self, name):
        super().__init__(name)  # Укажите параметры, такие как адрес и часы работы, при необходимости
        self.menu = {}
        self.bakery_types = ["торты", "печенье", "пирожные", "кексы"]  # Примеры типов выпечки
        self.best_sellers = []  # Лучшие продавцы

    def add_item(self, item_name, price):
        """Добавляет новый пункт в меню кондитерской."""
        self.menu[item_name] = price
        print(f"Item {item_name} added to the bakery menu with price ${price:.2f}")

    def remove_item(self, item_name):
        """Удаляет пункт из меню кондитерской."""
        if item_name in self.menu:
            del self.menu[item_name]
            print(f"Item {item_name} removed from the bakery menu.")
        else:
            print(f"Item {item_name} not found on the bakery menu.")

    def get_menu(self):
        """Возвращает текущее меню кондитерской."""
        return self.menu

    def get_bakery_types(self):
        """Возвращает список типов выпечки, которые предлагает кондитерская."""
        return self.bakery_types

    def check_item_availability(self, item_name):
        """Проверяет наличие определенного кондитерского изделия в меню."""
        if item_name in self.menu:
            print(f"{item_name} доступно в меню по цене ${self.menu[item_name]:.2f}.")
        else:
            print(f"{item_name} отсутствует в меню.")

if __name__ == "__main__":
    bakery = Bakery(name="Sweet Delights")

    # Добавляем пункты в меню
    bakery.add_item("Торт 'Медовик'", 15.00)
    bakery.add_item("Круассан", 2.50)
    bakery.add_item("Пирожное 'Эклер'", 3.00)

    # Получаем текущее меню
    print("Текущее меню кондитерской:", bakery.get_menu())

    # Получаем типы выпечки
    print("Типы выпечки:", bakery.get_bakery_types())

    
    # Проверяем наличие пункта в меню
    bakery.check_item_availability("Круассан")
    bakery.check_item_availability("Торт 'Тирамису'")

    # Удаляем пункт из меню
    bakery.remove_item("Круассан")

    # Получаем обновленное меню
    print("Обновленное меню кондитерской:", bakery.get_menu())