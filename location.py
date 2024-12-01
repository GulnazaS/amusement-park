from collections import deque
import random 

class Rating:
    '''class for storing rating. 
    Actually have to interface for storing rating with different methods
    implementated on colelctions deque with given length'''
    def __init__(self, depth:int = 10):
        '''storing latest rating'''
        self.db = deque(maxlen=depth)

    def add(self, rating:int):
        '''rating must be between 1 and 5'''

        if not isinstance(rating, int) or rating < 1 or rating > 5:
            raise ValueError(f'Rating must be integer in range (1, 5), found {rating} of type: {type(rating)}')
        
        self.db.append(rating)

    @property
    def mean(self)->int:
        '''return mean rating from latest'''
        if not self.db:
            raise ValueError('No rating yet')
        return sum(self.db) / len(self.db)

class Location:
    '''abstract class for amusement park location'''
    
    def __init__(self, name: str, address: str, opening_hours: tuple = (), description: str = '', active: bool = True):
        '''active - is working now or not'''
        self.name = name
        self.address = address
        self.opening_hours = opening_hours
        self.description = description
        self.visit_counter = 0
        self.active = active
        self.rate = Rating(10)  #store only last 10 ratings

    def visit(self):
        '''emulate visit location. Maybe form smart camera for counting people or entrance counter. Doesn't matter'''
        self.visit_counter += 1

    @property
    def rating(self):
        '''user rating of location'''
        return self.rate.mean

    @rating.setter
    def rating(self, new_rate):
        self.rate.add(new_rate)


if __name__ == '__main__':
    loc = Location('Большая карусель', 'У озера', opening_hours = (10, 20), description = 'Самая большая карусель в парке')

    try:
        print(loc.rating)
    except ValueError:
        print('No rating specified')

    #emulate visits and set rating
    for i in range(50):
        loc.visit()
        loc.rating = random.randint(1, 5)

    print(loc.rating, loc.visit_counter)