from functionality.filehandler import FileHandler
from functionality.cipher import ROT13, ROT47
from functionality.ioreader import IOReader
from typing import Union
from os.path import exists
from .menu import Menu
from typing import Any


# TODO Buffer -> Usuwanie go po zapisaniu, zapisywanie buffer do jsona,
class Manager:
    """Manager class implementing facade structural pattern"""

    MENU_PROMPT: str = "Entered value must be in range 1-3"

    app_name: str = "Cipher app."

    def __init__(self):
        self.cipher = {"ROT13": ROT13, "ROT47": ROT47}
        self.input = {"keyboard": IOReader, "file": FileHandler}
        self.output = {"screen": IOReader, "file": FileHandler}
        self.running = True
        self.exit = False
        self.buffer: list[list[Any]] = []

    def end_app(self) -> None:
        self.running = False

    def cipher_factory(self, cipher_key: str) -> Union[ROT13, ROT47]:
        """Return cipher object(ROT13/ROT48) based on passed str"""
        return self.cipher.get(cipher_key)()

    def input_factory(self, input_key: str) -> Union[IOReader, FileHandler]:
        """Return input object(IOReader/FileHandler) based on passed str"""
        return self.input.get(input_key)()

    def output_factory(self, output_key: str) -> Union[IOReader, FileHandler]:
        """Return output object(IOReader/FileHandler) based on passed str"""
        return self.output.get(output_key)()

    def execute_case(self, cipher_: str, input_: str, output_: str) -> None:
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

        encoded_decoded_text: str = cipher_.encode_decode(input_text)
        output_.write(encoded_decoded_text, input_text, cipher_.cipher_type)

        if output_ != "file":
            self.buffer.append([encoded_decoded_text, input_text, cipher_.cipher_type])

    def print_menu(self) -> Union[None, tuple, ValueError]:
        """Prints user menu and returns given choice in form of tuple"""
        print(Manager.app_name)

        while True:
            try:
                main_menu_choice: int = int(input(Menu.MAIN_MENU))

                while main_menu_choice not in [1, 2, 3]:
                    print(Manager.MENU_PROMPT)
                    main_menu_choice = int(input(Menu.MAIN_MENU))

                if main_menu_choice == 3:
                    print("Closing app...")
                    self.running = False
                    return -1, -1, -1

                input_menu_choice: int = int(input(Menu.INPUT_MENU))
                while input_menu_choice not in [1, 2, 3]:
                    print(Manager.MENU_PROMPT)
                    input_menu_choice = int(input(Menu.INPUT_MENU))

                if input_menu_choice == 3:
                    continue

                output_menu_choice: int = int(input(Menu.OUTPUT_MENU))
                while output_menu_choice not in [1, 2, 3]:
                    print(Manager.MENU_PROMPT)
                    output_menu_choice = int(input(Menu.OUTPUT_MENU))

                if output_menu_choice == 3:
                    continue

            except ValueError:
                print(
                    "Input must corresponds to given options (1-3)!\nReturning to main menu..."
                )
                continue

            return main_menu_choice, input_menu_choice, output_menu_choice

    def user_request_handler(self) -> [None, FileNotFoundError, ValueError]:
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

    def run_app(self):
        while self.running:
            try:
                self.exit = self.user_request_handler()
                if self.exit:
                    break
                continue_: str = input("Continue?(y/n):\n>>> ")
                if continue_ == "n":
                    if self.buffer:
                        dump_unsaved: str = input(
                            f"You have {len(self.buffer)} unsaved results. "
                            f"Do you want to save them to file? (y/n): "
                        )
                        if dump_unsaved == "y":
                            dump_file_handler = FileHandler("app_buffer")
                            for item in self.buffer:
                                dump_file_handler.write(item[0], item[1], item[2])
                    print("Closing app...")
                    self.running = False
            except (FileNotFoundError, ValueError, IsADirectoryError) as e:
                print(str(e), "Returning to main menu...", sep="\n")
                continue
