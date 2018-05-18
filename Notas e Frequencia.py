#Notas e Frequencia Caique
x=float(input('Digite a porcentagem de frequência do aluno: '))

if x < 75:
    print ("O aluno foi reprovado por falta")

elif x >= 75:
    print ("O aluno obteve frequência mínima")

    p1=float(input('Digite a nota da P1: '))
    p2=float(input('Digite a nota da P2: '))
    p3=float(input('Digite a nota da P3: '))

    media=(p1+p2+p3)/3

if media >= 7:
    print ("O aluno está aprovado")

elif media < 3:
    print("O aluno está reprovado por nota")

elif media < 7 and media >= 3:
    print ("O aluno está em prova final")

    pf=float(input('Digite a nota da pf: '))
    notafinal=(media+pf)/2

if notafinal >= 5:
    print ("O aluno está aprovado em média final com nota: ",notafinal, )

else:
    print ("O aluno está reprovado por nota")

