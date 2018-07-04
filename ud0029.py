# unindo string sem repeti-las
def union(p,q):
    for e in q:
       if e not in p:
            p.append(e)

a = [1, 2, 3]
b = [2, 4, 6]
union(a,b)
print (a)
print (b)