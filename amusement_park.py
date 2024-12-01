import random
from location import Location
from typing import List

'''config just for exampleand future work'''
config_locations = {
    'Theater': {'capacity': 100, 'name': 'Theater'},
    'Carousel': {'fun': 9, 'name': 'SuperCarousel'}
}

class AmusementPark:
    '''park class for handling locations
        add - create and add new location to park
        remove - delete 
    '''
    def __init__(self, config: dict = None, max_locations: int = 100):
        '''config - dict of locations configs
           max_locations - max capacity of park
        '''
        self.capacity = max_locations
        self.locations = {}
        if config:
            print('initialize locations will be later')

        
    def add(self, name: str, *args, **kwargs)->None:
        '''add location to park'''
        if len(self.locations) == self.capacity:
            raise RuntimeError("AmusementPark is full, cannot add new location")

        self.locations[name] = Location(name, *args, **kwargs)  #todo add object creation later
        

    def remove(self, loc_id: str)->None:
        '''delete location from park'''

        self.locations.pop(loc_id, None)


    def top_visited(self, count = 10) -> List[Location]:
        '''return top count visited places'''
        locations = self._sort_locations(key = 'visit_counter')

        return locations[:count]

    def top_rated(self, count = 10) -> List[Location]:
        '''return top count visited places'''
        locs = self._sort_locations(key = 'rating')
        return locs[:count]
    
    def active_now(self) -> List[Location]:
        '''return locations which are currently working'''
        return [i for i in self.locations.values() if i.active]

    def _sort_locations(self, key: str) -> List[Location]:
        return [i for i in sorted(self.locations.values(), key = lambda x: getattr(x, key), reverse=True)]
    




if __name__ == '__main__':

    park = AmusementPark(max_locations = 10)

    park.add('Большая карусель', 'У озера', opening_hours = (10, 20), description = 'Самая большая карусель в парке', active = False)
    park.add('Колесо обозрения', '-', opening_hours = (10, 20), description = 'Живописная панорама Иртыша и города с высоты 68 метров действительно захватывает дух!')
    park.add('Колесо обозрения Детское', '-', opening_hours = (10, 20), description = 'Детское колесо обозрения — это миниатюрное колесо обозрения для детей, которое поднимает их в небо, даря волшебные виды', active = False)
    park.add('Автодром', 'Главный вход', opening_hours = (9, 18), description = 'Мини автодром - это маленький мир скорости, веселья и приключений, специально созданный для наших маленьких гонщиков! Здесь каждый ребенок может почувствовать себя настоящим героем гонок, взяв руль в свои руки и погоняв на своей машинке!')

    keys = tuple(park.locations.keys())

    for i in range(1000):    #random visit and rate
        key = random.choice(keys)
        park.locations[key].visit()
        park.locations[key].rating = random.randint(1, 5)

    #print top 3 most rated locations
    top_rated = park.top_rated(count = 3)
    print(*((i.name, i.rating) for i in top_rated), sep = ', ') 

    #print top 3 most rated locations
    top_visited = park.top_visited(count = 3)
    print(*((i.name, i.visit_counter) for i in top_visited), sep = ', ') 

    #print locations which are active
        #print top 3 most rated locations
    active = park.active_now()
    print('Сейчас работают: ', *(i.name for i in active), sep = ', ') 
