a = [1, 2, 3]
b = [11, 22, 33]



def add(a, b):
    c = []
    print(dir(c))
    for num in a,b:
        c.append(num)

    return c

print(add(a, b))