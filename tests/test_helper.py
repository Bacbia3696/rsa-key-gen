from src import helper
import pytest


@pytest.mark.parametrize("test_input,expected", [
    (7, True),
    (13, True),
    (43, True),
    (4, False),
    (20, False),
    (0, False),
])
def test_is_prime(test_input, expected):
    return helper.is_prime(test_input) == expected


def test_extended_gcd():

    # Assert True
    num1 = 2**3*7
    num2 = 2**9*3**4
    gcd, x, y = helper.extended_gcd(num1, num2)
    assert gcd == num1*x+num2*y
    assert gcd == 8


def test_generate_prime_number():
    prime_number = helper.generate_prime_number(1)
    # check if prime_numer is prime
    assert helper.is_prime(prime_number)
