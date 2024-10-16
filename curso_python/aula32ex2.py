hora = input('Qual o horário atual? Insira da seguinte forma: xx.xx ')

try:
    hora_flo = float(hora)
    if 0.00 <= hora_flo <= 11.00:
        print('Bom dia!')
    elif 12.00 <= hora_flo <= 17.00:
        print('Bom tarde!')
    elif 18.00 <= hora_flo <= 23.00:
        print('Boa noite!')
    else:
        print('Horário inválido')

except ValueError:
    print('Entrada inválida. Por favor, insira o horário no formato correto.')
