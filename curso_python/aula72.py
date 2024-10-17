def multiplicar(*args):
    total = 1
    for numero in args:
        total *= numero
    return total

def par_impar(numero):
    multiplo_2 =  numero % 2 == 0
    if multiplo_2:
        return f'{numero} é par'
    else:
        return f'{numero} é impar'

multiplicacao = multiplicar(1,2,3,4,5)
print(multiplicacao)

print(par_impar(3))
print(par_impar(2))