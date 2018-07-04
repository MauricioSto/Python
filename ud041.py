#escopo variavel
def word_count(document, search_term):
    """ Contar quantas vezes search_term aparece no documento. """
    words = document.split()
    answer = 0
    for word in words:
        if word == search_term:
            answer += 1
    return answer

def nearest_square(limit):
    """ Encontre o maior número quadrado menor que limit. """
    answer = 0
    while (answer+1)**2 < limit:
        answer += 1
    return answer**2

egg_count = 0

def buy_eggs():
    egg_count += 12 # comprar uma dúzia de ovos

buy_eggs()