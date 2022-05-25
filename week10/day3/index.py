import json

my_family = ''

json_file = "file.json"

with open(json_file, 'r') as file_obj:
    my_family = json.load(file_obj)
 
for child, color in zip(my_family['children'], ['pink', 'yellow']):
    child['favorite_color'] = color

with open(json_file, 'w') as file_obj:
    json.dump(my_family, file_obj, indent = 2, sort_keys=True)