import pytest
from functionality.facade import *


@pytest.fixture
def mock_file_path(mocker):
    mocker.patch(
        "functionality.filehandler.FileHandler.get_file_name", return_value="test"
    )


@pytest.fixture
def init_manager():
    return Manager()


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
