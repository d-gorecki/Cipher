from functionality.filehandler import *
from datetime import datetime
from json import dump

FILEHANDLER_INPUT_TEST_FILE: str = "test/filehandler_test_files/input_test_file"


class RWFile:
    """Class associating read/write file methods for testing FileHandler module"""

    @staticmethod
    def write_test_file(text: str) -> None:
        with open(FILEHANDLER_INPUT_TEST_FILE, "w") as f:
            f.writelines(text)

    @staticmethod
    def read_test_file(path_: str) -> str:
        output: str
        with open(path_, "r") as f:
            return f.read()


def test_read_from_file(mocker):
    expected = "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
    RWFile.write_test_file(expected)

    def get_file_name(obj: FileHandler) -> None:
        obj.file_name = FILEHANDLER_INPUT_TEST_FILE

    mocker.patch("functionality.filehandler.FileHandler.get_file_name", get_file_name)

    assert FileHandler().read() == expected
