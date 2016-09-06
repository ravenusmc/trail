import random 

#This is where the wagon class will be. 
class Wagon():

  def __init__(self, ration, health, weather):
    self.ration = ration
    self.health = health 
    self.weather = weather 
    self.oxen = 0
    self.food = 100
    self.cloth = 0
    self.wheel = 0
    self.axle = 0
    self.tongue = 0
    self.speed = 0
    self.distance = 2000
    

  def weatherType(self):
    weatherType = random.randint(1,3) 
    if weatherType == 1:
      self.weather = "Sunny"
    elif weatherType == 2:
      self.weather = "Cloudy"
    elif weatherType == 3:
      self.weather = "Rainy"
    

  #This method will keep track of the speed and subtract that number from the distance each day. 
  def move(self):
    self.speed = 2.5 * self.oxen
    self.distance -= self.speed 
    if self.distance == 0:
        print("You have reached Oregon!")

  #This will affect the amount of food eating by the ration level. I decided to place this method here 
  #and not in the human class becuase one cannot change the individual ration levels-as of now. Thus, 
  #since ration and food are properties of wagon I figured it would be easier to keep them here. 
  def eat(self):
    if self.ration == "Meager":
      self.food -= .25
    elif self.ration == "Normal":
      self.food -= .5
    elif self.ration == "Tons":
      self.food -= 1

  #This method will determine the overall health for the wagon. 
  def healthLevel(self, leader, personOne, personTwo, personThree, personFour):
    if leader.life > 20 and personOne.life > 20 and personTwo.life > 20 and personThree.life > 20 and personFour.life > 20:
      self.health = "Good"
    elif leader.life > 10 and personOne.life > 10 and personTwo.life > 10 and personThree.life > 10 and personFour.life > 10:
      self.health = "Average"
    elif leader.life > 5 and personOne.life > 5 and personTwo.life > 5 and personThree.life > 5 and personFour.life > 5:
      self.health = "Poor"

  
wagon = Wagon("Meager", "Good", "Sunny")
wagon.weatherType()
print(wagon.weather)



