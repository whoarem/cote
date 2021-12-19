import datetime
from pkg.foo import Foo
print(Foo)

print(datetime.datetime.now())

print([1, 2, 3][:0])
print([1, 2, 3][3:])
print([1, 2, 3][4:])
print([1, 2, 3][:3])
print([1, 2, 3][:4])

a = [1, 2, 3]

a.insert(5, 5)

print(a)
print(1+True)
print(divmod(5, 2))


class Foo:
    def __init__(self, name) -> None:
        self.name = name

    def speak(self):
        print('I am '+self.name)


class Bar(Foo):
    def __init__(self, name) -> None:
        super().__init__(name)

    def speak(self):
        print('You are '+self.name)


bar = Bar('John')
bar.speak()


def int_sum(*args):
    try:
        for n in args:
            print(n)
            sum += n
    except:
        print('error')
    return sum


print(int_sum(1))

print(int_sum(1, 2, 3))
