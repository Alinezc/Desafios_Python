"""" Em 2012 foi alcançado um novo recorde mundial na famosa Competição de Cachorros-Quentes do Nathan: o 
campeão, Joey Chestnut, devorou 68 cachorros-quentes em dez minutos, um aumento incrível em relação aos 62 
sanduíches devorados pelo mesmo Chestnut em 2011.
O restaurante Nathan’s Famous Corporation, localizado no Brooklyn, NY, é o responsável pela competição. 
Eles produzem deliciosos cachorros-quentes, mundialmente famosos, mas quando o assunto é matemática eles não
são tão bons. Eles desejam ser listados no Livro de Recordes do Guinness, mas para isso devem preencher um 
formulário descrevendo os fatos básicos da competição. Em particular, eles devem informar o número médio de 
cachorros-quentes consumidos pelos participantes durante a competição.
.Dados o número total de cachorros-quentes consumidos e o número total de participantes na competição, 
você deve escrever um programa para determinar o número médio de cachorros-quentes consumidos pelos 
participantes."""

valores = input().split(" ") 

cachorros_quentes = float(valores[0])
participantes = float(valores[1])

if  cachorros_quentes >= 1 and participantes <= 1000:
    total = cachorros_quentes / participantes
    print(f" {total:0.2f}")