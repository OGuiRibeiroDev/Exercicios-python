#Dictionary COmprehension e Set Comprehension
produto = {
    'nome': 'Caneta Azul',
    'preco': 1.5,
    'categoria': 'Escritório',
}


dc = {
    chave : valor
    if isinstance(valor, (int, float)) else valor.upper()
    for chave, valor 
    in produto.items()
    if chave != 'categoria'
}

lista = [
    ('a', 'valor a'),
    ('b', 'valor b'),
    ('c', 'valor c'),
]

dc = {
    chave: valor
    for chave, valor in lista
}

s1 = {2 ** i for i in range (10)}
print(s1)
