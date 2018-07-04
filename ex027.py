# contagem de strings com iniciais em 'U'
def measure_udacity(list):
    result = 0
    for e in list:
        if e[0] == 'U':
            result = result + 1
    return result

# encontrar um elemento em uma lista

def find_element(x,y):
    p = -1
    i = 0
    for e in x:
        if e == y:
            p = i
            break
        i = i + 1
    return p

print(find_element([1,2,3],3))

print(find_element(['alpha','beta'],'gamma'))


# solução do professor
def find_element(x,y):
    p = 0
    while p < len(x):
        if x[p] == y:
            return p
        p = p + 1
    return -1


