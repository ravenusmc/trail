import random 

class River():

  def crossRiver(self, wagon, leader, personOne, personTwo, personThree, personFour):
    fallIntoRiver = random.randint(1, 300)
    print("You decide to cross the river!")
    if fallIntoRiver >= 1:
      drownChance = random.randint(1,1000)
      people = [leader, personOne, personTwo, personThree, personFour]
      personDie = random.randint(0,4)
      if drownChance >= 925 and leader.alive == True or personOne.alive == True or personTwo.alive == True or personThree.alive == True or personFour.alive == True:
        print(people[personDie].name + " drown!")
        people[personDie].alive = False 
      print("The wagon turned over...")
      print("You lose the following: ")
      wagon.food -= 50
      wagon.wheel -= 1
      wagon.bullets -= 3
      print("50 pounds of Food!")
      print("1 Wheel")
      print("5 bullets")
      print(people[personDie].name)
    else:
      print("You made it across the river!")
    input("Press enter to continue!")


  def shallowCrossPoint(self, wagon, leader, personOne, personTwo, personThree, personFour):
    print("shallow")
