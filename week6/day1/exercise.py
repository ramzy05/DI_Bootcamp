""" #For example,  
#my_name = "Frank"  this line creates a name variable type: string 
#print("My name is {}".format(my_name))

cars = 100#this line creates a variable type : integer
space_in_a_car = 4.0#this line creates a variable type : float
drivers = 30 #this line creates a variable type: integer
passengers = 90 #this line creates a variable type: integer
cars_not_driven = cars - drivers #this line return(inside cars_not_driven) the  substraction the value drivers var value in the value of cars
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven


print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car,"in each car.")
 """


user_input = int(input('Entrer a number between 1 and 100: '))
if not user_input % 3:
  print('Fizz')
if not user_input % 5:
  print('Buzz')
if (not user_input % 5) and (not user_input % 3):
  print('FizzBuzz')