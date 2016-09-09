from valid import *
from humanClass import *
from wagon import Wagon
from store import *


#This is the title screen of the game and introduces the user to it. This will also be the main menu of
#the game.
def main():
  print("\033c")
  print("{            The Oregon Trail             }")
  print(" ----------------------------------------- ")
  print("You may:")
  print("1. Travel the trail")
  print("2. Learn about the trail")
  print("3. Quit")
  choice = int(input("What is your choice? "))
  while not mainValid(choice):
    choice = int(input("What is your choice? "))
  if choice == 1:
    characterSelection()
  elif choice == 2:
    learn()
  elif choice == 3:
    quit()

#This function is where you will select the character that you want to be. 
#The banker is easy, carpenter is medium and the farmer is hard. 
def characterSelection():
  print("\033c")
  print("{__________________________________}")
  print("Many kinds of people made the trip to Oregon.")
  print("You may: ")
  print("1. Be a banker from Boston")
  print("2. Be a Carpenter from Ohio")
  print("3. Be a farmer from Illinois")
  print("4. Find out the differences between these choices")
  choice = int(input("What is your choice? "))
  while not characterValid(choice):
    choice = int(input("What is your choice? "))
  if choice == 1:
    characterNames(choice)
  elif choice == 2:
    characterNames(choice)
  elif choice == 3:
    characterNames(choice)
  elif choice == 4:
    characterDifferences()

#This is where the player will establish the names of all of the people in their party including their own.
def characterNames(choice):
  print("\033c")
  name = input("What is the first name of the wagon leader? ")
  if choice == 1:
    leader = Human(name, "Banker")
    leader.money = 2000
  elif choice == 2:
    leader = Human(name, "Carpenter")
    leader.money = 1500
  elif choice == 3: 
    leader = Human(name, "Farmer")
    leader.money = 1000
  print("What are the first names of the other members of your party?")
  name = input("Please enter a name: ")
  personOne = Human(name, "partyOne")
  name = input("Please enter a name: ")
  personTwo = Human(name, "partyTwo")
  name = input("Please enter a name: ")
  personThree = Human(name, "partyThree")
  name = input("Please enter a name: ")
  personFour = Human(name, "partyFour")
  print("Jumping back to 1848!")
  monthSelection(leader, personOne, personTwo, personThree, personFour)

#This function is where the player will select which month they want to start the journey in.
def monthSelection(leader, personOne, personTwo, personThree, personFour):
  print("\033c")
  print("{__________________________________}")
  print("It is 1848.")
  print("Your jumping off place for Oregon is Independence, Missouri.")
  print("You must decide which month to leave Indepence.")
  print("1. March")
  print("2. April")
  print("3. May")
  print("4. June")
  print("5. July")
  choice = int(input("What is your choice? "))
  while not monthValid(choice):
     choice = int("What is your choice? ")
  month = ""
  if choice == 1:
    month = "3/1/1848" 
  elif choice == 2:
    month = "4/1/1848"
  elif choice == 3:
    month = "5/1/1848"
  elif choice == 4:
    month = "6/1/1848"
  elif choice == 5:
    month = "7/1/1848"
  oxenTotal = 0.00
  foodTotal = 0.00
  clothTotal = 0.00
  spareTotal = 0.00
  bulletsTotal = 0.00
  wagon = Wagon("Normal", "Good", "Sunny", month)
  storeGreeting(wagon, leader, personOne, personTwo, personThree, personFour, oxenTotal, foodTotal, clothTotal, spareTotal, bulletsTotal)

####### NON ESSENTIAL FUNCTIONS HERE ##########

#This function is the quit function that will bring the user out of the game. 
def quit():
  print("\033c")
  print("Well, hopefully you will like to travel the trail one day!")
  print("Be sure to always study history!")
  input("Have a great day! (PRESS ENTER TO EXIT) ")
  exit()

#This function will tell the user where to find more information about the Oregan trail. 
def learn():
  print("\033c")
  print("If you want information about the Oregon trail I suggest that you check out wikipedia.")
  print("Here is a good link: ")
  print("https://en.wikipedia.org/wiki/Oregon_Trail")
  print("If you want information on the game look at: ")
  print("https://en.wikipedia.org/wiki/The_Oregon_Trail_(video_game)")
  print("Fun Fact: The Oregon Trail computer game was originally a card game!")
  print("Take that Settlers of Cataan!!!")
  print("(I actually really like Settlers of Cataan)")
  print('\n')
  menuFunc()

def characterDifferences():
  print("\033c")
  print("The main differences between the characters is the amount of money you will get.")
  print("The banker gets the most, then the carpenter and finally the farmer.")
  print("If you choose the banker you will also get the least amount of bonus points at the end.")
  print("Basically, the banker is easy, carpenter is medium and the farmer is hard.")
  menuFunc()

def menuFunc():
  print("What do you want to do: ")
  print("1. Main Menu")
  print("2. Quit")
  choice = int(input("What is your choice? "))
  if choice == 1:
    main()
  elif choice == 2:
    quit()

main()
