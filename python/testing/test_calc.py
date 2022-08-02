import pytest
from calcFunctions import *
import datetime

@pytest.mark.add #adds a marker called 'add'
@pytest.mark.mygroup #adds a marker called 'my group'
def test_add_1():
    obj = CalcFunctions()
    assert 10 == obj.add_two(4, 6)

#@pytest.mark.xfail #expected to fail'
@pytest.mark.add
def test_add_2():
    obj = CalcFunctions()
    assert 11 == obj.add_two(7, 5)

@pytest.mark.multiply
def test_mult_1():
    obj = CalcFunctions()
    assert 24 == obj.multiply_two(3, 8)

#@pytest.mark.xfail
@pytest.mark.multiply
def test_mult_2():
    obj = CalcFunctions()
    assert 25 == obj.multiply_two(4, 6)

#@pytest.mark.skipif(datetime.datetime.today().weekday() == 1, reason = "It's Tuesday")
@pytest.mark.cube
def test_cube_1():
    obj = CalcFunctions()
    assert 27 == obj.cube(3)

#@pytest.mark.skipif(datetime.datetime.today().weekday() == 1, reason = "It's Tuesday")
#@pytest.mark.xfail
@pytest.mark.cube
@pytest.mark.mygroup
def test_cube_2():
    obj = CalcFunctions()
    assert 65 == obj.cube(4)
