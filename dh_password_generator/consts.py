# pylint: disable=too-few-public-methods
"""Константы пакета генератора паролей"""

__author__: str = "Digital Horizons"

import string
from typing import Callable, LiteralString, Literal


class Settings:
    """
    Настройки генератора

    :cvar MIN_PASSWORD_LENGTH: минимальная длинна для генерации пароля
    :type MIN_PASSWORD_LENGTH: int
    :cvar MAX_PASSWORD_LENGTH: максимальная длинна для генерации пароля
    :type MAX_PASSWORD_LENGTH: int
    :cvar MIN_STRONG_PASSWORD_LENGTH: минимальная длинна пароля для повышенной сложности
    :type MIN_STRONG_PASSWORD_LENGTH: int
    """

    MIN_PASSWORD_LENGTH: int = 4
    MAX_PASSWORD_LENGTH: int = 20
    MIN_STRONG_PASSWORD_LENGTH: int = 12


class DefaultValueParams:
    """
    Дефолтные параметры для запуска генератора

    :cvar LENGTH: базовая длинна генерации пароля
    :type LENGTH: int
    :cvar ALPHABET: использовать буквы для генерации
    :type ALPHABET: bool
    :cvar DIGITS: использовать цифры для генерации
    :type DIGITS: bool
    :cvar SPECIAL: использовать спецсимволы для генерации
    :type SPECIAL: bool
    """

    LENGTH: int = 8
    ALPHABET: bool = True
    DIGITS: bool = True
    SPECIAL: bool = True


class Symbols:
    """
    Списки символом по группам

    :cvar ALPHABET: буквы для генерации
    :type ALPHABET: LiteralString
    :cvar DIGITS: цифры для генерации
    :type DIGITS: Literal['0123456789']
    :cvar SPECIAL: специальные символы для генерации
    :type SPECIAL: Literal['!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~']
    """

    ALPHABET: LiteralString = string.ascii_letters
    DIGITS: Literal['0123456789'] = string.digits
    SPECIAL: Literal['!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'] = string.punctuation


# Человекочитаемы названия для групп
HUMAN_SYMBOLS_GROUP_NAME: dict[str, str] = {
    "ALPHABET": "букв",
    "DIGITS": "цифр",
    "SPECIAL": "спец. символов",
}

# Карта консольных аргументов для парсера из консоли
CONSOLE_ARGS_MAP: list[dict[str, str | Callable | list[str]] | bool] = [
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
        "is_bool": True
    },
    {
        "flags": ["-d", "--digits"],
        "type": bool,
        "help": f"Использовать цифры в генерации пароля. "
        f"По умолчанию используется значение {DefaultValueParams.DIGITS}",
        "is_bool": True
    },
    {
        "flags": ["-s", "--special"],
        "type": bool,
        "help": f"Использовать спецсимволы в генерации пароля. "
        f"По умолчанию используется значение {DefaultValueParams.SPECIAL}",
        "is_bool": True
    },
]
