class Person() :
    def play(self) :
        print(f"{self.attack} attacks!")

class Mage(Person) :
    def __init__(self, name) :
        self.name = name
        self.attack = "Mage"
class Barbarian(Person) :
    def __init__(self, name) :
        self.name = name
        self.attack = "Mage"

b_n = input("Your barbarian name: ").lower()
m_n = input("Your mage name: ").lower()
b = Barbarian(b_n)
m = mage(m_n)

while True :
    inp = input("Mage or Barbarian?")
    if inp = "barbarian" :
        Barbarian.play()
    elif inp = "mage" :
        Mage.play()
    else :
        print("TYPE NORMAL NAME!")