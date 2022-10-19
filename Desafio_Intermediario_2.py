
while True:
    papapagaio = {"esquerda": "ingles", "direita": "frances",
                  "nenhuma": "portugues", "ambas": "caiu"}
    try:
        st = input()

        print(papapagaio[st])

    except EOFError:
        break
