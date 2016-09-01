#I created this merchant class to help solve some problems that I was having wih the store file. 
#So far, it seems to help solve my problems as well as to increase my understanding of OOP.
class Merchant():

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

  def MerchantMain(self, wagon, leader):
    print("\033c")
    print("So, Say, what would you nice folks like?")
    print("You may only choose one option and I may not be back soon!")
    print("1. Food")
    print("2. Wheel")
    print("3. Axle")
    if choice == 1:
      print("Food is .50 cents per pound!")
      amount = int(input("How much food y'all want? ")
      




