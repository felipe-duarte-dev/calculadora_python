def soma(a, b):
    return a + b

a, b = map(float, input().split())
resultado = soma(a,b)
print(f'O resultado da soma é: {resultado}')