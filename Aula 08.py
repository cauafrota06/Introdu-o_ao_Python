#import datetime as dt

#entradaNome = input('Digite seu nome: ')

#print(f'Seu nome é {entradaNome}, e agora é: {dt.datetime.now().time()}')

umaVariavel = 10
print(f'{umaVariavel} e {type(umaVariavel)}')

umaVariavel = "Hello Word"
print(f'{umaVariavel} e {type(umaVariavel)}')

umaVariavel =10.5
print(f'{umaVariavel} e {type(umaVariavel)}')

umaVariavel = True
print(f'{umaVariavel} e {type(umaVariavel)}')

umaVariavel = None
print(f'{umaVariavel} e {type(umaVariavel)}')

#Type Hint

variavelNumero: int = 10
variavelFloat: float = 3.14
variavelString = str = "Hello World"
variavelBoolean: bool = False

#INPUT

numeroA = int(input('Digite um número:'))
numeroB = int(input('Digite outro número:'))
print(f'A soma é {numeroA + numeroB}')