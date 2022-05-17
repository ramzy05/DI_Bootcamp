#exo1
class Pets():
  def __init__(self, animals):
    self.animals = animals

  def walk(self):
    for animal in self.animals:
      print(animal.walk())

class Cat():
  is_lazy = True

  def __init__(self, name, age):
    self.name = name
    self.age = age

  def walk(self):
    return f'{self.name} is just walking around'

class Bengal(Cat):
  def sing(self, sounds):
    return f'{sounds}'

class Chartreux(Cat):
  def sing(self, sounds):
    return f'{sounds}'

#my code
class Feel(Cat):
  def sing(self, sounds):
    return f'{sounds}'

bengal_inst = Bengal('Beno', 2)
chart_inst = Bengal('Charly', 1)
feel_inst = Feel('Feeling', 3)

my_cats = [bengal_inst, chart_inst, feel_inst]

#my code


""" for cat in my_cats:
    print(cat.walk())

#end exo1

# exo2

class Dog:
  def __init__(self, name, age, weight):
    self.__name = name 
    self.__age = age
    self.__weight = weight

  def bark(self):
    return self.__name
  
  def run_speed(self):
    return self.__weight / self.__age*10

  def fight(self, other_dog):
    

#end exo2 """

liste = ['s', 'd']

import random
new_list = [random.randint(0, 10) for item in liste]

print(new_list)