# -*- coding: utf-8 -*-

from amusement_park import AmusementPark
from attraction import Attraction
from theater import Theater
from shop import Shop
import random


#Демонстрация работы парка развлечений 

park = AmusementPark(max_locations = 10)

park.add_location(Attraction(
    "Карусель", 
    "У озера", 
    opening_hours = (10, 20), 
    description="Средненькая карусель",
    number_of_seats=20, 
    duration=8, 
    fun_level=5))

park.add_location(Theater(
    "Театр Супер",
    "За забором",
    opening_hours = (10, 20),
    description="Самый крутой театр",
    number_of_seats=150,
    actors=('Иванов', 'Петров', 'Сидоров', 'Дж.Клуни')
    ))

park.add_location(Shop("Магазин сувениров","Магазин сувениров", "Рядом с центральной площадью"))


keys = tuple(park.locations.keys())

for i in range(1000):    #random visit and rate
    key = random.choice(keys)
    park._locations[key].visit()
    park._locations[key].rating = random.randint(1, 5)

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
