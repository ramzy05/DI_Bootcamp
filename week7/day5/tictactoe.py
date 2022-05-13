

from operator import indexOf
from tabnanny import check


lastestPlayer = ''

players = [
  {
    'value': ' X ',
    'row': 0,
    'col':0,
    'name': 'playerX', 
  },
  {
    'value': ' O ',
    'row': 0,
    'col':0,
    'name': 'playerO', 
  }
]

idResponse = [
  '11',
  '12',
  '13',
  '21',
  '22',
  '23',
  '31',
  '32',
  '33'
]

resultat = [

  '*****************',
  ['*  ',' X ','|',' X ','|',' X ', '  *'],
  ['*  ','---','|','---','|','---','  *'],
  ['*  ','   ','|','   ','|','   ', '  *'],
  ['*  ','---','|','---','|','---','  *'],
  ['*  ','   ','|','   ','|','   ','  *'],
  '*****************'
]


def display_board():
  print('\nTIC TAC TOE')
  print(resultat[0])
  for i in range(1, len(resultat) -1):
    line = ''
    for j in range(len(resultat[i])):
      line += resultat[i][j]
      
    print(line)
  print(resultat[len(resultat)-1])
 
display_board()

def placePlayerChoice(player):
    
  if player['row'] != 1:
    if player['row'] != 3:
      player['row'] += 1
    else:
      player['row'] += 2

  line = resultat[player['row']]
  if player['col'] == 1:
    line[player['col']]= player['value']
  elif  player['col'] == 2:
    line[player['col']+1]= player['value']
  elif  player['col'] == 3:
    line[player['col']+2]= player['value']
    
def check_line(line):
  if line.count(' X ')== 3:
    print('PlayerX win')
    return
  elif line.count(' O ') == 3:
    print('PlayerO win')
    return

def check_win():
  list_to_check = resultat[1:len(resultat)-1]
  list_to_check.pop(1)#on enleve les lignes unitiles
  list_to_check.pop(2)#on enleve les lignes unitiles
  for i in range(len(list_to_check)):
    line = list(list_to_check[i])
    list_to_check[i].clear()
    #on retire les etoiles et les bars
    list_to_check[i] = [ j for j in line if j not in['*  ', '|', '  *']]
  print(list_to_check)

  #check les lignes
  check_line(list_to_check[0])
  """  for line in list_to_check:
    if line.count(' X ')== 3:
      print('PlayerX win')
      return
    elif line.count(' O ') == 3:
      print('PlayerO win')
      return """
  
  #check les colonnes:
  """on va creer une liste 
  pour transformer mes ligne colonne et ajoutons a list_to_check"""
  list_to_check_copie = list(list_to_check)
 
  for line in list_to_check_copie: 
    currentCol = list()
    for i in range(3):
      for item in list_to_check_copie:
        currentCol.append(item[i])

  

def player_input(player):
  #getting the row
  while True:
    while True:
      try:
        player['row'] = int(input('Entrer le numero de ligne: '))
      except:
        print("Veuillez entrer un nombre entier entre 1 et 3 pour la ligne")
      else:
        if player['row'] not in range(1,4):
          print("Veuillez entrer un nombre entier entre 1 et 3 pour la ligne")
          continue
        else:
          break
      

    #getting the col
  
    while True:
      try:
        player['col'] = int(input('Entrer le numero de colonne: '))
      except:
        print("Veuillez entrer un nombre entier entre 1 et 3 pour la colonne")
      else:
        if player['col'] not in range(1,4):
          print("Veuillez entrer un nombre entier entre 1 et 3 pour la colonne")
          continue
        else:
          break

    if str(player['row'])+str(player['col']) not in idResponse:
        print(f"\nA la ligne {player['row']} et à la colonne {player['col']} sont deja occupes, veuillez choisir une autre position\n")
        continue
    else:
      print(f"{player['row']} and {player['col']}\n")
      break

""" player_input(players[1])
placePlayerChoice(players[1])
display_board() """
check_win()