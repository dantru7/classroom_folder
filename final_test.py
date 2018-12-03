"""
Module for testing
"""

import re


def init(city: str, country: str, list_of_streets: list) -> str:
    """

    """
    if not isinstance(city, str) or not isinstance(country, str) or not isinstance(list_of_streets, str, tuple):
        raise TypeError

    a = re.compile('(?:[a-zA-Zа-яА-Я -]+)')
    if not a.fullmatch(str) or a.fullmatch(country):
        raise InvalidValue
    for x in list_of_streets:
        if not a.fullmatch(x):
            raise ValueError

