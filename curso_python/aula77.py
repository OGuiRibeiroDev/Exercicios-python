pessoa = {
    'nome': 'Guilherme Henrique',
    'sobrenome': 'Machado Ribeiro',
    'idade': '20',
    'altura': '1.80',
    'endereco': [{'rua': 'tal', 'numero': 222},
                 {'rua': 'rua coisa', 'numero': 233}],
}

chave = 'nome'

pessoa[chave] = 'Gui'

print(pessoa['nome'])

pessoa[chave] = 'maria'

del pessoa['sobrenome']
print(pessoa)