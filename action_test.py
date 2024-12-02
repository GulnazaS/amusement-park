import pytest
from action import Action

def test_Action():
    act = Action(name="test", duration=10, min_age=6, max_age=14)
    assert act.name == "test"
    assert act.duration == 10
    assert act.min_age == 6
    assert act.max_age == 14
    
    with pytest.raises(NotImplementedError):
        act.run()
