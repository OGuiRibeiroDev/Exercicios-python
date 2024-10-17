x = 1
y = 20

def escopo():
    global x
    x = 10

    def outrafuncao():
        x = 11
        y = 2
        print(x, y)

    outrafuncao()
    print(x)

print(x)
escopo()
print(x)