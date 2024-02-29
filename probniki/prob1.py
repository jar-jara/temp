from random import *


class Carta():
    def __init__(self, health, armor, man, reputation):
        self.health = health
        self.armor = armor
        self.man = man
        self.reputation = reputation
    
    def print_info(self):
        print('Здоровье:', self.health)
        print('Броня:', self.armor)
        print('Человек:', self.man)
        print('Репутация:', self.reputation)

cards = []

karta1 = Carta('100', '25', '3', '20')
karta2 = Carta('85', '10', '1', '30')
karta3 = Carta('90', '20', '5', '10')
karta4 = Carta('80', '15', '4', '25')

cards.append(karta1)
cards.append(karta2)
cards.append(karta3)
cards.append(karta4)

print(cards)



#choise = randint(cards[0, 4])
#print(choise)