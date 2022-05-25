import datetime

 
my_bd = datetime.datetime(2022, 7, 5)

day = my_bd.timestamp() - datetime.datetime.now().timestamp()
day = str(datetime.timedelta(seconds=day))
day = day.replace(', ', ' and ')
print(f"My birthday is in {day}")