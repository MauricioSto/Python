def bigger(a, b):
    if a > b:
        return a
    else:
        return b

def biggest(a, b, c):
    return bigger(a, bigger(b, c))

def median(a, b, c):
    big = biggest(a,b,c)
    if big == a:
        return bigger(b, c)
    if big == b:
        return bigger(a,c)
    else:
        return bigger(a,b)






print(median(1, 3, 2))
print(median(1, 2, 3))
print(median(3, 2, 1))
print(median(2, 3, 1))
print(median(2, 1, 3))
print(median(3, 1, 2))
print(median(3, 2, 3))

