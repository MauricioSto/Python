def greatest(list):
    big = 0
    for e in list:
        if e > big:
            big = e
    return big



print (greatest([4,23,1]))
#>>> 23
print (greatest([]))
#>>> 0
