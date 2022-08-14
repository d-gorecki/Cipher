import pytest

from functionality.cipher import ROT13, ROT47


@pytest.fixture
def return_ROT13_object():
    return ROT13()


@pytest.fixture
def return_ROT47_obj():
    return ROT47


@pytest.mark.ROT13
def test_should_return_proper_encoded_value_when_input_is_lower_str(
    return_ROT13_object,
):
    input_ = "aaa"
    expected = "nnn"
    assert return_ROT13_object.encode_decode(input_) == expected


@pytest.mark.ROT13
def test_should_return_proper_encoded_value_when_input_is_lower_str_with_spaces(
    return_ROT13_object,
):
    input_ = "aaa aaa"
    expected = "nnn nnn"
    assert return_ROT13_object.encode_decode(input_) == expected


@pytest.mark.ROT13
@pytest.mark.parametrize("test_input", [("111"), ("!/., "), ("ąężćó"), ("aaa123!")])
def test_expect_exception_when_passed_input_does_not_consist_of_ascii_letters(
    test_input,
):
    with pytest.raises(ValueError):
        ROT13().encode_decode(test_input)


@pytest.mark.ROT13
def test_should_return_proper_encoded_value_when_input_is_upper_str(
    return_ROT13_object,
):
    input_ = "ZZZZZ"
    expected = "MMMMM"
    assert return_ROT13_object.encode_decode(input_) == expected


@pytest.mark.ROT13
def test_should_return_proper_encoded_value_when_input_is_upper_str_with_spaces(
    return_ROT13_object,
):
    input_ = "ZZZZZ ZZZZZ"
    expected = "MMMMM MMMMM"
    assert return_ROT13_object.encode_decode(input_) == expected
