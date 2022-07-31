from functionality.filehandler import FileHandler
from functionality.cipher import ROT13
from functionality.ioreader import IOReader
from typing import Union


class Manager:
    """Manager class implementing facade structural pattern"""

    app_name: str = "Cipher app."

    main_menu: str = (
        "Please select encoding method:\n"
        "1. ROT13\n"
        "2. ROT47\n"
        "3. Exit program\n"
        ">>> "
    )

    input_menu: str = (
        "Please select input method:\n"
        "1. Keyboard\n"
        "2. File\n"
        "3. Return to main menu\n"
        ">>> "
    )

    output_menu: str = (
        "Please select output target:\n"
        "1. Screen\n"
        "2. File\n"
        "3. Return to main menu\n"
        ">>> "
    )

    def __init__(self):
        self.cipher = {"ROT13": ROT13, "ROT47": "ROT47"}
        self.input = {"keyboard": IOReader, "file": FileHandler}
        self.output = {"screen": IOReader, "file": FileHandler}

    def cipher_factory(self, cipher_key: str) -> ROT13:
        return self.cipher.get(cipher_key)()

    def input_factory(self, input_key: str) -> Union[IOReader, FileHandler]:
        return self.input.get(input_key)()

    def output_factory(self, output_key: str) -> Union[IOReader, FileHandler]:
        return self.output.get(output_key)()

    def execute_case(self, cipher_: str, input_: str, output_: str):
        """Execute actions basing on passed arguments(case): cipher, input and output type"""
        cipher_: ROT13 = self.cipher_factory(cipher_)
        input_: Union[IOReader, FileHandler] = self.input_factory(input_)
        output_: Union[IOReader, FileHandler] = self.output_factory(output_)

        output_.write(cipher_.encode(input_.read()))

    def user_request_handler(self):
        """Perform action depending on user input"""
        print(Manager.app_name)
        main_menu_choice: int = int(input(Manager.main_menu))
        if main_menu_choice in [1, 2]:
            input_menu_choice = int(input(Manager.input_menu))
            if input_menu_choice in [1, 2]:
                output_menu_choice = int(input(Manager.output_menu))
        else:
            print("Closing app...")
            return

        match (main_menu_choice, input_menu_choice, output_menu_choice):
            case (1, 1, 1):
                print("ROT13 -> Keyboard -> Screen")
                self.execute_case("ROT13", "keyboard", "screen")
            case (1, 1, 2):
                print("ROT13 -> Keyboard -> File")
                self.execute_case("ROT13", "keyboard", "file")

            case (1, 2, 1):
                print("Rot13 -> File -> Screen")

            case (1, 2, 2):
                print("Rot13 -> File -> File")

            case _:
                print("Something went wrong...")


ex = Manager()
ex.user_request_handler()
