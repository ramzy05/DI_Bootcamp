""" class Cat:
  def __init__(self, name, age):
    self.name = name
    self.age = age

cat1 = Cat("Greg", 2)
cat2 = Cat("Miaou", 3)
cat3 = Cat("Tom", 6)
cats = [cat1, cat2, cat3]
def oldest_cat(liste_cat,*args):

  dico = {cat.age:cat.name for cat in liste_cat}
  maxAge = max(list(dico.keys()))

  print(f"The oldest cat is {dico[maxAge]}, and is {maxAge} years old")

oldest_cat(cats) """

""" class Dog:
  def __init__(self, name, height):
    self.name = name
    self.height = height
  
  def bark(self):
    print(f"{self.name} goes woof!")

  def jump(self):
    print(f'{self.name} jumps {self.height*2} cm high!')
  

davids_dog = Dog('Rex', 50)
print(f'name = {davids_dog.name}\nheight = {davids_dog.height}')
davids_dog.bark()
davids_dog.jump()

sarahs_dog = Dog('Teacup', 20)
print(f'name = {sarahs_dog.name}\nheight = {sarahs_dog.height}')
sarahs_dog.bark()
sarahs_dog.jump()

if sarahs_dog.height < davids_dog.height:
  print(f'{davids_dog.name} is bigger')
else:
  print(f'{sarahs_dog.name} is bigger') """
