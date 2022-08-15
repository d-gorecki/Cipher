import io
import sys

import pytest
from functionality.facade import *


@pytest.fixture
def mock_file_path(mocker) -> None:
    mocker.patch(
        "functionality.filehandler.FileHandler.get_file_name", return_value="test"
    )


@pytest.fixture
def init_manager() -> Manager:
    return Manager()


@pytest.fixture
def mock_execute_case(mocker) -> None:
    mocker.patch("functionality.facade.Manager.execute_case", return_value="")


@pytest.mark.factory
@pytest.mark.parametrize("test_input, expected", [("ROT13", ROT13), ("ROT47", ROT47)])
def test_cipher_factory_should_return_proper_object(test_input, expected, init_manager):
    assert isinstance(init_manager.cipher_factory(test_input), expected)


@pytest.mark.factory
@pytest.mark.parametrize(
    "test_input, expected", [("keyboard", IOReader), ("file", FileHandler)]
)
def test_input_factory_should_return_proper_object(
    test_input, expected, mock_file_path, init_manager
):
    assert isinstance(init_manager.input_factory(test_input), expected)


@pytest.mark.factory
@pytest.mark.parametrize(
    "test_input, expected", [("file", FileHandler), ("screen", IOReader)]
)
def test_output_factory_should_return_proper_object(
    test_input, expected, mock_file_path, init_manager
):
    assert isinstance(init_manager.output_factory(test_input), expected)


@pytest.mark.execute_case
def test_execute_case_except_exception_when_input_file_doest_not_exist(
    init_manager, mock_file_path
):
    with pytest.raises(FileNotFoundError):
        init_manager.execute_case("ROT13", "file", "file")


@pytest.mark.user_request_handler
@pytest.mark.parametrize(
    "input_, expected",
    [
        ((1, 1, 1), "ROT13 -> Keyboard -> Screen"),
        ((1, 1, 2), "ROT13 -> Keyboard -> File"),
        ((1, 2, 1), "ROT13 -> File -> Screen"),
        ((1, 2, 2), "ROT13 -> File -> File"),
        ((2, 1, 1), "ROT47 -> Keyboard -> Screen"),
        ((2, 1, 2), "ROT47 -> Keyboard -> File"),
        ((2, 2, 1), "ROT47 -> File -> Screen"),
        ((2, 2, 2), "ROT47 -> File -> File"),
        ((-3, -3, 3), "Something went wrong..."),
    ],
)
def test_user_request_handler_should_execute_proper_case_for_given_inputs(
    mocker, capsys, input_, expected, init_manager, mock_execute_case
):

    mocker.patch("functionality.facade.Manager.print_menu", return_value=input_)
    init_manager.user_request_handler()
    captured = capsys.readouterr()

    assert captured.out == expected + "\n"
