string = 'Guilherme'
metodo = 'upper'

if hasattr(string, metodo):
    print('Existe upper')
    print(getattr(string,metodo)())
else:
    print('Não existe o método', metodo)