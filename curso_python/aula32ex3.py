nome = input('Qual o seu primeiro nome? ')


if len(nome) <= 4:
    print('seu nome é curto')
elif 5 <= len(nome) <=6:
    print('Seu nome é normal')
else:
    print('Seu nome é muito grande')