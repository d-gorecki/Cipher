import pytest

from functionality.cipher import ROT13, ROT47


@pytest.fixture
def return_rot13_object() -> ROT13:
    return ROT13()


@pytest.fixture
def return_rot47_obj() -> ROT13:
    return ROT47


@pytest.mark.ROT13
def test_rot13_should_return_proper_decoded_value_when_input_is_lower_str(
    return_rot13_object,
):
    input_: str = "aaa"
    expected: str = "nnn"
    assert return_rot13_object.encode_decode(input_) == expected


@pytest.mark.ROT13
def test_rot13_should_return_proper_decoded_value_when_input_is_lower_str_with_spaces(
    return_rot13_object,
):
    input_: str = "aaa aaa"
    expected: str = "nnn nnn"
    assert return_rot13_object.encode_decode(input_) == expected


@pytest.mark.ROT13
@pytest.mark.parametrize("test_input", [("111"), ("!/.,"), ("ąężćó"), ("aaa123!")])
def test_rot13_expect_exception_when_passed_input_does_not_consist_of_ascii_letters(
    test_input,
):
    with pytest.raises(ValueError):
        ROT13().encode_decode(test_input)


@pytest.mark.ROT13
def test_rot13_should_return_proper_decoded_value_when_input_is_upper_str(
    return_rot13_object,
):
    input_: str = "ZZZZZ"
    expected: str = "MMMMM"
    assert return_rot13_object.encode_decode(input_) == expected


@pytest.mark.ROT13
def test_rot13_should_return_proper_decoded_value_when_input_is_upper_str_with_spaces(
    return_rot13_object,
):
    input_: str = "ZZZZZ ZZZZZ"
    expected: str = "MMMMM MMMMM"
    assert return_rot13_object.encode_decode(input_) == expected


@pytest.mark.ROT47_1
@pytest.mark.parametrize(
    "test_input, expected", [("!", "P"), ("~", "O"), ("Z", "+"), ("8", "g")]
)
def test_rot47_should_return_proper_decoded_value_when_input_is_in_range_33_126(
    test_input,
    expected,
):

    assert ROT47().encode_decode(test_input) == expected


@pytest.mark.ROT47
@pytest.mark.parametrize("test_input", [("ążćóź")])
def test_rot47_expect_exception_when_passed_input_is_NOT_in_range_33_126(
    test_input,
):
    with pytest.raises(ValueError):
        ROT47().encode_decode(test_input)
