"""def duplicar(numero):
    return numero * 2

numero_duplicado = duplicar(18)
print(numero_duplicado)


def triplicar(numero):
    return numero * 3

numero_triplicado = triplicar(18)
print(numero_triplicado)


def quadruplicar(numero):
    return numero * 4

numero_quadruplicado = quadruplicar(18)
print(numero_quadruplicado)"""

def criarMultiplicador(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar

duplicar = criarMultiplicador(2)
triplicar = criarMultiplicador(3)
quadruplicar = criarMultiplicador(4)

print(duplicar(2))
print(triplicar(4))
print(quadruplicar(6))