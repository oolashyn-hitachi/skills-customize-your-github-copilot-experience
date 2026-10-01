from functions import add_numbers, is_even


def test_add_numbers():
    assert add_numbers(2, 3) == 5


def test_is_even_with_even_number():
    assert is_even(4) is True


def test_is_even_with_odd_number():
    assert is_even(5) is False
