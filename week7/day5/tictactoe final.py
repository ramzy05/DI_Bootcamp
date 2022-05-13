
from random import randint


lastestPlayer = ''

players = [
  {
    'value': ' X ',
    'row': '',
    'col':'',
    'name': 'playerX', 
  },
  {
    'value': ' O ',
    'row': '',
    'col': '',
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
""" resultat = [

  '*****************',
  ['*  ',' X ','|',' X ','|',' X ', '  *'],
  ['*  ','---','|','---','|','---','  *'],
  ['*  ','   ','|','   ','|','   ', '  *'],
  ['*  ','---','|','---','|','---','  *'],
  ['*  ','   ','|','   ','|','   ','  *'],
  '*****************'
] """

resultat =[
  ['   ','   ','   '],
  ['   ','   ','   '],
  ['   ','   ','   ']
]



def display_board():

  print('\nTIC TAC TOE')
  print('*****************')
  print(f"*  {resultat[0][0]}|{resultat[0][1]}|{resultat[0][2]}  *")
  print('*  ---|---|---  *')
  print(f"*  {resultat[1][0]}|{resultat[1][1]}|{resultat[1][2]}  *")
  print('*  ---|---|---  *')
  print(f"*  {resultat[2][0]}|{resultat[2][1]}|{resultat[2][2]}  *")
  print('*****************')


def placePlayerChoice(player):
  resultat[player['row']-1][player['col']-1] = player['value']
    

def check_line(line):
  if line.count(' X ')== 3:
    display_board()
    print('\n\nPlayerX win')
    return True
  elif line.count(' O ') == 3:
    display_board()
    print('\n\nPlayerO win')
    return True
  return False

def col_to_line(lines):
  col_line = list()#ici on stockera les colonnes transformés en ligne
  
  for i in range(len(lines)):
    tmp = list()#on stockera les colones avant de les ajouter a currentCol 
    for actual_line in lines:
      tmp.append(actual_line[i])
     
    col_line.append(tmp)

  return col_line

def diag_to_line(lines):
  diag_line = [
    [
      lines[0][0],
      lines[1][1],
      lines[2][2]
    ],
    [
      lines[0][2],
      lines[1][1],
      lines[2][0]
    ]
  ]
  

  return diag_line


def check_win():
  list_to_check = list(resultat)
  list_to_check_copy = list(list_to_check)
  

  #check les lignes
  list_to_check.extend(col_to_line(list_to_check_copy))
  list_to_check.extend(diag_to_line(list_to_check_copy))

  for line in list_to_check:
    if check_line(line):
      return True
  
  return False


  

def player_input(player):
  #getting the row
  while True:
    while True:
      try:
        player['row'] = int(input(f"{player['name']} entrer le numero de ligne: "))
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
        player['col'] = int(input(f"{player['name']} entrer le numero de colonne: "))
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
      #success
      placePlayerChoice(player)

      #enlevons les couples possibles dans idResponse:
      idResponse.remove(str(player['row'])+str(player['col']))

      break

"""player_input(players[1])
display_board() """

#stop est une variable global qui va permettre de stopper ma boucle dans la fonction play


def change_player(player):
  if players.index(player) == 0 :
    return 1
  else:
    return 0
  

def play():

  count = 1 #count sera superieur ou egale à 3
  player = players[randint(0,1)]
  
  display_board()#print board first time

  player_input(player)#initialisation du jeu, premier tour du premier joueur


  while True and count <= 9:

    count += 1
    player = players[change_player(player)]
    display_board()
    player_input(player)#le joue suivant joue a son tour

    if(count >= 3):
      """ on check si quelqu'un a gagné """
      
      if check_win():
        break


  if count >= 10:
    print("\n\n\nEgalité :-)") 

  """ fin du jeu si count = 10 """
  print('\n\nEnd of the game')

  

play()
