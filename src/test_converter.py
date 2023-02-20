import pytest
from converter import int_to_roman_numeral


def test_int_to_roman_numeral():
    assert int_to_roman_numeral(19) == "XIX"
    assert int_to_roman_numeral(1989) == "MCMLXXXIX"
    assert int_to_roman_numeral(3999) == "MMMCMXCIX"
    assert int_to_roman_numeral("19") == "O número que será convertido precisa ser um inteiro."
    assert int_to_roman_numeral(4000) == "O número que será convertido não pode ser maior do que 3999."