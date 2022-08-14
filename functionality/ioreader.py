class IOReader:
    """IOReader class"""

    def read(self) -> str:
        """Read data from io stream and return it in form of str"""
        output: str = input("Please enter text:\n>>> ")

        return output

    def write(
        self, text: str, encdoded_text: str = None, cipher_type: str = None
    ) -> None:
        """Print passed data to CLI"""
        print(text)
