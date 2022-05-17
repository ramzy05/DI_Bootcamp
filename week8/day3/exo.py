""" 
class Door:
  def __init__(self):
    self.is_opened = ''
  
  def open_door(self):
    print('ouverture de la porte')

  def close_door(self):
    print('fermeture de la porte')
    self.is_opened = False

class BlockedDoor(Door):
  def __init__(self):
      super().__init__()
  
  def open_door(self):
    raise Exception('The blocked door cannot be open')
  
  def close_door(self):
    raise Exception('The blocked door cannot be close')
      


door = BlockedDoor()

door.close_door() """
__name__ = 'master'
print(__name__)