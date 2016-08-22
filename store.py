from valid import *

#This is the initial store greeting function. The user will learn here what they can buy. 
def storeGreeting(leader, personOne, personTwo, personThree, personFour, month, oxenTotal, foodTotal, clothTotal, spareTotal):
  print("\033c")
  print("{__________________________________}")
  print("Hello, I am Daniel.")
  print("So you're going to Oregon! I can fix you up with what you need: ")
  print(" - A team of oxen to pull your wagon")
  print(" - Clothing for both summer and winter")
  print(" - Plenty of food for the trip")
  print(" - Spare parts for your wagon")
  input("Press enter to continue ")
  storeMain(leader, personOne, personTwo, personThree, personFour, month, oxenTotal, foodTotal, clothTotal, spareTotal)

#This is the main menu screen which will keep track of all of the supplies that the player buys.
def storeMain(leader, personOne, personTwo, personThree, personFour, month, oxenTotal, foodTotal, clothTotal, spareTotal):
  print("\033c")
  print("-----------------------------------------")
  print("         Daniel's General Store          ") 
  print("         Independence, Missouri          ")
  print("-----------------------------------------")
  print("1. Oxen $" + str(oxenTotal))
  print("2. Food $" + str(foodTotal))
  print("3. Clothing $" + str(clothTotal))
  print("4. Spare Parts $" + str(spareTotal))
  leader.money = leader.money - (oxenTotal + foodTotal + clothTotal + spareTotal)
  print("Amount you have: $" + str(leader.money))
  choice = int(input("Which item would you like to buy? "))
  while not storemainValid(choice):
    choice = int(input("Which item would you like to buy? "))
  if choice == 1:
    oxenTotal = oxen()
    storeMain(leader, personOne, personTwo, personThree, personFour, month, oxenTotal, foodTotal, clothTotal, spareTotal)
  elif choice == 2:
    foodTotal = food()
    storeMain(leader, personOne, personTwo, personThree, personFour, month, oxenTotal, foodTotal, clothTotal, spareTotal)
  elif choice == 3:
    clothTotal = cloth()
    storeMain(leader, personOne, personTwo, personThree, personFour, month, oxenTotal, foodTotal, clothTotal, spareTotal)
  elif choice == 4:
    spareTotal = spare()
    storeMain(leader, personOne, personTwo, personThree, personFour, month, oxenTotal, foodTotal, clothTotal, spareTotal)
  elif choice == 5:
    goodLuckScreen()

#This is the function that takes you to buy the required number of oxen for your journey.
def oxen():
  print("\033c")
  print("-----------------------------------------")
  print("         Daniel's General Store          ") 
  print("         Independence, Missouri          ")
  print("-----------------------------------------")
  print("There are 2 oxen in a yoke. I recommend at least 3 yoke.")
  print("I charge $40 a yoke.")
  print("Think carefully before you purchase. For all sales are final!")
  yokeNumber = int(input("How man yoke do you want? "))
  while not oxenValid(yokeNumber):
    print("Value must be between 1 and 10")
    yokeNumber = int(input("How man yoke do you want? "))
  oxenTotal = yokeNumber * 40
  print("Bill so far: $" + str(oxenTotal))
  return oxenTotal

#A brief screen that will tell the player good luck once they exit the store. 
def goodLuckScreen():
  print("\033c")
  print("Well, then, you're ready to start. Good Luck!")
  print("The journey will be long and hard!")
  input("Press enter to continue ")




































