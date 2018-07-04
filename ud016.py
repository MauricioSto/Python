def loop (n):

# vai funcionar
    i = 0
    while i <= n:
        i = i + 1
        print(i)

 # vai funcionar
    i = 1
    while True:
        i = i * 2
        n = n + 1
        print(n)
        if i > n:
            break
 #nunca sei como fica
    while n != 1:
        if n % 2 == 0:
            n = n/2
            print (n)
        else:
            n = 3 * n + 1
            print(n)

loop (3)