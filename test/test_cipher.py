import pytest

from functionality.cipher import ROT13


@pytest.fixture
def return_ROT13_object():
    return ROT13()


def test_should_return_proper_encoded_value_when_input_is_lower_str(
    return_ROT13_object,
):
    input = "aaa"
    expected = "nnn"
    assert return_ROT13_object.encode_decode(input) == expected


def test_should_return_proper_encoded_value_when_input_is_upper_str(
    return_ROT13_object,
):
    input = "ZZZZZ"
    expected = "MMMMM"
    assert return_ROT13_object.encode_decode(input) == expected


"""def test_should_return_proper_encoded_value_when_input_is_mixed_str(return_ROT13_object):
    input = 'ZZZZZ bbbb XXX ii o'
    expected = 'MMMMM oooo KKK vv b'
    assert return_ROT13_object.encode_decode(input) == expected"""
