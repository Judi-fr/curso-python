def operar(a, b):
    return a + b, a - b


def main():
    resultado = operar(10, 5)
    print(resultado)
    print(type(resultado))


main()
