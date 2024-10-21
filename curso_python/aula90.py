#Generator Expression, Iterables e Iterators em Python
import sys


iterable = ['Eu', 'Tenho', '__iter__']
iterator = iter(iterable)

generator = (n for n in range(1000000))
lista = [n for n in range(1000000)]

print(sys.getsizeof(lista))
print(sys.getsizeof(generator))

for n in generator:
    print(n)