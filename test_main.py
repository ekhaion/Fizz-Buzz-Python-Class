import pytest
from main import FizzBuzz


@pytest.fixture
def fizzbuzz_object():
    return FizzBuzz(fizzbuzz="fizzbuzz", numbers_to_divide=15, numbers_fizzbuzz=(3, 5, 7))
