"""Модуль запуска генерации"""

__author__: str = "Digital Horizons"

from dh_password_generator.password_generator import PasswordGenerator

if __name__ == "__main__":
    PasswordGenerator().process()
