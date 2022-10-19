ALFABETO = 27
def positions(letra):
    for i in letra:
        print((ord(i) & ALFABETO), end =" ")
  
letra = input()
positions(letra)
    