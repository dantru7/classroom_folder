import final

gen = final.init("SPb", "Russia", ["La", "Lala"])

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))


@final.decor("test")
def a(x):
    print(x)
