from enum import Enum
from inspect import cleandoc


class Menu(Enum):
    def __str__(self):
        return self.value

    MAIN_MENU: str = cleandoc(
        """
        Please select encoding method:
        1. ROT13
        2. ROT47
        3. Exit program
        >>>
        """
    )

    INPUT_MENU: str = cleandoc(
        """Please select input method:
        1. Keyboard
        2. File
        3. Return to main menu
        >>>
        """
    )

    OUTPUT_MENU: str = cleandoc(
        """
        Please select output target:
        1. Screen
        2. File
        3. Return to main menu
        >>>
        """
    )
