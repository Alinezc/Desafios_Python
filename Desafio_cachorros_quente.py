valores = input().split(" ") 

cachorros_quentes = float(valores[0])
participantes = float(valores[1])

if  cachorros_quentes >= 1 and participantes <= 1000:
    total = cachorros_quentes / participantes
    print(f" {total:0.2f}")