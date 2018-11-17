"""
def summator(arr):
    sum = 0
    for x in range(len(arr)):
        sum += x
    return sum


summator([x for x in range(10)])
"""


class SummatorError(Exception):
    pass


class NotAList(SummatorError):
    pass


class InvalidType(SummatorError):
    pass


"""
#Is it necessary to throw an exception? 
class EmptyList(SummatorError):
    pass
"""


def sum_(arr: list):
    if type(arr) != list:
        raise NotAList
    if len(arr) == 0:
        return 0 # to safe some time if list is empty
    sum1 = 0
    for x in arr:
        if type(x) != (int or float):
            raise InvalidType
        sum1 += x
    return sum1


def avg(arr: list):
    if type(arr) != list:
        raise NotAList
    if len(arr) == 0:
        return 0 # to prevent a division by zero
    sum1 = 0
    for x in arr:
        if type(x) != (int or float):
            raise InvalidType
        sum1 += x
    return sum1/len(arr)
