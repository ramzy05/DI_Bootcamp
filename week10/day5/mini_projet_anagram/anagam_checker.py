class AnagramChecker:
  def __init__(self, ) :
    self.words = '' 
    with open("sowpods.txt", "r", encoding='utf-8') as f:
       self.words = f.readlines()
  

a = AnagramChecker()
with open("sowpods.txt", "r", encoding='utf-8') as f:
       print(f.readlines())
