""" from functools import reduce

def check_arguments(*args):
    return list(map(lambda x: x+x, args))

print(check_arguments(1, 2, 3, 23, 4))



def check_argumentsRed(*args):
    return reduce(lambda x, y: x+y , list(args))

print(check_arguments(1, 2, 3, 23, 4)) 

my_list = [2,3,1,2,"four",42,1,5,3,"imanumber"]

def sumList(liste):
  somme = 0
  for item in liste:
    try:
      somme += item

    except:
      continue
  
  print(somme)

sumList(my_list)"""

from functools import reduce

factoriel = lambda n: reduce(lambda x, y: x*y, range(1,n+1))

print(factoriel(4))

