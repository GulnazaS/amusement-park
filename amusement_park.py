from location import Location
from typing import List

class AmusementPark:
    '''park class for handling locations
        add - add new location to park
        remove - delete location from park
    '''
    def __init__(self, max_locations: int = 100):
        '''
           max_locations - max capacity of park
        '''
        self._capacity = max_locations
        self._locations = {}

    @property
    def locations(self)->dict:
        return self._locations

    def add_location(self, new_location)->None:
        '''add location to park'''
        if len(self._locations) == self._capacity:
            raise RuntimeError("AmusementPark is full, cannot add new location")

        self._locations[new_location.name] = new_location


    def remove(self, loc_id: str)->None:
        '''delete location from park'''

        self._locations.pop(loc_id, None)


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
        return [i for i in self._locations.values() if i.active]

    def _sort_locations(self, key: str) -> List[Location]:
        return [i for i in sorted(self._locations.values(), key = lambda x: getattr(x, key), reverse=True)]
    
