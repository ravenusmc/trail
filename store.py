from valid import *

#This is the initial store greeting function. The user will learn here what they can buy. 
def storeGreeting(wagon, leader, personOne, personTwo, personThree, personFour, month, oxenTotal, foodTotal, clothTotal, spareTotal):
  print("\033c")
  print("{__________________________________}")
  print("Hello, I am Daniel.")
  print("So you're going to Oregon! I can fix you up with what you need: ")
  print(" - A team of oxen to pull your wagon")
  print(" - Clothing for both summer and winter")
  print(" - Plenty of food for the trip")
  print(" - Spare parts for your wagon")
  input("Press enter to continue ")
  storeMain(wagon, leader, personOne, personTwo, personThree, personFour, month, oxenTotal, foodTotal, clothTotal, spareTotal)

#This is the main menu screen which will keep track of all of the supplies that the player buys.
def storeMain(wagon, leader, personOne, personTwo, personThree, personFour, month, oxenTotal, foodTotal, clothTotal, spareTotal):
  storeGreeter()
  print("1. Oxen $" + str(oxenTotal))
  print("2. Food $" + str(foodTotal))
  print("3. Clothing $" + str(clothTotal))
  print("4. Spare Parts $" + str(spareTotal))
  print("5. Start Your Journey!")
  leader.money = leader.money - (oxenTotal + foodTotal + clothTotal + spareTotal)
  print("Amount you have: $" + str(leader.money))
  choice = int(input("Which item would you like to buy? "))
  while not storemainValid(choice):
    choice = int(input("Which item would you like to buy? "))
  if choice == 1:
    oxenTotal = oxen()
    storeMain(wagon, leader, personOne, personTwo, personThree, personFour, month, oxenTotal, foodTotal, clothTotal, spareTotal)
  elif choice == 2:
    foodTotal = food()
    storeMain(wagon, leader, personOne, personTwo, personThree, personFour, month, oxenTotal, foodTotal, clothTotal, spareTotal)
  elif choice == 3:
    clothTotal = cloth()
    storeMain(wagon, leader, personOne, personTwo, personThree, personFour, month, oxenTotal, foodTotal, clothTotal, spareTotal)
  elif choice == 4:
    spareTotal = spare()
    storeMain(wagon, leader, personOne, personTwo, personThree, personFour, month, oxenTotal, foodTotal, clothTotal, spareTotal)
  elif choice == 5:
    goodLuckScreen()

#This is the function that takes you to buy the required number of oxen for your journey.
def oxen():
  storeGreeter()
  print("There are 2 oxen in a yoke. I recommend at least 3 yoke.")
  print("I charge $40 a yoke.")
  print("Think carefully before you purchase. For all sales are final!")
  yokeNumber = int(input("How many yoke do you want? "))
  while not oxenValid(yokeNumber):
    print("Value must be between 1 and 5")
    yokeNumber = int(input("How many yoke do you want? "))
  oxenTotal = yokeNumber * 40
  return oxenTotal

def food():
  storeGreeter()
  print("I recommend taking at least 200 lbs of food / person.")
  print("I sell bulk food for .20 cents a pound")
  print("Think carefully before you purchase. For all sales are final!")
  foodNumber = int(input("How many pounds of food do you want? "))
  while not foodValid(foodNumber):
    print("Value must be 0 or greater!")
    foodNumber = int(input("How many pounds of food do you want? "))
  foodTotal = foodNumber * .20
  return foodTotal

def cloth():
  storeGreeter()
  print("You'll need warm clothing in the mountains.")
  print("I recommend taking at least 2 sets of clothes per person.")
  print("Each set is $10.00.")
  clothNumber = int(input("How many sets of cloth do you want? "))
  while not clothValid(clothNumber):
    print("Value must be 0 or greater")
    clothNumber = int(input("How many sets of cloth do you want? "))
  clothTotal = clothNumber * 10
  return clothTotal

def spare():
  storeGreeter()
  print("It's a good idea to have a few spare parts for your wagon.")
  print("Here are the prices: ")
  print("Wagon wheel - $10 each")
  print("Wagon axle - $10 each")
  print("wagon tongue - $10")
  wheel = int(input("How many wagon wheels? "))
  while not wheelValid(wheel):
    print("Value must be 0 or greater!")
    wheel = int(input("How many wagon wheels? "))
  wheelTotal = wheel * 10
  axle = int(input("How many wagon axle's? "))
  while not axleValid(axle):
    print("value must be 0 or greater!")
    axle = int(input("How many wagon axle's? "))
  axleTotal = axle * 10
  tongue = int(input("How many wagon tongue's? "))
  while not tongueValid(tongue):
    print("Value must be 0 or greater!")
    tongue = int(input("How many wagon tongue's? "))
  tongueTotal = tongue * 10 
  spareTotal = tongueTotal + axleTotal + wheelTotal
  return spareTotal

#A brief screen that will tell the player good luck once they exit the store. 
def goodLuckScreen():
  print("\033c")
  print("Well, then, you're ready to start. Good Luck!")
  print("The journey will be long and hard!")
  input("Press enter to continue ")

##### Other Store Functions 

def storeGreeter():
  print("\033c")
  print("-----------------------------------------")
  print("         Daniel's General Store          ") 
  print("         Independence, Missouri          ")
  print("-----------------------------------------")




































