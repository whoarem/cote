def false():
    print('getting false')
    return False


def true():
    print('getting true')
    return True


if true() and false():
    print(1)
print()

if false() and true():
    print(2)
print()

if true() and true():
    print(3)


a = set([1, 2, 3, 4])
b = set([3, 4, 5, 6])
print(a.intersection(b))
