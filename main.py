def sum (o):
    a = 0
    for i in range(o):
        if i % 2 == 0:
            a += i
    if o < 0:
        return a * - 1
    else:
        return a