from abc import ABC
import string


class Cipher(ABC):
    """Abstract base class for ROT13 and ROT47 subclasses"""

    def encode(self, input_text: str):
        raise NotImplementedError


class ROT13(Cipher):
    """ROT13 class implementing ROT13 algorithm."""

    lowercase: str = string.ascii_lowercase
    uppercase: str = string.ascii_uppercase

    def encode(self, input_text: str) -> str:
        """Return encoded/decoded text"""
        output_text: str = ""
        for char_ in input_text:
            if char_ in ROT13.lowercase:
                output_text += ROT13.lowercase[(ROT13.lowercase.find(char_) + 13) % 26]
            elif char_ in ROT13.uppercase:
                output_text += ROT13.uppercase[(ROT13.uppercase.find(char_) + 13) % 26]
            else:
                raise ValueError(
                    "ROT13 can encode only ASCII lower and uppercase letters."
                )

        return output_text
