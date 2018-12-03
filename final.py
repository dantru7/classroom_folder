"""
Module for testing
"""

import re
import json
import random
import string




def check(city: str, country: str, list_of_streets: list) -> bool:
    """
    Check if all arguments have correct type and data
    :param city: Name of the city
    :param country: Name of the country
    :param list_of_streets: List of the names of the streets
    :return: Returns true if everything is OK. Throws exceptions otherwise
    """
    if not isinstance(city, str) or not isinstance(country, str) or not isinstance(list_of_streets, (list, tuple)):
        raise TypeError

    a = re.compile('(?:[a-zA-Zа-яА-Я0-9][a-zA-Zа-яА-Я0-9 -]+)')
    if not a.fullmatch(city) or not a.fullmatch(country):
        raise ValueError
    for street in list_of_streets:
        if not isinstance(street, str):
            raise TypeError
        if not a.fullmatch(street):
            raise ValueError
    return True


def init(city: str, country: str, list_of_streets: list):
    """
    Initialize the module with given data
    :param city: Name of the city
    :param country: Name of the country
    :param list_of_streets: List of the names of the streets
    :return: Returns the generator of random addresses with ot without block
    """
    if check(city, country, list_of_streets):
        return get_sample_data(city, country, list_of_streets)


def init_json(path='', json_data=''):
    """
    Initialize the module with given data
    :param path: Path to file, which contains the data in json format
    :param json_data: data (city, country, list_of_streets) in json format
    :return: Returns the generator of random addresses with ot without block
    """
    if not path or not json:
        raise ValueError
    if path and json_data:
        raise ValueError
    data = {}
    if path:
        with open(path, 'r') as file:
            temp = file.read()
            data = json.loads(temp)
    elif json_data:
        data = json_data

    if data['city']:
        json_city = data['city']
    else:
        raise ValueError
    if data['country']:
        json_country = data['country']
    else:
        raise ValueError
    if data['list_of_streets']:
        json_list_of_streets = data['list_of_streets']
    else:
        raise ValueError

    if check(json_city, json_country, json_list_of_streets):
        return get_sample_data(json_city, json_country, json_list_of_streets)


def get_sample_data(city, country, list_of_streets) -> tuple:
    """
    Generator of random addresses with ot without block
    :param city: Name of the city
    :param country: Name of the country
    :param list_of_streets: List of the names of the streets
    :return: The tuple with random address with ot without block
    """
    while True:
        street_n = random.choice(list_of_streets)
        if random.choice([True, False]):
            char = ord('A') + random.randint(0, 25)
            yield (city, country, street_n, random.randint(1, 150), chr(char), random.randint(1, 1500))
        else:
            yield (city, country, street_n, random.randint(1, 150), random.randint(1, 1500))


def decor(flag_string=''):
    """
    Decorator of function. Checks if any of the arguments (string) equals flag_string
    :param flag_string: flag_string
    :return: Decoration function
    """
    def decor1(f):
        def wrap(*args, **kwargs):
            if flag_string and flag_string in args and flag_string in kwargs.values():
                print("{} has been called with following parameters:".format(f))
                print(args)
            elif not flag_string:
                print("flag_string is empty!")
            return f(*args)
        return wrap
    return decor1


if __name__ == "__main__":
    print("DON'T RUN ME!")
