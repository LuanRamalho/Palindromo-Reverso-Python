def result(palavra):
    palavra_min = palavra.lower() # A função lower retornar a palavra com letras minúsculas.
    palavra_invertida = palavra_min[::-1] # Retorna a palavra de trás para frente.
    if palavra_min == palavra_invertida:
        print("A palavra é palíndromo.")
    else:
        print("A palavra não é palíndromo.")
    print()
    print('Sua palavra: ', end='') # O comando end Faz a resposta ficar na mesma linha do anúncio da resposta, como se fosse só para continuar na mesma linha.
    print(palavra)
    print('Inversão: ', end='')
    print(palavra_invertida)


word=input('Digite uma palavra: ')
print(result(word))
