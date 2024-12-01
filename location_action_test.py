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
