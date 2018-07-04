# imprimir uma caixa
def box(width, height, symbol):
    """Imprimir uma caixa composta de asteriscos ou algum outro caractere.

    width: Largura da caixa em caracteres, deve ser pelo menos 2
    height: Altura da caixa em linhas, deve ser pelo menos 2
    symbol: Uma única sequência de caracteres usada para desenhar as bordas da caixa
    """
    print(symbol * width) # imprimir a borda superior da caixa

    # print sides of box
    for _ in range(height-2):
        print(symbol + " " * (width-2) + symbol)

    print(symbol * width) # imprimir a borda inferior da caixa

#def box(width, height, symbol='*'):
box (7,5, '#')
