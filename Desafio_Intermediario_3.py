salario = int(input())

if (salario <= 600.00):
    reajuste = 0.17

elif(salario <= 900.00):
    reajuste = 0.13

elif (salario <= 1500.00):
    reajuste = 0.12

elif (salario <= 2000.00):
    reajuste = 0.10

else:
    reajuste = 0.05

percentual = reajuste * 100
novo_salario = salario * (1 + reajuste)


print(
    f"Novo salario: {novo_salario:.2f} Reajuste ganho: {novo_salario - salario:.2f} Em percentual: {percentual:.0f} %")
