from valid import *

#I created this merchant class to help solve some problems that I was having wih the store file. 
#So far, it seems to help solve my problems as well as to increase my understanding of OOP. The methods 
#in this file may be long but they got the job done and help me solve my issue!
class Merchant():

  #This method introduces the player to the traveling merchant. 
  def travelingMerchant(self, wagon, leader):
    print("\033c")
    print("{__________________________________}")
    print("Hello, I am the travelling Merchant.")
    print("Luckily you found me on your journey! I can fix you up with what you need: ")
    print(" - A team of oxen to pull your wagon")
    print(" - Clothing for both summer and winter")
    print(" - Plenty of food for the trip")
    print(" - Spare parts for your wagon")
    input("Press enter to continue ")

  #This method allows the player to buy certain items from the traveling merchant. 
  def MerchantMain(self, wagon, leader):
    print("\033c")
    print("So, Say, what would you nice folks like?")
    print("You may only choose one option and I may not be back soon!")
    print("1. Food")
    print("2. Wheel")
    print("3. Axle")
    choice = int(input("What is your choice? "))
    while not merchantClassValid(choice):
      print("That is not a valid selection!")
      choice = int(input("What is your choice? "))
    if choice == 1:  
      print("Food is .50 cents per pound!")
      amount = int(input("How much food y'all want? "))
      while merchantPriceValid(amount):
        print("The value cannot be below 0")
        amount = int(input("How much food y'all want? "))
      total = amount * .50 
      leader.money = leader.money - total 
      wagon.food = wagon.food + amount 
      print("Thank you for your business!")
    elif choice == 2:
      print("Wheels are 20 each!")
      amount = int(input("How many wheels y'all want? "))
      while merchantPriceValid(amount):
        print("The value cannot be below 0")
        amount = int(input("How many wheels y'all want? "))
      total = amount * 20
      leader.money = leader.money - total 
      wagon.wheel = wagon.wheel + amount 
      print("Thank you for your business!")
    elif choice == 3:
      print("Axles are 20 each!")
      amount = int(input("How many axles y'all want? "))
      while merchantPriceValid(amount):
        print("The value cannot be below 0")
        amount = int(input("How many axles y'all want? "))
      total = amount * 20
      leader.money = leader.money - total 
      wagon.axle = wagon.axle + amount 
      print("Thank you for your business!")







