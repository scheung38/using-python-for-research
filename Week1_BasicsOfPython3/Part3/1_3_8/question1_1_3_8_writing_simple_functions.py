def intersect(a, b):
    mylist = []
    for i in a:
        if i in b:
            mylist.append(i)
    return mylist


def intersect2(a, b):
    mylist = []
    [mylist.append(i) for i in a if i in b]
    return mylist

print(intersect([1, 2, 3], [3, 4, 5, 6, 7]))
print(intersect2([1, 2, 3, 4, 5], [3, 4, 5, 6, 7]))


def random_passwd(length):
    import random
    pw = str()
    for i in range(length):
        pw += random.choice('abcdefghijklmnopqrstuvwxyz' + '0123456789')
    return pw


print(random_passwd(50))