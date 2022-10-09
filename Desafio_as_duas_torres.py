entrada = input().split(" ")

distancia = int(entrada[0])
diametro1 = int(entrada[1])
diametro2 = int(entrada[2])

if distancia > 0 and distancia < 10000:
    if diametro1 > 0 and diametro2 < 100:
        total = distancia/(diametro1+diametro2)
        print(f" {total:0.2f}")

""" print("Inserir a distância entre os Palantír:")
total_distancia = int(input())
#distancia_total = int(total)

print("Inserir o diâmetro do Palantír de Sauron:")
sauron = int(input())
#diametro_sauron = int(sauron)
print("Inserir o diâmetro do Palantír de Saruman:")
saruman = int(input())
#diametro_saruman = int(saruman)

if total_distancia > 0 and total_distancia < 10000:
    if sauron > 0 and saruman < 100:
        total = total_distancia/(sauron + saruman)
    else :
        print("Erro!")

print(f"O valor é total: {total:0.2f}")
 """
