# programa que gera a tabuada de multiplicação

base = int(input("Digite o número base da tabuada:  "))
mult = 10

while mult >= 0:
    print (f"O valor de {base} vezes {mult} é :{base*mult}")
    mult -= 1
