import random 

class River():

  #This function will be for the wagon to cross the river. It does use the random number generator to determine
  #if the wagon will tip over. Also, I will have another random number to see if someone will drown and thus die. 
  def crossRiver(self, wagon, leader, personOne, personTwo, personThree, personFour):
    fallIntoRiver = random.randint(1, 300)
    print("You decide to cross the river!")
    if fallIntoRiver >= 275: #In order for the wagon to tip over the random number has to be above 275 out of 300.
      drownChance = random.randint(1,1000)
      #This is a list of the people in the wagon. One of them will randomly be selected based on a random number.
      people = [leader, personOne, personTwo, personThree, personFour]
      personDie = random.randint(0,4)
      #In order for someone to die, the drown chance has to be greater than or equal to 925 out of 1000. 
      if drownChance >= 925 and leader.alive == True or personOne.alive == True or personTwo.alive == True or personThree.alive == True or personFour.alive == True:
        print(people[personDie].name + " drown!")
        people[personDie].alive = False 
      print("The wagon turned over...")
      print("You lose the following: ")
      #I could have made the wagon lose more or made it randomly generated. For now it will be this small amount. 
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


  def shallowCrossPoint(self):
    print("You safely cross the river!")
    print("No one got hurt or died in the crossing")
    input("Press enter to continue!")
