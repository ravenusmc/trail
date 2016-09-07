import random 
import pandas as pd

#This is where the wagon class will be. 
class Wagon():

  def __init__(self, ration, health, weather, month):
    self.ration = ration
    self.health = health 
    self.weather = weather
    self.month = month 
    self.oxen = 0
    self.food = 0
    self.cloth = 0
    self.wheel = 0
    self.axle = 0
    self.tongue = 0
    self.speed = 0
    self.distance = 2000
  
  #This method is what will determine the weather type. I really think, that I should have had some trail class
  #and off of that had a wagon and human class subordinate to that class. 
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

  #This method was probably the most annoying thing to write! It essentially changes the date for the player. 
  #it takes in the starting date that the player entered and then increases that date by one. Not a hard thing to do
  #but actually doing this took a lot of time to find something that was simple to use and which I understood. 
  def changeDate(self):
    startdate = self.month
    self.month = pd.to_datetime(startdate) + pd.DateOffset(days=1)

# month = "3/1/1848"
# wagon = Wagon("Meager", "Good", "Sunny", month)
# print(wagon.month)
# wagon.changeDate()
# print(wagon.month)
# wagon.changeDate()
# print(wagon.month)

# wagon.changeDate()
# print(wagon.month)




