from location import Location


'''config just for exampleand future work'''
config = {
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
        if len(self.locations) == max_locations:
            raise RuntimeError("AmusementPark is full, cannot add new location")

        self.locations[name] = Location()  #todo add object creation later
        

    def remove(self, id: str)->None:
        '''delete location from park'''

        self.locations.pop(id, None)


    def top_visited(self, count = 10):
        '''return top count visited places'''
        locations = self._sort_locations(key = 'visited')

        return locations.items()[:count]

    def top_rated(self, count = 10):
        '''return top count visited places'''
        locations = self._sort_locations(key = 'rating')

        return locations.items()[:count]
    
    def _sort_locations(self, key: str):

        return {k:v for k, v in sorted(self.locations, key=lambda x: getattr(x, key), reverse=True)}