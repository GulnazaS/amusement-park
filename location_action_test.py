import pytest
from action import Action
from location_action import Location_Action


TOTAL_SEATS = 4

def create_test_location(number_of_seats = TOTAL_SEATS):
    return Location_Action(name='Большая карусель', address='У озера', opening_hours = (10, 20), description = 'Самая большая карусель в парке', 
                           number_of_seats = number_of_seats)


def test_Action_create():
    loc = create_test_location(4)
    assert isinstance(loc, Location_Action)
    # корректность инициализации переменных
    assert loc.number_of_seats == TOTAL_SEATS
    assert loc.free_seats == TOTAL_SEATS

def test_Action_sell_ticket():
    loc = create_test_location()
    with pytest.raises(ValueError):
        loc.sell_ticket()
        
    loc.sell_ticket(1)
    assert loc.free_seats == 3
    loc.sell_ticket(2)
    assert loc.free_seats == 1

    with pytest.raises(ValueError):
        loc.sell_ticket(2)
        
    loc.sell_ticket(1)
    assert loc.free_seats == 0

    with pytest.raises(ValueError):
        loc.sell_ticket(1)
    

def test_Action_reset_free_seats():
    loc = create_test_location()
    loc.sell_ticket(3)
    assert loc.free_seats == 1
    loc.reset_free_seats()
    assert loc.free_seats == TOTAL_SEATS

    loc.sell_ticket(4)
    assert loc.free_seats == 0
    loc.reset_free_seats()
    assert loc.free_seats == TOTAL_SEATS

def test_add_action():
    loc = create_test_location()
    loc.add_action(name='Представление 1', duration=10, min_age=5, max_age=15)
    loc.add_action(name='Представление 2', duration=12, min_age=4, max_age=11)

    assert len(loc.actions.keys()) == 2
    act = loc.actions['Представление 1']
    assert act.duration == 10
    assert act.min_age == 5
    assert act.max_age == 15
    
    act = loc.actions['Представление 2']
    assert act.duration == 12
    assert act.min_age == 4
    assert act.max_age == 11    
    
def test_remove_action():
    loc = create_test_location()
    loc.add_action(name='Представление 1', duration=10, min_age=5, max_age=15)
    loc.add_action(name='Представление 2', duration=12, min_age=4, max_age=11)

    assert len(loc.actions.keys()) == 2
    loc.remove_action('Представление 1')
    assert len(loc.actions.keys()) == 1
    assert loc.actions['Представление 2'] is not None

    loc.remove_action('Представление 1')
    assert len(loc.actions.keys()) == 1
