from action import Action
from location import Location

class Location_Action(Location):
    '''абстрактный класс для локаций с действием'''
    
    def __init__(self, name: str, address: str, opening_hours: tuple = (), 
                 description: str = '', active: bool = True,
                 number_of_seats: int = 0,
                 ):
        super().__init__(name=name, address=address, opening_hours=opening_hours, description=description, active=active)
        self.__actions = {} # словарь действий
        self.__is_one_action = False  # флаг того, что в локации возможно только одно действие
        self.__number_of_seats = number_of_seats # количество мест для посетитителей на один сеанс
        self.__free_seats = number_of_seats  # количество свободных мест
        
    @property
    def number_of_seats(self):
        return self.__number_of_seats

    @property
    def free_seats(self):
        return self.__free_seats
        
    @property
    def action(self):
        return self.__actions

        
    def add_action(self, name:str, *args, **kwargs):
        '''добавляет действие в локацию'''
        if self.__is_one_action and len(self.__actions.keys()) > 0:
            raise ValueError(f"Локация '{self.name} может содержать только одно действие")
        
        self.action[name] = Action(name, *args, **kwargs)


    def remove_action(self, name: str):
        '''удаляет действие из локации'''
        if name in self.__actions.keys():
            self.__actions.pop(name)

    def sell_ticket(self, count: int =  0):
        '''продажа билетов'''
        if count <= 0:
            raise ValueError(f"Количество продаваемых билетов должно быть болше 0")
        if (self.__free_seats - count) >= 0:
            self.__free_seats -= count
        else:
            raise ValueError(f"В локации '{self.name}' нет нужного количества свободных мест")

    def reset_free_seats(self):
        self.__free_seats = self.__number_of_seats
        