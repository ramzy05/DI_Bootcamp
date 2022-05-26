''' from anagam_checker import AnagramChecker

get_user_menu_choice =  lambda :(input("Menu:\n(x) Input a word\n(q) exit\n : ").lower())

def main():
  
  while True:
    try:
      user_choice = get_user_menu_choice()
      assert user_choice in ['x', 'q']
    except:
      print("\/nYou should choose 'x' option or q 'option' ");
    else:
      if user_choice == 'q':#user quits de game
        break
      else:
       pass '''

file = open("sowpods.txt")

str = file.read().splitlines()[:5]

print(type(str), str)


