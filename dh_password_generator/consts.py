import string
from typing import Callable


class Settings:
    MIN_PASSWORD_LENGTH: int = 4
    MAX_PASSWORD_LENGTH: int = 20
    MIN_STRONG_PASSWORD_LENGTH: int = 12


class DefaultValueParams:
    LENGTH: int = 8
    ALPHABET: bool = True
    DIGITS: bool = True
    SPECIAL: bool = True


class Symbols:
    ALPHABET: list[str] = string.ascii_letters
    DIGITS: list[str] = string.digits
    SPECIAL: list[str] = string.punctuation


HUMAN_SYMBOLS_GROUP_NAME: dict[str, str] = {
    "ALPHABET": "букв",
    "DIGITS": "цифр",
    "SPECIAL": "спец. символов"
}


CONSOLE_ARGS_MAP: list[dict[str, str | Callable | list[str]]] = [
    {
        "flags": ["-l", "--length"],
        "type": int,
        "help": f"Длинна генерируемого пароля. "
                f"По умолчанию используется значение {DefaultValueParams.LENGTH} символов",
    },
    {
        "flags": ["-a", "--alphabet"],
        "type": bool,
        "help": f"Использовать буквы в генерации пароля. "
                f"По умолчанию используется значение {DefaultValueParams.ALPHABET}",
    },
    {
        "flags": ["-d", "--digits"],
        "type": bool,
        "help": f"Использовать цифры в генерации пароля. "
                f"По умолчанию используется значение {DefaultValueParams.DIGITS}",
    },
    {
        "flags": ["-s", "--special"],
        "type": bool,
        "help": f"Использовать спецсимволы в генерации пароля. "
                f"По умолчанию используется значение {DefaultValueParams.SPECIAL}",
    },
]
