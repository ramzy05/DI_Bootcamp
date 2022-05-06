


word = (input('Entrer une phrase: ')).lower()
action = 0

while True:
  print("""\n1- crypter votre phrase
2- decrypter votre phrase""")

  action = input('\nEntrer le numéro de l\'operation souhaitée: ')
  if(action in['1', '2']):
    break
  else:
    print('Veuillez entrer un choix valide!\n')

if(action == '1'):
  encrypted_w = ''
  for letter in word:
    order = ord(letter) + 3
    if(order > ord('z')):
      order = ord('a') +  order - ord('z') - 1
      encrypted_w += chr(order)
    else:
      encrypted_w += chr(order)
  print('\ncryptage en cours...')
  print('...')
  print('..')
  print(word,'(encryptage)=>',encrypted_w)

elif(action == '2'):
  decrypted_w = ''
  for letter in word:
    order = ord(letter) - 3
    if(order  < ord('a')):
      order = ord('z') +  order - ord('a') + 1
      decrypted_w += chr(order)
    else:
      decrypted_w += chr(order)

  print('\ndécryptage en cours...')
  print('...')
  print('..')
  print(word,'(decryptage)=>',decrypted_w)