from functionality.filehandler import *
from datetime import datetime

FILEHANDLER_INPUT_TEST_FILE: str = "filehandler_test_files/input_test_file"
FILEHANDLER_OUTPUT_TEST_FILE: str = "filehandler_test_files/output_test_file"


class RWFile:
    """Class associating read/write file methods for testing FileHandler module"""

    @staticmethod
    def write_test_file(text: str):
        with open(FILEHANDLER_INPUT_TEST_FILE, "w") as f:
            f.writelines(text)

    @staticmethod
    def read_test_file(path_: str):
        output: str
        with open(path_, "r") as f:
            return f.read()


def test_read_from_file(mocker):
    expected = "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
    RWFile.write_test_file(expected)

    def get_file_name(obj: FileHandler):
        obj.file_name = FILEHANDLER_INPUT_TEST_FILE

    mocker.patch("functionality.filehandler.FileHandler.get_file_name", get_file_name)

    assert FileHandler().read() == expected


def test_write_to_file(mocker):
    mocker.patch(
        "functionality.filehandler.FileHandler.create_output_files_dir", return_value=""
    )
    output_test_path: str = FILEHANDLER_OUTPUT_TEST_FILE + datetime.now().strftime(
        "_%d_%m_%Y_%H_%M_%S"
    )

    def get_file_name(obj: FileHandler):
        obj.file_name = output_test_path

    mocker.patch("functionality.filehandler.FileHandler.get_file_name", get_file_name)

    expected = (
        "{'Cipher type': 'cipher_type', "
        "'Encoded text:': 'encoded_text', "
        "'Decoded text:': 'decoded_text'}\n"
    )

    FileHandler().write(
        cipher_type="cipher_type",
        decoded_text="decoded_text",
        encoded_text="encoded_text",
    )

    assert expected == RWFile.read_test_file(output_test_path)
