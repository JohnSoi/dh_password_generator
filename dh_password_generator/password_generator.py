# pylint: disable=too-few-public-methods
"""Модуль генератора паролей"""

__author__: str = "Digital Horizons"

from random import choice

from dh_password_generator.consts import Symbols, Settings
from dh_password_generator.console_manager import ConsoleManager
from dh_password_generator.generator_params import GeneratorParams


class PasswordGenerator:
    """
    Генератор паролей

    :ivar _params: параметры генератора из консоли
    :type _params: GeneratorParams
    :ivar _console_manager: консольный менеджер для вывода информации
    :type _console_manager: ConsoleManager
    """

    def __init__(self) -> None:
        self._params: GeneratorParams = GeneratorParams()
        self._console_manager = ConsoleManager()

    def process(self) -> None:
        """Основной метод запуска процесса генерации"""
        self._console_manager.permanent_print(
            f"Будет сгенерирован пароль из "
            f'"{self._params.length}" символов из '
            f'{", ".join(self._params.human_symbols_group)}'
        )
        password: str = self._generate()
        password_strong: str = self._get_password_strong()
        self._console_manager.permanent_print(f"Ваш пароль: {password}")
        self._console_manager.permanent_print(f"Сложность пароля: {password_strong}")

    def _generate(self) -> str:
        """
        Генерация пароля по заданным параметрам

        :return: сгенерированный пароль
        :rtype: str
        """
        used_groups: list[str] = []
        password: str = ""

        for _ in range(self._params.length):
            group_symbols: str = self._get_group(used_groups)
            symbols: list[str] = getattr(Symbols, group_symbols)
            symbol: str = choice(symbols)

            if group_symbols == "ALPHABET":
                if choice((True, False)):
                    symbol = symbol.upper()

            password += symbol

        return password

    def _get_password_strong(self) -> str:
        """
        Получение сложности сгенерированного пароля

        :return: сложность пароля в виде человекачитаемого текста
        :rtype: str
        """
        password_strong_cond: tuple[bool, ...] = (
            self._params.length >= Settings.MIN_STRONG_PASSWORD_LENGTH,
            len(self._params.symbols_group) > 1,
            len(self._params.symbols_group) > 2,
        )

        match password_strong_cond.count(True):
            case 1:
                return "Средняя"
            case 2:
                return "Высокая"
            case 3:
                return "Очень высокая"
            case _:
                return "Низкая"

    def _get_group(self, used_groups: list[str]) -> str:
        """
        Получение текущей группы для случайного выбора символов.
        Учитывает, что бы равномерно использовались все группы

        :param used_groups: список использованных групп
        :type used_groups: list[str]
        :return: группа символов для случайного выбора из нее
        :rtype: str
        """
        while True:
            temp_group: str = choice(self._params.symbols_group)
            if used_groups.count(temp_group) >= (self._params.length / len(self._params.symbols_group) + 1):
                continue

            used_groups.append(temp_group)

            return temp_group
