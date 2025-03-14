def soma(a, b):
    return a + b

def divisao(a, b):
    return a / b

def multiplicacao(a, b):
    return a * b

def subtracao(a, b):
    return a - b

print('Digite 1 para função soma')
print('Digite 2 para função subtração')
print('Digite 3 para função multiplicaçao')
print('Digite 4 para função divisão')
operacao = int(input('Qual opção você deseja: '))

match operacao:
    case 1:
        a, b = map(float, input('Digite os dois números que deseja somar:').split())
        resultado = soma(a,b)
        print(f'O resultado da soma é: {resultado}')
    case 2: 
        a, b = map(float, input('Digite os dois números que desejar subtrair:').split())
        resultado = subtracao(a,b)
        print(f'O resultado da subtração é: {resultado}')
    case 3:
        a, b = map(float, input('Digite os dois números que deseja multiplicar:').split())
        resultado = multiplicacao(a,b)
        print(f'O resultado da multiplicação é: {resultado}')
    case 4:
        a, b = map(float, input('Digite os dois números que deseja dividir:').split())
        resultado = divisao(a,b)
        print(f'O resultado da divisão é: {resultado}')
    case _:
        print('Operação inválida')
