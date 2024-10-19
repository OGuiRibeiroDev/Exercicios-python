#s1 = set('Guilherme')
#s1 = {'Guilherme', 1, 2, 3}

#s1 = set() #vazio
#s1 = {'Guilherme', 1, 2, 3} #com dados

#s2 = {1, 2, 3, 3, 3, 3, 1}

#l1 = [1, 2, 3, 3, 3, 3, 1]
#s1 = set(l1)
#l2 = list(s1)
#s1 = s1 = {1, 2, 3}

# print(3 in s1)
# print(4 in s1)

# for numero in s1:
#     print(numero)


# s1 = set()
# s1.add('Gui Ribeiro')
# s1.add(1)
# s1.update(('Hello world', 1, 1, 1))
# s1.update('Nome')
# s1.discard('N')
# s1.discard('Hello world')
# s1.clear()

# print(s1)


s1 = {1, 3, 4, 5}
s2 = {2, 4, 3, 6}

print('União de sets ')
s3 = s1 | s2
print(s3)

print('Intersecção')
s3 = s1 & s2
print(s3)

print('Diferença')
#Pega os itens do set da esquerda que só estão presentes no mesmo
s3 = s1 - s2
print(s3)

print('Diferença simétrica')
s3 = s1 ^ s2
print(s3)

# s4 = {'a', 'c', 'e'}
# s5 = {'b', 'd', 'f'}

# s6 = s4 | s5
# print(s6)