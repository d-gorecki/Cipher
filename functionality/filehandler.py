class FileHandler:
    """File handler class"""

    def __init__(self):
        self.file_path = ""

    def get_file_path(self) -> None:
        """Get file name(path) from user"""
        self.file_path: str = input("Please enter file name(path): ")

    def read_file(self) -> str:
        """Read data from file and return it in form of str"""
        with open(self.file_path, mode="r") as f:
            output: str = "".join(f.readlines())

        return output

    def write_file(self, text: str) -> None:
        """Write passed data to file. Append data in case file does exist.
        Create new file in case passed file does not exist."""
        with open(self.file_path, mode="a") as f:
            f.writelines(text)
