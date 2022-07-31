class IOReader:
    """IOReader class"""

    def io_read(self) -> str:
        """Read data from io stream and return it in form of str"""
        output: str = input("Please enter text:\n>>> ")

        return output

    def io_write(self, text: str) -> None:
        """Print passed data to CLI"""
        print(text)
