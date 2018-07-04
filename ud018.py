# quiz selo
# criar um código onde retorna a quantidade de cada " moeda ", sendo que são 5 , 2 e 1
def stamps(n):
    #retorna o valor do 5
    a = (n / 5)
    # retorna o valor do 2
    b = (n % 5 / 2)
    # retorna o valor do 1
    c = ((n % 5)%2)
    return (a,b,c)

print(stamps(8))
