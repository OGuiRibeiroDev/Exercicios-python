p1 = {
    'nome': 'Guilherme Henrique',
    'sobrenome': 'Machado Ribeiro',
}

print(p1)
print(p1.get('nome', 'não existe'))
nome = p1.pop('nome')
print(nome)
ultima_chave = p1.popitem()
print(ultima_chave)

'''p1.update({
    'nome': 'novo nome',
    'idade': '30'
})'''

#p1.update(nome = 'novo valor', idade = 30)

tupla = ('nome', 'novo valor'), ('idade', 30)
lista = ['nome', 'novo valor'], ['idade', 30]
p1.update(tupla)

print(p1)