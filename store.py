from valid import *

#This is the initial store greeting function. The user will learn here what they can buy. 
def storeGreeting(leader, personOne, personTwo, personThree, personFour, month):
  print("\033c")
  print("{__________________________________}")
  print("Hello, I am Daniel.")
  print("So you're going to Oregon! I can fix you up with what you need: ")
  print(" - A team of oxen to pull your wagon")
  print(" - Clothing for both summer and winter")
  print(" - Plenty of food for the trip")
  print(" - Spare parts for your wagon")
  input("Press enter to continue ")
  storeMain(leader, personOne, personTwo, personThree, personFour, month)

#This is the main menu screen which will keep track of all of the supplies that the player buys.
def storeMain(leader, personOne, personTwo, personThree, personFour, month):
  print("\033c")
  print("-----------------------------------------")
  print("         Daniel's General Store          ") 
  print("         Independence, Missouri          ")
  print("-----------------------------------------")
  oxenTotal = 0.00
  foodTotal = 0.00
  clothTotal = 0.00
  spareTotal = 0.00
  print("1. Oxen $" + str(oxenTotal))
  print("2. Food $" + str(foodTotal))
  print("3. Clothing $" + str(clothTotal))
  print("4. Spare Parts $" + str(spareTotal))
  print("Amount you have: $" + str(leader.money))
  choice = int(input("Which item would you like to buy? "))
  if choice == 1:
    oxen()

def oxen():
  print("\033c")
  print("-----------------------------------------")
  print("         Daniel's General Store          ") 
  print("         Independence, Missouri          ")
  print("-----------------------------------------")
  print("There are 2 oxen in a yoke. I recommend at least 3 yoke.")
  print("I charge $40 a yoke.")
  yokeNumber = int(input("How man yoke do you want? "))
  yokeCost = yokeNumber * 40
  print("Bill so far: $" + str(yokeCost))
  storeMain(leader, personOne, personTwo, personThree, personFour, month, yokeCost)




































