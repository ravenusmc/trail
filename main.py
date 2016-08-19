from valid import *
from auxFuncs import *

#This is the title screen of the game and introduces the user to it. 
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
    start()
  elif choice == 2:
    learn()
  elif choice == 3:
    quit()

main()