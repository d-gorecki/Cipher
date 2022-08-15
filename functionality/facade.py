from functionality.filehandler import FileHandler
from functionality.cipher import ROT13, ROT47
from functionality.ioreader import IOReader
from typing import Union
from os.path import exists
import logging

logging.basicConfig(level=logging.INFO, format="")


class Manager:
    """Manager class implementing facade structural pattern"""

    MENU_PROMPT: str = "Entered value must be in range 1-3"

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
        self.cipher = {"ROT13": ROT13, "ROT47": ROT47}
        self.input = {"keyboard": IOReader, "file": FileHandler}
        self.output = {"screen": IOReader, "file": FileHandler}
        self.running = True
        self.exit = False

    def end_app(self):
        self.running = False

    def cipher_factory(self, cipher_key: str) -> Union[ROT13, ROT47]:
        return self.cipher.get(cipher_key)()

    def input_factory(self, input_key: str) -> Union[IOReader, FileHandler]:
        return self.input.get(input_key)()

    def output_factory(self, output_key: str) -> Union[IOReader, FileHandler]:
        return self.output.get(output_key)()

    def execute_case(self, cipher_: str, input_: str, output_: str):
        """Execute actions basing on passed arguments(case): cipher, input and output type"""
        cipher_: Union[ROT13, ROT47] = self.cipher_factory(cipher_)

        if input_ == "file" and output_ == "file":
            print("# INPUT FILE")
            input_: FileHandler = self.input_factory(input_)
            input_text: str = input_.read()
            if not exists(input_.file_name):
                raise FileNotFoundError(
                    "No such file or directory!\nReturning to main menu..."
                )
            print("# OUTPUT FILE")
            output_: FileHandler = self.output_factory(output_)
        else:
            input_: Union[IOReader, FileHandler] = self.input_factory(input_)
            input_text: str = input_.read()
            output_: Union[IOReader, FileHandler] = self.output_factory(output_)

        output_.write(
            cipher_.encode_decode(input_text), input_text, cipher_.cipher_type
        )

    def print_menu(self) -> Union[None, tuple]:
        """Prints user menu and returns given choice in form of tuple"""
        print(Manager.app_name)

        while True:
            try:
                main_menu_choice: int = int(input(Manager.main_menu))

                while main_menu_choice not in [1, 2, 3]:
                    print(Manager.MENU_PROMPT)
                    main_menu_choice = int(input(Manager.main_menu))

                if main_menu_choice == 3:
                    print("Closing app...")
                    self.running = False
                    return -1, -1, -1

                input_menu_choice: int = int(input(Manager.input_menu))
                while input_menu_choice not in [1, 2, 3]:
                    print(Manager.MENU_PROMPT)
                    input_menu_choice = int(input(Manager.input_menu))

                if input_menu_choice == 3:
                    continue

                output_menu_choice: int = int(input(Manager.output_menu))
                while output_menu_choice not in [1, 2, 3]:
                    print(Manager.MENU_PROMPT)
                    output_menu_choice = int(input(Manager.input_menu))

                if output_menu_choice == 3:
                    continue

            except ValueError:
                logging.info(
                    "Input must corresponds to given options (1-3)!\nReturning to main menu..."
                )
                continue

            return main_menu_choice, input_menu_choice, output_menu_choice

    def user_request_handler(self):
        """Perform action depending on user input"""

        main_menu_choice, input_menu_choice, output_menu_choice = self.print_menu()

        match (main_menu_choice, input_menu_choice, output_menu_choice):
            case (-1, -1, -1):
                return True
            case (1, 1, 1):
                print("ROT13 -> Keyboard -> Screen")
                self.execute_case("ROT13", "keyboard", "screen")
            case (1, 1, 2):
                print("ROT13 -> Keyboard -> File")
                self.execute_case("ROT13", "keyboard", "file")
            case (1, 2, 1):
                print("ROT13 -> File -> Screen")
                self.execute_case("ROT13", "file", "screen")
            case (1, 2, 2):
                print("ROT13 -> File -> File")
                self.execute_case("ROT13", "file", "file")
            case (2, 1, 1):
                print("ROT47 -> Keyboard -> Screen")
                self.execute_case("ROT47", "keyboard", "screen")
            case (2, 1, 2):
                print("ROT47 -> Keyboard -> File")
                self.execute_case("ROT47", "keyboard", "file")
            case (2, 2, 1):
                print("ROT47 -> File -> Screen")
                self.execute_case("ROT47", "file", "screen")
            case (2, 2, 2):
                print("ROT47 -> File -> File")
                self.execute_case("ROT47", "file", "file")
            case _:
                print("Something went wrong...")
