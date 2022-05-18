""" 
class User:
  def __init__(self, name, score = 0):
    self.name = name
    self.score = score

 """

import random



class Game:
  results ={
    'win': 0,
    'loss': 0,
    'draw': 0
  }

  def __init__(self):
      self.user_item = ''
      self.computer_item = ''
      self.__link = {
        'r':'rock',
        'p':'paper',
        's':'scissors'
      }
    

  def get_user_item(self):
    user_input = ''
    while True:
      try:
        user_input = input("\nSelect (r)ock, (p)aper, or (s)cissors: ").lower()
        assert user_input in ['r', 'p', 's']
      except:
        print("\nYou choice should be in one of elements of this set(r,p,s)")
      
      else:
        self.user_item = user_input
        """  self.options[self.user_choice] = 'User' """

        return self.user_item
        


  def get_computer_item(self):
    self.computer_item = random.choice(['r', 'p', 's'])
    """  self.options[self.computer_item] = 'Computer' """
    return self.computer_item

  def get_game_result(self, user_item, computer_item):
    option = [user_item, computer_item]
    #checking of the result
    
    if option in [['r','s'],['p','r'],['s', 'p']]:
      #user won
      """  Game.results['win'] += 1 """
      return 'win'

    elif option in [['r','r'],['p','p'],['s','s']]:
      #equality
      """ Game.results['draw'] += 1 """
      return 'draw'

    else:
      #user lost
      """ Game.results['loss'] += 1 """
      return 'loss'

  def play(self):
    user_item = self.get_user_item()
    computer_item =  self.get_computer_item()

    #print selected values
    print(f"\nYou have selected {self.__link[user_item]}.\nThe computer selected {self.__link[computer_item]}.\nYou {self.get_game_result(user_item, computer_item)}")
  
    return self.get_game_result(user_item, computer_item)#win/draw/loss/ 

