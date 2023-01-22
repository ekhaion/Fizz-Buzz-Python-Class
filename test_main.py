import pytest
from main import FizzBuzz, _is_modulo_3_equal_0, _is_modulo_5_equal_0


@pytest.fixture
def fizzbuzz_object():
    return FizzBuzz(fizzbuzz="fizzbuzz", numbers_to_divide=15)


def test__display_word(fizzbuzz_object):
    assert -_is_modulo_3_equal_0(15) and _is_modulo_5_equal_0(15)
    assert _is_modulo_3_equal_0(3)
    assert _is_modulo_5_equal_0(5)


def test_loop_on_numbers_to_divide(fizzbuzz_object):
    assert fizzbuzz_object.loop_on_numbers_to_divide()
