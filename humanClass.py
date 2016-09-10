from wagon import *
import random 

#The human class will monitor all aspects of the individual players in the Oregon Trail. Many of the methods
#Will do such things as monitor the human objects life either decreasing or increasing it. I did think about 
#writing a whole seperate disease class but figured I will keep the diseases here since they will affect human life.
#However, if I were to build this again I probably would have a seperate disease class. 
class Human():

  def __init__(self, name, job):
    self.name = name 
    self.job = job 
    self.money = 0
    self.life = 30
    self.infected = False
    self.alive = True  

  #This method will drain the life from each of the player objects a little bit each day. It's a tough 
  #journey. In order for the life to go back up, the wagon has got to stop. 
  def lifeDrop(self, wagon):
    if wagon.ration == "Meager" and self.alive == True:
      self.life -= 5
    elif wagon.ration == "Normal" and self.alive == True:
      self.life -= 4
    elif wagon.ration == "Tons" and self.alive == True:
      self.life -= 3

  #This method will increase the life of the party when they are resting. 
  def lifeIncrease(self, wagon):
    if wagon.ration == "Tons" and self.infected == False and self.alive == True:
      self.life += 5
    elif wagon.ration == "Normal" and self.infected == False and self.alive == True:
      self.life += 4
    elif wagon.ration == "Meager" and self.infected == False and self.alive == True:
      self.life += 3
    elif wagon.ration == "Tons" and self.infected == True and self.alive == True:
      self.life += 4
    elif wagon.ration == "Normal" and self.infected == True and self.alive == True:
      self.life += 2
    elif wagon.ration == "Meager" and self.infected == True and self.alive == True:
      self.life += 1

  #This method will assign a disease to an individual at a random point.
  def diseaseInfection(self):
    diseaseChance = random.randint(1, 10)
    diseases = ["typhoid", "Yellow Fever", "cholera"]
    diseaseName = random.randint(0,2)

    if diseaseChance > 7 and self.infected == False and self.alive == True:
      disease = diseases[diseaseName]
      self.infected = True 
      print(self.name + " has been infected with: " + disease)
      print("You best stop the wagon and rest!")
      input("Press Enter to continue! You best rest to help " + self.name)

  #This is the method which will slowly kill the disease infected party member if they do not rest. 
  def diseaseKilling(self):
    if self.infected == True and self.alive == True: 
      self.life -= 3
    print("")
    print(self.name + " is infected with illness.")
    print("You best stop the wagon and rest!")
    input("Press Enter to continue! You best rest to help " + self.name)

  #This method will work to heal the individual from their disease when the wagon is not moving. 
  def rest(self):
    healthyChance = random.randint(1,10)
    if self.infected == True and healthyChance < 5 and self.alive == True: 
      print(self.name + " is disease free!")



# mike = Human("Mike", "Banker")
# beth = Human("Beth", "Cook")
# mike.diseaseInfection()
# beth.diseaseInfection()
# mike.diseaseKilling()
# beth.diseaseKilling()




    
