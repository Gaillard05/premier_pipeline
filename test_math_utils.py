import pytest
from math_utils import calculate_average

def test_calculate_average_valid_input():
    assert calculate_average([1, 2, 3, 4, 5]) == 3.0
    assert calculate_average([10, 20, 30]) == 20.0
    assert calculate_average([1.5, 2.5, 3.5]) == 2.5

def test_calculate_average_empty_list():
    with pytest.raises(ValueError):
        calculate_average([])

def test_calculate_average_single_value():
    assert calculate_average([42]) == 42
