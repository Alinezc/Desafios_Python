"""" Saruman, o Branco, um grande mago da Terra-média, traiu os bons costumes e se filiou ao lorde do mal, 
Sauron. Sauron comanda a torre de Minas Morgul, que abriga um dos seus mais temidos servos, o Rei Bruxo de 
Angmar, um dos Nazgûl (antigos reis humanos que foram corrompidos pelos poderes dos anéis de Sauron). Saruman
comanda a torre de Orthanc, onde cria seus servos Uruk-hai, orcs mais terríveis que os convencionais. 
Para comunicação, eles utilizam as relíquias esféricas chamadas Palantír, que ficam no topo de suas torres.
A Terra-média avança cada vez mais em tecnologia, muito impulsionada pelas guerras que a acometem diariamente.
Um dos problemas que tem atrapalhado sua população é a Interferência de Comunicação Mágica (ICM).
Os estudiosos de Minas Tirith, grande cidadela de Gondor, concluíram que para calcular o ICM para Palantír’s,
basta dividir a distância entre os dois Palantír’s, pela soma do diâmetro dos mesmos. Gandalf, o Cinza, chegou 
a questionar essa conclusão, alegando que ela não fazia muito sentido, mas ele mesmo concluiu que dar sentido
às coisas não faz sentido.Saruman e Sauron precisam de uma comunicação estável, pois têm medo que Frodo e 
seus amigos consigam atrapalhar seus planos, portanto, querem saber quanto de ICM há na comunicação de seus 
Palantír’s, para que saibam quanto de magia devem empregar na comunicação."""

print("Inserir a distância entre os Palantír:")
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
    else:
        print("Erro!")

print(f"O valor é total: {total:0.2f}")
