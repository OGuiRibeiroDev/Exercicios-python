#try, except, else e finally
try:
    print('Abrir Arquivo')
    8/0

except ZeroDivisionError:
    print('DIVIDIU ZERO')

except IndexError:
    print('IndexError')

except (NameError, ImportError):
    print('NameError, ImporError')

else:
    print('Não houve erros')

finally:
    print('Fechar Arquivo')