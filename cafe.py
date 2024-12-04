from foodcourt import FoodCourt

class Cafe(FoodCourt):
    """
    Класс Кафе, наследующийся от FoodCourt.
    """
    def __init__(self, name):
        self.name = name
        self.menu = {}
    
    def add_item(self, item_name, price):
        """Добавляет новый пункт в меню."""
        self.menu[item_name] = price
    
    def remove_item(self, item_name):
        """Удаляет пункт из меню."""
        if item_name in self.menu:
            del self.menu[item_name]
        else:
            print(f"Item {item_name} not found on the menu.")
            
    def get_menu(self):
        """Возвращает текущее меню."""
        return self.menu