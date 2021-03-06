from valid import *
from merchant import *
from huntClass import *
from river import *
import datetime
import random
#I am using pandas to convert my date. I spent about two weeks slowly researching how to take a date
#and add one to it. I found the solution on stackover flow by using pandas. 
import pandas as pd
 
#This function will be where the player will be traveling the trail. 
def travellingTrail(wagon, leader, personOne, personTwo, personThree, personFour):
  print("\033c")
  print("Date: ", wagon.month)
  print("Weather: ", wagon.weather)
  print("Health:", wagon.health)
  print("Pace: ", wagon.speed, "MPH")
  print("Ration Level: ", wagon.ration)
  print("Food amount: ", wagon.food)
  print("Distance: ", wagon.distance)
  print("1. Travel the trail")
  print("2. Stop to rest")
  print("3. More options.")
  choice = int(input("What is your choice? "))
  while not travellingTrailValid(choice):
    print("Invalid Selection!")
    choice = int(input("What is your choice? "))
  if wagon.distance > 0 and leader.life > 0:
    if choice == 1:
      trailMoving(wagon, leader, personOne, personTwo, personThree, personFour)
    elif choice == 2:
      trailResting(wagon, leader, personOne, personTwo, personThree, personFour)
    elif choice == 3: 
      trailMenu(wagon, leader, personOne, personTwo, personThree, personFour)
  elif wagon.distance <= 0:
    Oregon(wagon, leader, personOne, personTwo, personThree, personFour)
  elif leader.life <= 0:
    died(wagon, leader, personOne, personTwo, personThree, personFour)

#This function will actually change all of the factors when the wagon is moving. The Weather type, distance 
#travelled, wagon speed, pace, ration level, and overall health are all calculated by this one function. 
def trailMoving(wagon, leader, personOne, personTwo, personThree, personFour):
  print("\033c")
  #I wonder if there is a way to combine all of these objects into one?
  leader.lifeDrop(wagon)
  personOne.lifeDrop(wagon)
  personTwo.lifeDrop(wagon)
  personThree.lifeDrop(wagon)
  personFour.lifeDrop(wagon)
  leader.diseaseInfection()
  personOne.diseaseInfection()
  personTwo.diseaseInfection()
  personThree.diseaseInfection()
  personFour.diseaseInfection()
  leader.diseaseKilling()
  personOne.diseaseKilling()
  personTwo.diseaseKilling()
  personThree.diseaseKilling()
  personFour.diseaseKilling()
  leader.die()
  personOne.die()
  personTwo.die()
  personThree.die()
  personFour.die()
  wagon.changeDate()
  wagon.weatherType()
  wagon.eat()
  wagon.clothingWorn()
  wagon.wagonWheel()
  wagon.wagonAxle()
  wagon.wagonTongue()
  riverAhead(wagon, leader, personOne, personTwo, personThree, personFour)
  wagon.move()
  wagon.healthLevel(leader, personOne, personTwo, personThree, personFour)
  travellingTrail(wagon, leader, personOne, personTwo, personThree, personFour)

#This function is what will control everything when the user rests. The date will still increase, food will go down
#but the party health will go up. 
def trailResting(wagon, leader, personOne, personTwo, personThree, personFour):
  print("\033c")
  wagon.changeDate()
  wagon.weatherType()
  wagon.eat()
  leader.lifeIncrease(wagon)
  personOne.lifeIncrease(wagon)
  personTwo.lifeIncrease(wagon)
  personThree.lifeIncrease(wagon)
  personFour.lifeIncrease(wagon)
  leader.rest()
  personOne.rest()
  personTwo.rest()
  personThree.rest()
  personFour.rest()
  wagon.clothingWorn()
  wagon.healthLevel(leader, personOne, personTwo, personThree, personFour)
  travellingTrail(wagon, leader, personOne, personTwo, personThree, personFour)

#This function will play at the end of the game when the user reaches Oregon. I know the words are not 
#correctly spelled. It was from the old ending of Ghostbusters for the NES. 
def Oregon(wagon, leader, personOne, personTwo, personThree, personFour):
  print("\033c")
  print("You have reached Oregon!")
  print("Conglaturation!!!")
  print("You have completed a Great Game!")
  print("Now go and rest our Heroes!")
  input("Press Enter to exit!")

#This function will execute when the party has died. 
def died(wagon, leader, personOne, personTwo, personThree, personFour):
  print("\033c")
  print("It is a sad day")
  print(leader.name + " has died!")
  print("Your journey to Oregon is over!")
  print("May you return to the soil from which you came...")
  input("Press Enter to exit!")

### Trail Menu and its Functions below ###

#This is the main game menu that the user will see as they travel along the trail.
def trailMenu(wagon, leader, personOne, personTwo, personThree, personFour):
  print("\033c")
  print("You may:")
  print("1. Continue on the trail")
  print("2. Check supplies")
  print("3. Change Pace")
  print("4. Change food rations")
  print("5. Buy Supplies")
  print("6. Hunt!")
  choice = int(input("What is your choice? "))
  while not trailMenuValid(choice):
    print("That was not a valid selection!")
    choice = int(input("What is your choice? "))
  if choice == 1:
    travellingTrail(wagon, leader, personOne, personTwo, personThree, personFour)
  elif choice == 2:
    checkSupplies(wagon, leader, personOne, personTwo, personThree, personFour)
  elif choice == 3:
    changePace(wagon, leader, personOne, personTwo, personThree, personFour)
  elif choice == 4:
    changeFood(wagon, leader, personOne, personTwo, personThree, personFour)
  elif choice == 5:
    buySupplies(wagon, leader, personOne, personTwo, personThree, personFour)
  elif choice == 6:
    hunt(wagon, leader, personOne, personTwo, personThree, personFour)


#This function takes the user to the supplies screen where they can see the level of their supplies. 
def checkSupplies(wagon, leader, personOne, personTwo, personThree, personFour):
  print("\033c")
  print("You have the following supplies on hand: ")
  print("Oxen: ", wagon.oxen)
  print("Food: ", wagon.food)
  print("Cloth: ", wagon.cloth)
  print("Wheel: ", wagon.wheel)
  print("Axle: ", wagon.axle)
  print("Tongue: ", wagon.tongue)
  print("bullets: ", wagon.bullets)
  input("Press enter to return to the menu!")
  travellingTrail(wagon, leader, personOne, personTwo, personThree, personFour)

#This function will allow the user to change the pace of the wagon. 
def changePace(wagon, leader, personOne, personTwo, personThree, personFour):
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
  travellingTrail(wagon, leader, personOne, personTwo, personThree, personFour)

#This function will allow you to change the food levels for your party. 
def changeFood(wagon, leader, personOne, personTwo, personThree, personFour):
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
  travellingTrail(wagon, leader, personOne, personTwo, personThree, personFour)

#This function will get use a radom number generator to see if a merchant is nearby. If the 
#merchant is nearby the player will be taken to the merchant store who sells some items. 
#However, the merchant store does not sell everything. Finally, this was the first time 
#that I actually tried using an object to set up the merchant. It worked nicely and I believe 
#it helped me gain a much larger grasp of OOP. 
def buySupplies(wagon, leader, personOne, personTwo, personThree, personFour):
  print("\033c")
  merchant = random.randint(1, 10)
  if merchant > 0:
    merchant = Merchant()
    merchant.travelingMerchant(wagon, leader)
    merchant.MerchantMain(wagon, leader)
  elif merchant <= 0:
    print("Sorry no Merchant is around!")
  input("Press enter to return to the menu!")
  travellingTrail(wagon, leader, personOne, personTwo, personThree, personFour)

#This will be my hunting function. It will not take the user to a screen where one shoots animals. Instead, 
#It will be a number guessing game where if you guess the number you reward will be randomly generated. 
def hunt(wagon, leader, personOne, personTwo, personThree, personFour):
  print("\033c")
  hunt = Hunt()
  hunt.welcome()
  hunt.hunting(wagon)
  travellingTrail(wagon, leader, personOne, personTwo, personThree, personFour)

#Creating a river crossing function. 
def riverAhead(wagon, leader, personOne, personTwo, personThree, personFour):
  print("\033c")
  riverChance = random.randint(1,200)
  shallowCrossPointChance = random.randint(1,200)
  if riverChance >= 175:
    river = River()
    print("The wagon has come upon a river")
    print("1. Cross the river")
    print("2. Try to look for a shallow place to cross")
    option = int(input("What would you like to do? "))
    while not riverAheadValid(option):
      print("That is not a valid option!")
      option = int(input("What would you like to do? ")) 
    if option == 1:
      river.crossRiver(wagon, leader, personOne, personTwo, personThree, personFour)
    elif option == 2 and shallowCrossPointChance >= 50:
      river.shallowCrossPoint()
    elif option == 2 and shallowCrossPointChance < 50:
      print("Sorry no cross point!")
      print("You now HAVE to cross the river by fording!")
      input("Please enter to continue!")
      river.crossRiver(wagon, leader, personOne, personTwo, personThree, personFour)





