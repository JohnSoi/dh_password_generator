"""Модуль для работы с выводом в консоль"""

__author__: str = "Digital Horizons"


class ConsoleManager:
    """
    Менеджер для работы с консольным выводом

    :ivar _need_print: флаг, который показывает нужен ли ввод
    :type _need_print: bool
    :ivar _last_line_length: последняя сохраненная строка вывода в консоль без очистки
    :type _last_line_length: int
    """

    def __init__(self, need_print: bool = True) -> None:
        """
        Инициализация класса менеджера вывода в консоль

        :param need_print: флаг, который показывает нужен ли ввод
        :type need_print: bool
        """
        self._need_print: bool = need_print
        self._last_line_length: int = 0

    def clear_line(self) -> None:
        """
        Очищает текущую строку

        .. code-block:: python
            from console_manager import ConsoleManager

            console_manager: ConsoleManager = ConsoleManager()
            console_manager.permanent_print("Первая строка, которая не удаляется автоматически")
            console_manager.permanent_print("Вторая строка, которая не удаляется автоматически")
            console_manager.clear_line() # Очищает все выведенные до этого строки
        """
        print("\r" + " " * self._last_line_length, end="", flush=True)

    def dynamic_print(self, text: str) -> None:
        """
        Выводит текст, перезаписывая предыдущий

        :param text: текст сообщения для вывода
        :type text: str

        .. code-block:: python
            from console_manager import ConsoleManager

            console_manager: ConsoleManager = ConsoleManager()
            console_manager.dynamic_print("Первая строка")
            console_manager.dynamic_print("Вторая строка, которая удалит первую")
        """
        if not self._need_print:
            return

        self.clear_line()
        print(f"\r{text}", end="", flush=True)
        self._last_line_length = len(text)

    def permanent_print(self, text: str) -> None:
        """
        Выводит текст навсегда (переходит на новую строку)

        :param text: текст сообщения для вывода
        :type text: str

        .. code-block:: python
            from console_manager import ConsoleManager

            console_manager: ConsoleManager = ConsoleManager()
            console_manager.permanent_print("Первая строка, которая не удаляется автоматически")
            console_manager.permanent_print("Вторая строка, которая не удаляется автоматически")
        """
        if not self._need_print:
            return

        self.clear_line()
        print(text)
        self._last_line_length = 0
