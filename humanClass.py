from wagon import *
import random 

class Human():

  def __init__(self, name, job):
    self.name = name 
    self.job = job 
    self.money = 0
    self.life = 30
    self.infected = False 

  #This method will drain the life from each of the player objects a little bit each day. It's a tough 
  #journey. In order for the life to go back up, the wagon has got to stop. 
  def lifeDrop(self, wagon):
    if wagon.ration == "Meager":
      self.life -= 5
    elif wagon.ration == "Normal":
      self.life -= 4
    elif wagon.ration == "Tons":
      self.life -= 3

  #This method will increase the life of the party when they are resting. 
  def lifeIncrease(self, wagon):
    if wagon.ration == "Tons" and self.infected = False:
      self.life += 5
    elif wagon.ration == "Normal" and self.infected = False:
      self.life += 4
    elif wagon.ration == "Meager" and self.infected = False:
      self.life += 3
    elif wagon.ration == "Tons" and self.infected = True:
      self.life += 4
    elif wagon.ration == "Normal" and self.infected = True:
      self.life += 3
    elif wagon.ration == "Meager" and self.infected = True:
      self.life += 3


  def diseaseInfection(self):
    diseaseChance = random.randint(1, 10)
    diseases = ["typhoid", "Yellow Fever", "cholera"]
    diseaseName = random.randint(0,2)

    if diseaseChance > 7 and self.infected == False:
      disease = diseases[diseaseName]
      self.infected = True 
      print(self.name + " has been infected with: " + disease)

  def rest(self):
    healthyChance = random.randint(1,10)
    if self.infected = True && healthyChance < 5: 
      print(self.name + " is disease free!")






mike = Human("Mike", "Banker")
beth = Human("Beth", "Cook")
mike.diseaseInfection()
beth.diseaseInfection()




    
