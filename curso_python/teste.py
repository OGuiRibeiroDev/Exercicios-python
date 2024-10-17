for lista in [[1, 2, 3], [4, 5, 6], [7, 8, 9]]:
    for numero in lista:
        escolha = input('Deseja prosseguir? (Digite 1 para sim ou qualquer outro valor para parar): ')
        if escolha == '1':  
            print(numero)
        else:
            break
