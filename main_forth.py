import datetime
import time

"""
def decor(func):
    def wrap(*args, **kwargs):
        wrap.count += 1
        print(datetime.datetime.now())
        print("this function is called " + str(wrap.count) + " times")
        print("Name of the function is " + func.__name__)
        res = func(*args, **kwargs)
        return res
    wrap.count = 0
    return wrap


@decor
def f():
    time.sleep(1)

f()
f()
f()
"""

############################################
# first task: print evaluation time
#help(time.process_time())

"""
def decor(f):
    def wrap(*arg, **kwargs):
        start = time.perf_counter()
        res = f(*arg, **kwargs)
        print("Eval Time: " + str(time.perf_counter() - start))
        return res
    return wrap

@decor
def func():
    time.sleep(1)
"""

############################################
# second task: decor + cache

"""
def convert(arg, dict):
    res = list()
    for x in arg:
        res.append(x)
    for x in dict:
        res.append(x[0])
        res.append(x[1])

    return tuple(res)


def decor(f):
    def wrap(*arg, **kwargs):
        start = time.perf_counter()
        # res = 0
        arkw = convert(arg, kwargs)
        if len(wrap.dict) != 0:
            value = wrap.dict.get(arkw)
            if value is None:
                res = f(*arg, **kwargs)
            else:
                # wrap.dict[key] = value
                res = value
        else:
            res = f(*arg, **kwargs)
        wrap.dict.update({arkw: res})
        print("Eval Time: " + str(time.perf_counter() - start))
        print(wrap.dict)
        return res
    wrap.dict = {}
    return wrap


@decor
def func(a, b):
    time.sleep(1)
    return a + b


func(1, 2)

func(1, 2)
func(1, 3)
func(1, 3)
"""

# second task: decor + cache


def convert(arg, dict):
    res = list()
    for x in arg:
        res.append(x)
    for x in dict:
        res.append(x[0])
        res.append(x[1])

    return tuple(res)


def decor(f):
    def wrap(*arg, **kwargs):
        start = time.perf_counter()
        # res = 0
        arkw = convert(arg, kwargs)
        if len(wrap.dict) != 0:
            value = wrap.dict.get(arkw)
            if value is None:
                res = f(*arg, **kwargs)
            else:
                # wrap.dict[key] = value
                res = value
        else:
            res = f(*arg, **kwargs)
        wrap.dict.update({arkw: res})
        print("Eval Time: " + str(time.perf_counter() - start))
        print(wrap.dict)
        return res
    wrap.dict = {}
    return wrap


@decor
def fib1(a):
    if a == 1 or a == 2:
        return 1
    res = 0
    x1 = 1
    x2 = 1
    while a - 3 >= 0:
        res = x1 + x2
        x1 = x2
        x2 = res
        a -= 0
    return res


func(1, 2)

func(1, 2)
func(1, 3)
func(1, 3)


