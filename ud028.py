# usando o index
def find_element(x,y):
    if (y in x):
        return x.index(y)
    else:
        return -1

# outra alternativa

def find_element(x,y):
    if y not in x:
        return -1
    else:
        return x.index(y)

print(find_element([1,2,3],3))

print(find_element(['alpha','beta'],'gamma'))