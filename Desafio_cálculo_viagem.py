valores = input().split(" ") 

tempo = int(valores[0])
velocidade_média = int(valores[1])

total = (tempo * velocidade_média)/12
print(f" {total:0.3f}")