"""Tests for `decorpy` package."""
import pytest
from decorpy import timer, debug, check_types


def test_types_count_input():
    """Test that exception is raised for invalid number of input parameters"""

    @check_types(input=(int, int), output=(int, ))
    def test(n):
        pass

    with pytest.raises(Exception) as e:
        assert test(5)
    assert str(e.value) == "The function expected 2 parameters."


def test_types_count_output():
    """Test that exception is raised for invalid number of output values"""

    @check_types(input=(int, ), output=(int, int))
    def test(n):
        return n

    with pytest.raises(Exception) as e:
        assert test(5)
    assert str(e.value) == "The function expected 2 return values."


def test_types_check():
    """Test that exception is raised for invalid types"""

    @check_types(input=(int, str), output=(str, ))
    def test(n, base_str):
        return base_str * n

    with pytest.raises(Exception) as e:
        assert test("5", "test")
    assert str(
        e.value) == "The type of 5 and input[0] are different : <class 'str'> and <class 'int'>"
