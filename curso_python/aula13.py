nome = "Guilherme Ribeiro"
altura = 1.80
peso = 85
imc = peso / (altura ** 2)

"f-strings"
linha_1 = f'{nome} tem {altura:.2f} de altura'
linha_2 = f'pesa {peso} e seu ICM é {imc:.2f}'

print(linha_1)
print(linha_2)