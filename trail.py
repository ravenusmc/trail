from valid import *
import datetime
import random

#Need possible loop for travellingTrail function. 

#This function will be where the player will be traveling the trail. 
def travellingTrail(wagon, leader, personOne, personTwo, personThree, personFour, month):
  print("\033c")
  print("Weather: ")
  print("Health: ")
  print("Pace: ", (wagon.oxen / 2)  * 5, "MPH")
  print("Rations: ", wagon.ration)
  print("Distance: ", wagon.distance)
  print("1. Travel the trail")
  print("2. Stop to rest")
  print("3. More options.")
  choice = int(input("What is your choice? "))
  while not travellingTrailValid(choice):
    print("Invalid Selection!")
    choice = int(input("What is your choice? "))
  if choice == 1:
    print("add stuff")
  elif choice == 2:
    print("add stuff")
  elif choice == 3: 
    trailMenu(wagon, leader, personOne, personTwo, personThree, personFour, month)


#This is the main game menu that the user will see as they travel along the trail.
def trailMenu(wagon, leader, personOne, personTwo, personThree, personFour, month):
  print("\033c")
  print("You may:")
  print("1. Continue on the trail")
  print("2. Check supplies")
  print("3. Change Pace")
  print("4. Change food rations")
  print("5. Buy Supplies")
  choice = int(input("What is your choice? "))
  while not trailMenuValid(choice):
    print("That was not a valid selection!")
    choice = int(input("What is your choice? "))
  if choice == 1:
    travellingTrail(wagon, leader, personOne, personTwo, personThree, personFour, month)
  elif choice == 2:
    checkSupplies(wagon, leader, personOne, personTwo, personThree, personFour, month)
  elif choice == 3:
    changePace(wagon, leader, personOne, personTwo, personThree, personFour, month)
  elif choice == 4:
    changeFood(wagon, leader, personOne, personTwo, personThree, personFour, month)
  elif choice == 6:
    buySupplies(wagon, leader, personOne, personTwo, personThree, personFour, month)


#This function takes the user to the supplies screen where they can see the level of their supplies. 
def checkSupplies(wagon, leader, personOne, personTwo, personThree, personFour, month):
  print("\033c")
  print("You have the following supplies on hand: ")
  print(wagon.oxen)
  print(wagon.food)
  print(wagon.cloth)
  print(wagon.wheel)
  print(wagon.axle)
  print(wagon.tongue)
  input("Press enter to return to the menu!")
  travellingTrail(wagon, leader, personOne, personTwo, personThree, personFour, month)

#This function will allow the user to change the pace of the wagon. 
def changePace(wagon, leader, personOne, personTwo, personThree, personFour, month):
  print("\033c")
  print("Here you can change the speed of your wagon.")
  print("You currently have:", wagon.oxen, "oxen.")
  print("How many yokes, 2 oxen, do you want to take off or increase?")
  print("Each yoke added increases your speed by 5 MPH up to 25 MPH")
  print("1. Increase speed")
  print("2. Decrease speed")
  print(wagon.speed)
  print(wagon.oxen)
  choice = int(input("What is your choice? "))
  if choice == 1: 
    speedUp = int(input("how many yoke's do you want to add, to your wagon? "))
    while not increaseValid(speedUp, wagon):
      print("Invalid selection, cannot go above:", wagon.speed, "based off your oxen count!" )
      speedUp = int(input("how many yoke's do you want to add, to your wagon? "))
    wagon.speed = (speedUp * 5) + wagon.speed
  elif choice == 2:
    speedDown = int(input("how many yoke's do you want to take off your wagon? "))
    while not decreaseValid(speedDown, wagon):
      print("Invalid selection cannot go below zero!")
      speedDown = int(input("how many yoke's do you want to take off your wagon? "))
    wagon.speed = wagon.speed - (speedDown * 5)
  print("Your new wagon speed is:", wagon.speed)
  input("Press enter to return to the menu!")
  travellingTrail(wagon, leader, personOne, personTwo, personThree, personFour, month)

#This function will allow you to change the food levels for your party. 
def changeFood(wagon, leader, personOne, personTwo, personThree, personFour, month):
  print("\033c")
  print("Here you can change the amount of food your group is eating")
  print("What level do you want to make them at: ")
  print("1. Meager")
  print("2. Normal")
  print("3. Tons")
  choice = int(input("What is your choice? "))
  while not changeFoodValid(choice):
    print("That is not a correct entry!")
    choice = int(input("What is your choice? "))
  if choice == 1:
    print("Rations sent to meager levels!")
    wagon.ration = "Meager"
  elif choice == 2:
    print("Rations sent to normal levels!")
    wagon.ration = "Normal"
  elif choice == 3:
    print("Rations sent to 'tons' level")
    wagon.ration = "Tons"
  input("Press enter to return to the menu!")
  travellingTrail(wagon, leader, personOne, personTwo, personThree, personFour, month)

def buySupplies(wagon, leader, personOne, personTwo, personThree, personFour, month):
  print("\033c")
  merchant = random.randint(1, 10)
  if merchant > 5:
    travelingMercahnt(wagon, leader, personOne, personTwo, personThree, personFour, month, oxenTotal, foodTotal, clothTotal, spareTotal)
  elif merchant <= 5:
    print("Sorry no Merchant is around!")
  input("Press enter to return to the menu!")
  travellingTrail(wagon, leader, personOne, personTwo, personThree, personFour, month)









# def setupMenu(wagon, leader, personOne, personTwo, personThree, personFour, month):
#   calenderSetup(month)

# def calenderSetup(month):
#   test = datetime(1848, 1, 1)
#   print(test)

