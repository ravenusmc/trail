from valid import *
import datetime

#This is the main game menu that the user will see as they travel along the trail.
def trailMenu(wagon, leader, personOne, personTwo, personThree, personFour, month):
  print("\033c")
  print("Weather: ")
  print("Health: ")
  print("Pace: ")
  print("Rations: ")
  print("Distance: ")
  print('\n')
  print("You may:")
  print("1. Continue on the trail")
  print("2. Check supplies")
  print("3. Change Pace")
  print("4. Change food rations")
  print("5. Stop to rest")
  print("6. Buy Supplies")
  choice = int(input("What is your choice? "))
  while not trailMenuValid(choice):
    print("That was not a valid selection!")
    choice = int(input("What is your choice? "))
  if choice == 1:
    wagon.move()
  elif choice == 2:
    checkSupplies(wagon)
  elif choice == 3:
    changePace(wagon)

#This function takes the user to the supplies screen where they can see the level of their supplies. 
def checkSupplies(wagon):
  print("You have the following supplies on hand: ")
  print(wagon.oxen)
  print(wagon.food)
  print(wagon.cloth)
  print(wagon.wheel)
  print(wagon.axle)
  print(wagon.tongue)
  input("Press enter to return to the menu!")
  trailMenu(wagon, leader, personOne, personTwo, personThree, personFour, month)

#This function will allow the user to change the pace of the wagon. 
def changePace(wagon):
  print("Here you can change the speed of your wagon.")
  print("You currently have:", wagon.oxen, "oxen.")
  yoke = wagon.oxen / 2 
  print("How many yokes, 2 oxen, do you want to take off or increase?")
  print("1. Increase speed")
  print("2. Decrease speed")
  choice = int(input("What is your choice? "))
  if choice == 1: 
    
  print()






# def setupMenu(wagon, leader, personOne, personTwo, personThree, personFour, month):
#   calenderSetup(month)

# def calenderSetup(month):
#   test = datetime(1848, 1, 1)
#   print(test)

