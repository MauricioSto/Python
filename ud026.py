spy = [0, 0, 7]
def replace_spy(spy):
    newspy = spy
    spy[2] = newspy[2]+1

replace_spy(spy)
print(spy)

#append ==> adiciona um item ao final da lista
# estrutura < list>.append(<element>)
#exemplo ==> spy.append(5)

# + ==> concatena duas listas
# <list> + <list>
#exemplo ==> [0,1] + [2,3] ==> [0,1,2,3]

# len ==> é lo mostra o numero de elementos na lista
# len(<list>)
#exemplo ==> len([0,1]) ==> 2

p = [1, 2]
p.append(3)
p = p + [4, 5]
print(len(p))

r = [1,2]
q = [3,4]
r.append(q)
print(len(r))

def print_all_ellements(p):
    i = 0
    while i < len(p):
        print(p[1])
        i = i + 1

def print_all_elements(p):
    for e in p:
        print(e)
