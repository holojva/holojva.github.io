from random import randint
class Potion :
    def __init__(self, name, quality) :
        self.name = name
        self.quality = quality
    def __str__(self) :
        return f"This potion named: {self.name}"
    def get_q(self) :
        return self.quality
    def get_n(self) :
        return self.name
    def __add__(self, other) :
        self_len = len(self.name) // 2
        other_len = len(other.name) // 2
        new_name = self.name[:self_len] + other.name[other_len:]
        new_quality = (self.quality + other.quality) // 2
        return Potion(new_name, new_quality)
    def __sub__(self, other) :
        new_quality = other.quality - randint(1, 100)
        return Potion(self.name, new_quality)
    def __mul__(self, other) :
        new_quality = other.quality * randint(1, 20)
        return Potion(self.name, new_quality)
    def __div__(self, other) :
        new_quality = other.quality / randint(1, 20)
        return Potion(self.name, new_quality)
    def check_quality(self) :
        if self.quality > 75 :
            print("Potion is very good")
        elif self.quality > 50 :
            print("Potion is good")
        elif self.quality > 30 :
            print("Potion have medium quality")
        elif self.quality > 0 :
            print("Potion is bad, blue screen of die")

class QualityPotion(Potion) :
    def special(self) :
        return QualityPotion(self.name, self.quality + 20)
class NotQualityPotion(Potion) :
    def special(self) :
        return QualityPotion(self.name, self.quality - 20)
quality = randint(1, 100)
qPotion = QualityPotion("Steve Jobs' iPhone", quality)

# print(qPotion)
# print(qPotion.get_q())
# upgradePotion = qPotion.special()
# print(upgradePotion.get_q())
first = 0
second = 0
while True :
    inp = input("q for quality, n for non quality ")
    name = input("Name: ")
    if inp == "n" :
        quality = randint(1, 100)
        if first != 0 :
            second = NotQualityPotion(name, quality)
        else :
            first = NotQualityPotion(name, quality)
        
    else :
        quality = randint(1, 100)
        if first != 0 :
            second = QualityPotion(name, quality)
        else :
            first = QualityPotion(name, quality)
    if first != 0 and second != 0 :
        znak = input("Do you want + or - your potions? ")
        if znak == "-" :
            first = first - second
            second = 0
        else :
            first = first + second
            second = 0
        print(f"New potion: {first}")
    Potion.check_quality(first) 