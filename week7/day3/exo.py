


my_list = ["Rick", "Morty", "Beth", "Jerry", "Snowball"]


final_list = list(map(lambda name: f'Hello {name}\n', list(filter(lambda name: len(name) < 5, my_list))))

print(''.join(final_list))