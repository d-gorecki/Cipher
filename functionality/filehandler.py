import os
from os import getcwd, mkdir, path, fsync


class FileHandler:
    """File handler class"""

    def __init__(self):
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

    def write(self, decoded_text: str, encoded_text: str, cipher_type: str) -> None:
        """Write passed data to file. Append data in case file does exist.
        Create new file in case passed file does not exist."""
        file_path: str = getcwd() + "/files"
        if not path.isdir(file_path):
            mkdir(file_path)
        with open(file_path + f"/{self.file_name}", "a") as f:
            # f.writelines(str({cipher_type: text}) + "\n")
            f.writelines(
                str(
                    {
                        "Cipher type": cipher_type,
                        "Encoded text:": encoded_text,
                        "Decoded text:": decoded_text,
                    }
                )
                + "\n"
            )
