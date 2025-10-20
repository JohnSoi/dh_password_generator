from random import choice
from tokenize import group

from dh_password_generator.console_manager import ConsoleManager
from dh_password_generator.consts import Symbols, DefaultValueParams, Settings
from dh_password_generator.generator_params import GeneratorParams


class PasswordGenerator:
    def __init__(self) -> None:
        self._params: GeneratorParams = GeneratorParams()
        self._console_manager = ConsoleManager()

    def process(self) -> None:
        self._console_manager.permanent_print(
            f'Будет сгенерирован пароль из "{self._params.length}" символов из {", ".join(self._params.human_symbols_group)}'
        )
        password: str = self._generate()
        password_strong: str = self._get_password_strong(password)
        self._console_manager.permanent_print(f"Ваш пароль: {password}")
        self._console_manager.permanent_print(f"Сложность пароля: {password_strong}")

    def _generate(self) -> str:
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

    def _get_password_strong(self, password: str) -> str:
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
        while True:
            temp_group: str = choice(self._params.symbols_group)

            if used_groups.count(temp_group) >= (len(self._params.symbols_group) / 2 * (self._params.length / len(self._params.symbols_group))):
                continue

            used_groups.append(temp_group)

            return temp_group
