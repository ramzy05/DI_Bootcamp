
class Character:
  def __init__(self, name, life = 20, attack = 10):
    self.name = str(name)
    self.life = life
    self.attack = attack


  def basic_attack(self, another_char):
    print(f"le Character {self.name} attaque Character {another_char.name}")
    another_char.life -= self.attack
    if another_char.life < 0:
      another_char.life = 0


class Druid(Character):
  def __init__(self, name, life =20 , attack = 10):
    super().__init__(name, life, attack)
    print(f"Creation of a new character({self.__class__.__name__}) called {self.name}")

  def meditate(self):
    self.life += 10
    self.attack -= 2
    print(f"{self.name} medite, sa vie augmente de 10, et l'attaque diminue de -2")

  def animal_help(self):
    self.attack += 5
    print(f"L'attaque du Druid {self.name} s'augmente de 5")

  def fight(self, another_char):
    another_char.life -= (0.75*self.life + 0.75*self.attack)
    print(f"le Druid {self.name} attaque le Character {another_char.name}")


class Warrior(Character):
  def __init__(self, name, life =20 , attack = 10):
    super().__init__(name, life, attack)
    print(f"Creation of a new character({self.__class__.__name__}) called {self.name}")

  def brawl(self, another_char):
    another_char.life -= self.attack*2
    self.life -= self.attack*0.5
    print(f"Warrior {self.attack} attaque Character {another_char.name} en prenant un coup sur sa vie")

  def train(self):
    self.life, self.attack = self.life + 2, self.attack + 2
    print(f"Warrior {self.name} s'entraine et sa vie et son attaque s'augmente de 2")

  def roar(self, another_char):
    another_char.attack  -= 3
    print(f"Warrior {self.name} attaque {another_char.name} et lui retranche 3 a sa vie")


class Mage(Character):
  def __init__(self, name, life =20 , attack = 10):
    super().__init__(name, life, attack)
    print(f"Creation of a new character({self.__class__.__name__}) called {self.name}")

  def curse(self, another_char):
    another_char.attack -=  2
    print(f"Mage {self.name} attaque {another_char.name} et lui retranche 2 a sa vie")
  
  def summon(self):
    self.attack += 3
    print(f"Mage {self.name} augmente son attaque de 3")

  def call_spell(self, another_char):
    another_char.life -= (self.attack/self.life)
    print(f"Mage {self.name} attaque {another_char.name} et lui retranche le produit de son attack et sa vie a sa vie(celle de l'autre character)")
 
      

first_char = Druid("a", 10, 5)
second_char = Warrior("t", 30, 10)
third_char = Mage("g", 15)

print(first_char.attack)

first_char.animal_help()

print(first_char.attack)

