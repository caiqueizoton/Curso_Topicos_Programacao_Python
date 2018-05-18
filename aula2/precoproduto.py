#Exerc 1 precço loja Caique

x=float(input('Digite o primeiro valor: '))
y=float(input('Digite o segundo valor: '))

multresult=x * y
somaresult=x + y

op = input('Escolha entre mult/soma: ')
if op == 'mult':
    print (multresult)
elif op == 'soma':
    print (somaresult)
