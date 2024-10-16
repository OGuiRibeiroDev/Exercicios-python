nome = input('Qual o seu nome? ')
idade = input('Qual a sua idade? ')

if nome and idade:
    print(f'Seu nome é {nome}')
    print(f'Seu nome invertido é {nome[::-1]}')

    if ' ' in nome:
        print('Seu nome contém espaços')

    print(f'Seu nome tem', len(nome) - 1, 'letras')
    print(f'A primeira letra do seu nome é ', {nome[0]})
    print(f'A última letra do seu nome é ', {nome[-1]})
    
else:
    print('Desculpe, você deixou os campos vazios')