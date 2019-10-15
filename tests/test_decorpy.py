"""Tests for `decorpy` package."""
import pytest
import math
from timeit import default_timer
from decorpy import timer, debug, check_types


def test_timer(capsys):
    """Test the time measurement of the timer decorator"""
    def long_func(n):
        sum = 0
        for i in range(n):
            sum += i
        return sum
    # Naive time
    start_test = default_timer()
    res = long_func(10)
    end_test = default_timer()
    total_time_magnitude = int(math.log10(end_test - start_test))
    # Decorator time
    long_func = timer(long_func)
    res = long_func(10)
    captured = capsys.readouterr()
    decorator_magnitude = int(math.log10(
        float(captured.out.split(" seconds")[0].split("is ")[1])))
    assert decorator_magnitude == total_time_magnitude


def test_debug(capsys):
    """Tests if return value and signature of function is correct"""
    @debug
    def debug_func(n, k=3):
        return n ** k
    test = debug_func(3, k=2)
    captured = capsys.readouterr()
    assert "Now calling debug_func(3, k=2)" in captured.out and "Call with debug_func(3, k=2) -> returned 9" in captured.out


def test_types_count_input():
    """Test that exception is raised for invalid number of input parameters"""

    @check_types(input=(int, int), output=(int,))
    def test(n):
        pass

    with pytest.raises(Exception) as e:
        assert test(5)
    assert str(e.value) == "The function expected 2 parameters."


def test_types_count_output():
    """Test that exception is raised for invalid number of output values"""

    @check_types(input=(int,), output=(int, int))
    def test(n):
        return n

    with pytest.raises(Exception) as e:
        assert test(5)
    assert str(e.value) == "The function expected 2 return values."


def test_wrong_input_types_check():
    """Test that exception is raised for invalid types"""

    @check_types(input=(int, str), output=(str,))
    def test(n, base_str):
        return base_str * n

    with pytest.raises(Exception) as e:
        assert test("5", "test")
    assert (
        str(e.value)
        == "The type of 5 and input[0] are different : <class 'str'> and <class 'int'>"
    )


def test_wrong_output_types_check():
    """Test that exception is raised for invalid types"""

    @check_types(input=(int, int), output=(int, ))
    def test(n1, n2):
        return n1 * n2 * 1.0

    with pytest.raises(Exception) as e:
        assert test(5, 2)
    assert (
        str(e.value)
        == "The type of 10.0 and output[0] are different : <class 'float'> and <class 'int'>"
    )

def test_wrong_output_tuple_types_check():
    """Test that exception is raised for invalid types"""

    @check_types(input=(int, int), output=(int, int))
    def test(n1, n2):
        return (n1, n2 * 1.0)

    with pytest.raises(Exception) as e:
        assert test(5, 2)
    assert (
        str(e.value)
        == "The type of 2.0 and output[1] are different : <class 'float'> and <class 'int'>"
    )

def test_wrong_output_tuple_length_types_check():
    """Test that exception is raised for invalid types"""

    @check_types(input=(int, int), output=(int, int))
    def test(n1, n2):
        return (n1 + n2 * 1.0, )

    with pytest.raises(Exception) as e:
        assert test(5, 2)
    assert (
        str(e.value)
        == "The function expected 2 return values."
    )

def test_correct_output_types_check():
    """Test that exception is raised for invalid types"""

    @check_types(input=(int, int), output=(float, ))
    def test(n1, n2):
        return n1 * n2 * 1.0

    assert test(5, 2) == 10.0
