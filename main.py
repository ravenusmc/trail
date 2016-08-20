from valid import *


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
  print("1. Be a baner from Boston")
  print("2. Be a Carpenter from Ohio")
  print("3. Be a farmer from Illinois")
  print("4. Find out the differences between these choices")
  choice = int(input("What is your choice? "))
  while not characterValid(choice):
    choice = int(input("What is your choice? "))
  if choice == 1:
    banker()
  elif choice == 2:
    carpenter()
  elif choice == 3:
    farmer()
  elif choice == 4:
    characterDifferences()



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
