"""Модуль параметров генерации"""

__author__: str = "Digital Horizons"

from argparse import Namespace, ArgumentParser

from dh_password_generator.consts import (
    CONSOLE_ARGS_MAP,
    HUMAN_SYMBOLS_GROUP_NAME,
    Symbols,
    Settings,
    DefaultValueParams,
)


class GeneratorParams:
    """
    Параметры генератора паролей

    :ivar _length: длинна генерируемого пароля
    :type _length: int
    :ivar _symbols_group: список использованных групп символов
    :type _symbols_group: list[str]
    """

    def __init__(self) -> None:
        self._get_params()

    @property
    def length(self) -> int:
        """
        Длинна генерируемого пароля

        :return: длинна для генерации
        :rtype: int
        """
        return self._length

    @property
    def symbols_group(self) -> list[str]:
        """
        Группы символов для использования при генерации

        :return: группы символов для генерации
        :rtype: list[str]
        """
        return self._symbols_group

    @property
    def human_symbols_group(self) -> list[str]:
        """
        Человекочитаемые названия групп символов для использования при генерации

        :return: человекочитаемые группы символов для генерации
        :rtype: list[str]
        """
        return [HUMAN_SYMBOLS_GROUP_NAME[group] for group in self.symbols_group]

    def _get_params(self) -> None:
        """Получение параметров из парсера консольного ввода"""
        console_args: Namespace = self._get_console_arguments()
        self._length: int = self._get_length(console_args)
        self._symbols_group: list[str] = self._get_symbols_group(console_args)

    def _get_console_arguments(self) -> Namespace:
        """
        Получить аргументы консольного ввода

        :return: аргументы из консоли
        :rtype: Namespace
        """
        parser: ArgumentParser = self._get_args_parser()
        return parser.parse_args()

    @staticmethod
    def _get_args_parser() -> ArgumentParser:
        """
        Получить парсер консольных параметров

        :return: парсер консольных параметров
        :rtype: ArgumentParser
        """
        parser: ArgumentParser = ArgumentParser(
            description="Генерация пароля заданной длинны с использованием заданных групп "
            "символов и итоговой оценкой сложности"
        )

        for args in CONSOLE_ARGS_MAP:
            parser.add_argument(
                *args["flags"], # pyright:ignore
                type=args["type"], # pyright:ignore
                help=(args["help"]) # pyright:ignore
            )

        return parser

    @staticmethod
    def _get_length(console_args: Namespace) -> int:
        """
        Получение длинны из аргументов с проверкой ввода

        :param console_args: аргументы из консольного ввода
        :type console_args: Namespace
        :return: длинна пароля для генерации
        :rtype: int
        """
        length: int | None = console_args.length

        if length is None:
            length = DefaultValueParams.LENGTH

        if not length:
            raise ValueError("Нельзя сгенерировать пароль с 0 длинной")

        if Settings.MIN_PASSWORD_LENGTH > length > Settings.MAX_PASSWORD_LENGTH:
            raise ValueError(
                f'Длинна пароля должна быть в диапазоне от "{Settings.MIN_PASSWORD_LENGTH}" '
                f'до "{Settings.MAX_PASSWORD_LENGTH}" символов.'
            )

        return length

    @staticmethod
    def _get_symbols_group(console_args: Namespace) -> list[str]:
        """
        Получения списка групп символов для использования при генерации

        :param console_args: консольные аргументы
        :type console_args: Namespace
        :return: список групп символов
        :rtype: list[str]
        """
        symbols_group: list[str] = []

        for group in list(filter(lambda item: item.isupper(), dir(Symbols))):
            need_add_group: bool | None = getattr(console_args, group.lower())

            if need_add_group is None:
                need_add_group = getattr(DefaultValueParams, group)

            if need_add_group:
                symbols_group.append(group)

        if not symbols_group:
            raise ValueError("Нельзя сгенерировать пароль из ничего!")

        return symbols_group
