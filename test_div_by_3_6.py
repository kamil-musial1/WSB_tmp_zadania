import conftest
import pytest


@pytest.fixture
def input_value():
   input = 39
   return input

def test_divisible_by_3(input_value):
    assert input_value % 3 == 0


def test_divisible_by_6(input_value):
    assert input_value % 6 == 0


# def input_value2():
#    input = 39
#    return input
#
# def test_divisible_by_31():
#    assert input_value2() % 3 == 0
#
# def test_divisible_by_61():
#    assert input_value2() % 6 == 0