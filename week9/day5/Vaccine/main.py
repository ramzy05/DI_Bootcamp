

class Human:
  next_id = 1
  def __init__(self, name, age, blood_type,priority = False):
    self.id_number = Human.next_id
    self.name = str(name)
    self.age = int(age)
    self.priority = priority
    self.blood_type = blood_type
    self.family = []
    Human.next_id += 1
  

  def add_family_member(self, person):
    self.family.append(person)
    person.family.append(self)

class Queue:
  humans = []
  def add_person(self, person):
    if person.age > 60 or person.priority:
      self.humans = [person] + self.humans
    else:
      self.humans += [person]

  def find_in_queue(self, person):
    """ on retourne None si person n'est pas dans
    la liste """
    for i in range(self.humans):
      if self.humans[i] is person:
        return i
      
    return None

  def swap(self, person1, person2):
    person1, person2 = person2, person1

  def get_next(self):
    if self.humans == []:
      return None
    next_human = list(self.humans[0])
    del  self.humans
    return next_human[0]
  
  def get_next_blood_type(self, blood_type):
    if self.humans == []:
      return None
    i = 0
    while i < len(self.humans):
      if self.humans[i].blood_type == blood_type:
        next_human = list(self.humans[0])
        del  self.humans
        return next_human
      i += 1
    return None

  def sort_by_age(self):
    sorted_humans = [human for human in self.humans if human.priority]
    sorted_humans += [human for human in self.humans if human.age > 60]
    sorted_humans += [human for human in self.humans if human.age <= 60]

  def rearange_queue(self):
    new_humans = list(self.humans)
    self.humans = []
    

liste = [2, 1]
del liste[0]
print(liste[0])