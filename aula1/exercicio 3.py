#exercicio 3

a=int(input("Digite o intervalo em segundos"))

minutagem=a//60

segundosf=a%60

hora=minutagem//60

minutos2=minutagem%60

print(f"O intervalo temporal em horas/minutos/segundos é:  {hora} h {minutos2} min {segundosf} seg")
