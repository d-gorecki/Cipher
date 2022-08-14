import pytest
from os import getcwd
from functionality.filehandler import *

FILEHANDLER_TEST_FILE: str = "filehandler_test_files/test_file"


@pytest.fixture
def return_filehandler_obj(mocker):
    def set_file_name(obj: FileHandler):
        obj.file_name = FILEHANDLER_TEST_FILE

    mocker.patch("functionality.filehandler.FileHandler.get_file_name", set_file_name)
    return FileHandler()


class RWFile:
    """Class associating read/write file methods for testing FileHandler module"""

    @staticmethod
    def write_test_file(text: str) -> str:
        with open(FILEHANDLER_TEST_FILE, "w") as f:
            f.writelines(text)

    @staticmethod
    def read_test_file():
        output: str
        with open(FILEHANDLER_TEST_FILE, "r") as f:
            output = f.readlines()
        return output


def test_read_from_file(return_filehandler_obj):
    expected = "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
    RWFile.write_test_file(expected)
    assert return_filehandler_obj.read() == expected


def test_write_to_file(return_filehandler_obj, mocker):
    mocker.patch(
        "functionality.filehandler.FileHandler.write.file_path", FILEHANDLER_TEST_FILE
    )

    cipher_type = "cipher_type"
    encoded_text = "encoded_text"
    decoded_text = "decoded_text"
    expected = str(
        {
            "Cipher type": cipher_type,
            "Encoded text:": encoded_text,
            "Decoded text:": decoded_text,
        }
    )

    return_filehandler_obj.write(decoded_text, encoded_text, cipher_type)

    assert RWFile.read_test_file() == expected
