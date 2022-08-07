from abc import ABC, abstractmethod
import string


class Cipher(ABC):
    """Abstract base class for ROT13 and ROT47 subclasses"""

    LOWERCASE: str = string.ascii_lowercase
    UPPERCASE: str = string.ascii_uppercase

    @abstractmethod
    def encode_decode(self, input_text: str):
        raise NotImplementedError


class ROT13(Cipher):
    """ROT13 class implementing ROT13 algorithm."""

    def __init__(self):
        self.cipher_type: str = "ROT13"

    def encode_decode(self, input_text: str) -> str:
        """Return encoded/decoded text"""
        output_text: str = ""
        for char_ in input_text:
            if char_ in ROT13.LOWERCASE:
                output_text += ROT13.LOWERCASE[(ROT13.LOWERCASE.find(char_) + 13) % 26]
            elif char_ in ROT13.UPPERCASE:
                output_text += ROT13.UPPERCASE[(ROT13.UPPERCASE.find(char_) + 13) % 26]
            else:
                raise ValueError(
                    "ROT13 can encode only ASCII lower and uppercase letters."
                )

        return output_text
