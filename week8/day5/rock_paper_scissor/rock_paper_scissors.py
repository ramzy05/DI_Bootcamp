
from  game import Game

get_user_menu_choice =  lambda :(input("Menu:\n(x) Play game\n(q) Show scores and exit\n : ").lower())

def print_results(results):
  print('Game Results:')
  for key,val in results.items():
    print(f" You {key} {val} times")
  
  print("\n")


def main():

  while True:
    try:
      user_choice = get_user_menu_choice()
      assert user_choice in ['x', 'q']
    except:
      print("\nYou should choose 'x' option or q 'option' ");
    else:
      if user_choice == 'q':#user quits de game
        break
      else:
        if Game.results == { 'win': 0,'loss': 0,'draw': 0}:
          game = Game()
        Game.results[game.play()] += 1#increment element
 


  """ Game.results = {key:int(val/2) for key,val in Game.results.items()} """
  print_results(Game.results)
  print('End of the game')

main()