import sys
from random import randint

count = 1
randomNumber = randint(1, 20)
print("Random number: ", randomNumber)
print('Guess random number between 1 - 20 \n')

while count <= 3:
    number = input('Podaj liczbę\n')
    count += 1
    if number == str(randomNumber):
        print("Wygrałeś!!!")
        sys.exit()
    else:
        print('\nPróbuj dalej')
        continue

print("!!!Przegrałeś tą gre!!!")
