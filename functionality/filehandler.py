from os import getcwd, mkdir, path
from json import dump


class FileHandler:
    """File handler class"""

    def __init__(self, path_: str = None):
        self.file_name: str = ""
        self.get_file_name()

    def get_file_name(self) -> None:
        """Get file name(path) from user"""
        self.file_name: str = input("Please enter file name: ")

    def read(self) -> str:
        """Read data from file and return it in form of str"""
        with open(self.file_name, mode="r") as f:
            output: str = "".join(f.readlines())

        return output

    @staticmethod
    def create_output_files_dir() -> str:
        """Check if /files dir already exist in current dir. If not create /files dir. Return dir path"""
        file_path: str = getcwd() + "/files/"
        if not path.isdir(file_path):
            mkdir(file_path)

        return file_path

    def write(self, decoded_text: str, encoded_text: str, cipher_type: str) -> None:
        """Write passed data to file. Append data in case file does exist.
        Create new file in case passed file does not exist."""
        file_path: str = FileHandler.create_output_files_dir()

        with open(file_path + f"{self.file_name}.json", "a") as f:
            dump(
                {
                    "Cipher type": cipher_type,
                    "input text": encoded_text,
                    "encoded/decoded text": decoded_text,
                },
                f,
                indent=4,
            )
            f.write("\n")

    def dump_buffer(self, buffer: list[dict]):
        """Write passed data into file in json format. Used for unsaved buffer"""
        file_path: str = FileHandler.create_output_files_dir()
        with open(file_path + f"{self.file_name}.json", "w") as f:
            dump(buffer, f, indent=4)
