""" ex1 """
import math
from random import Random


display_message = lambda : print('j\' ai appris le html')
display_message()
""" end ex1 """

""" ex2 """
favorite_book = lambda title: print("One of my favorite books is", title)
favorite_book("The black")
""" end ex2 """


""" ex3 """
describe_city = lambda city_name, country_name = 'Cameroon': print(city_name,'is in', country_name)
describe_city('yaounde')  

""" end ex3 """


""" ex4 """
def random(number):
  if number not in range(1, 101):
    print('Le nombre passé en parametre n\' pas dans l\interval [1-100]')
    return
    
  if number == Random.randint(1, 100):
    print('SUCCESS!!!!')

  else:
    print('You fail')
    
  return

random(2)
""" end ex4 """


""" ex """
""" end ex """

""" ex """
""" end ex """
""" ex """

""" end ex """

""" ex """
""" end ex """