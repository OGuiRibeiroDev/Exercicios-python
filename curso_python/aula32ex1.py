numero = input('Digite um número inteiro: ')

if numero.isdigit():
    numero_int = int(numero)
    resto = numero_int % 2 == 0
    par_impar_texto = 'ímpar'

    if resto:
        par_impar_texto = 'par'

    print(f'O número {numero_int} é {par_impar_texto}')
else:
    print('Você não digitou um número inteiro')