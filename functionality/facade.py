from functionality.cipher import ROT13


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

    def __init__(self):
        self.cipher = {"ROT13": ROT13, "ROT47": "ROT47"}
        self.input_ = {"keyboard": "IOReader", "file": "FileHandler"}

    def user_request_handler(self):
        """Perform action depending on user input"""
        print(Manager.app_name)
        main_menu_choice: int = int(input(Manager.main_menu))
        if main_menu_choice in [1, 2]:
            input_menu_choice = int(input(Manager.input_menu))
        else:
            print("Closing app...")
            return

        match (main_menu_choice, input_menu_choice):
            case (1, 1):
                print("ROT13 -> Keyboard")
            case (1, 2):
                print("ROT13 -> File")
            case (1, 3):
                print("Returning")
            case (2, 1):
                print("ROT47 -> Keyboard")
            case (2, 2):
                print("ROT47 -> File")
            case (2, 3):
                print("Returning")
            case _:
                print("Something went wrong...")
